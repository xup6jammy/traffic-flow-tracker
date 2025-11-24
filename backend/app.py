from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import cv2
import base64
import time
from threading import Thread, Lock
from detector import VehicleDetector
import os

app = Flask(__name__,
            static_folder='../frontend',
            template_folder='../frontend')
app.config['SECRET_KEY'] = 'your-secret-key-here'

CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

detector = None
detector_lock = Lock()
is_running = False

STREAM_URL = "https://jtmctrafficcctv3.gov.taipei/NVR/14834171-3d56-4081-99e9-77ac645f1362/live.m3u8"

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend', path)

def video_processing_thread():
    global is_running, detector

    print("視頻處理線程已啟動")

    while is_running:
        try:
            with detector_lock:
                if detector is None:
                    continue

                frame, stats, new_vehicle = detector.process_frame()

                if frame is not None:
                    _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
                    frame_base64 = base64.b64encode(buffer).decode('utf-8')

                    socketio.emit('video_frame', {'frame': frame_base64})

                    socketio.emit('stats_update', stats)

                    if new_vehicle:
                        _, thumb_buffer = cv2.imencode('.jpg', new_vehicle['image'])
                        thumb_base64 = base64.b64encode(thumb_buffer).decode('utf-8')

                        socketio.emit('new_vehicle', {
                            'direction': new_vehicle['direction'],
                            'image': thumb_base64,
                            'class': new_vehicle['class'],
                            'timestamp': new_vehicle['timestamp']
                        })

        except Exception as e:
            print(f"視頻處理錯誤: {e}")
            time.sleep(0.1)

        time.sleep(0.033)

@socketio.on('connect')
def handle_connect():
    global is_running, detector

    print('客戶端已連接')

    with detector_lock:
        if detector is None:
            print("正在初始化 YOLO 檢測器...")
            detector = VehicleDetector(STREAM_URL)

        if not is_running:
            is_running = True
            thread = Thread(target=video_processing_thread, daemon=True)
            thread.start()

    emit('status', {'message': '已連接到服務器'})

@socketio.on('disconnect')
def handle_disconnect():
    print('客戶端已斷開連接')

@socketio.on('request_stats')
def handle_request_stats():
    with detector_lock:
        if detector:
            stats = detector.get_stats()
            emit('stats_update', stats)

if __name__ == '__main__':
    print("=" * 50)
    print("台北市交通監控系統 - Web 版本")
    print("=" * 50)
    print(f"服務器啟動中...")
    print(f"訪問地址: http://localhost:5000")
    print("按 Ctrl+C 停止服務器")
    print("=" * 50)

    socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)
