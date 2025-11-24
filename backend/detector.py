import cv2
from ultralytics import YOLO
import time
import math
from collections import deque

class VehicleDetector:
    def __init__(self, stream_url, model_path='yolov8n.pt'):
        self.stream_url = stream_url
        self.model_path = model_path

        print(f"載入 YOLO 模型: {model_path}")
        self.model = YOLO(model_path)
        self.model.to('cpu')

        print(f"連接視頻流: {stream_url}")
        self.cap = cv2.VideoCapture(stream_url)

        ret, first_frame = self.cap.read()
        if ret:
            frame_height, frame_width = first_frame.shape[:2]
            self.reference_line_y = frame_height // 2
            self.frame_width = frame_width
            self.frame_height = frame_height
            print(f"畫面尺寸: {frame_width}x{frame_height}")
            print(f"參考線位置: y={self.reference_line_y}")
        else:
            raise Exception("無法讀取視頻流")

        self.tracked_vehicles = {}
        self.next_vehicle_id = 1
        self.detection_distance_threshold = 50

        self.northbound_count = 0
        self.southbound_count = 0

        self.northbound_images = deque(maxlen=10)
        self.southbound_images = deque(maxlen=10)

        self.fps = 0
        self.frame_count = 0
        self.fps_start_time = time.time()

        self.vehicle_classes = [2, 3]

        self.new_vehicle_data = None

    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def process_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            print("無法讀取幀，嘗試重新連接...")
            self.cap.release()
            self.cap = cv2.VideoCapture(self.stream_url)
            return None, self.get_stats(), None

        current_time = time.time()
        current_detections = []
        self.new_vehicle_data = None

        results = self.model(frame, verbose=False, device='cpu')

        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    cls_id = int(box.cls[0])

                    if cls_id in self.vehicle_classes:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        centroid = ((x1 + x2) // 2, (y1 + y2) // 2)
                        confidence = float(box.conf[0])
                        class_name = self.model.names[cls_id]

                        current_detections.append({
                            'centroid': centroid,
                            'class': class_name,
                            'bbox': (x1, y1, x2, y2),
                            'confidence': confidence
                        })

                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        label = f"{class_name}: {confidence:.2f}"
                        cv2.putText(frame, label, (x1, y1 - 10),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        self.track_vehicles(current_detections, current_time, frame)

        cv2.line(frame, (0, self.reference_line_y),
                (self.frame_width, self.reference_line_y), (0, 0, 255), 3)
        cv2.putText(frame, "Reference Line",
                   (self.frame_width - 200, self.reference_line_y - 10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        self.frame_count += 1
        if self.frame_count % 30 == 0:
            self.fps = 30 / (time.time() - self.fps_start_time)
            self.fps_start_time = time.time()

        return frame, self.get_stats(), self.new_vehicle_data

    def track_vehicles(self, current_detections, current_time, frame):
        matched_ids = set()

        for detection in current_detections:
            centroid = detection['centroid']
            class_name = detection['class']
            bbox = detection['bbox']

            matched_id = None
            min_dist = float('inf')

            for vehicle_id, vehicle_info in self.tracked_vehicles.items():
                if vehicle_info['class'] == class_name:
                    dist = self.distance(centroid, vehicle_info['centroid'])
                    if dist < self.detection_distance_threshold and dist < min_dist:
                        min_dist = dist
                        matched_id = vehicle_id

            if matched_id is not None:
                old_y = self.tracked_vehicles[matched_id]['centroid'][1]
                new_y = centroid[1]

                if not self.tracked_vehicles[matched_id]['counted']:
                    x1, y1, x2, y2 = bbox
                    vehicle_img = frame[y1:y2, x1:x2].copy()

                    if old_y < self.reference_line_y <= new_y:
                        self.southbound_count += 1
                        self.tracked_vehicles[matched_id]['counted'] = True
                        print(f"南下車輛 +1 ({class_name}) - 總南下: {self.southbound_count}")

                        if vehicle_img.size > 0:
                            self.new_vehicle_data = {
                                'direction': 'southbound',
                                'image': vehicle_img,
                                'class': class_name,
                                'timestamp': time.strftime('%H:%M:%S')
                            }

                    elif old_y > self.reference_line_y >= new_y:
                        self.northbound_count += 1
                        self.tracked_vehicles[matched_id]['counted'] = True
                        print(f"北上車輛 +1 ({class_name}) - 總北上: {self.northbound_count}")

                        if vehicle_img.size > 0:
                            self.new_vehicle_data = {
                                'direction': 'northbound',
                                'image': vehicle_img,
                                'class': class_name,
                                'timestamp': time.strftime('%H:%M:%S')
                            }

                self.tracked_vehicles[matched_id]['centroid'] = centroid
                self.tracked_vehicles[matched_id]['last_seen'] = current_time
                matched_ids.add(matched_id)
            else:
                self.tracked_vehicles[self.next_vehicle_id] = {
                    'centroid': centroid,
                    'class': class_name,
                    'last_seen': current_time,
                    'counted': False
                }
                matched_ids.add(self.next_vehicle_id)
                self.next_vehicle_id += 1

        vehicles_to_remove = []
        for vehicle_id, vehicle_info in self.tracked_vehicles.items():
            if current_time - vehicle_info['last_seen'] > 3.0:
                vehicles_to_remove.append(vehicle_id)

        for vehicle_id in vehicles_to_remove:
            del self.tracked_vehicles[vehicle_id]

    def get_stats(self):
        return {
            'southbound': self.southbound_count,
            'northbound': self.northbound_count,
            'total': self.northbound_count + self.southbound_count,
            'fps': round(self.fps, 1)
        }

    def release(self):
        if self.cap:
            self.cap.release()
        print("檢測器資源已釋放")
