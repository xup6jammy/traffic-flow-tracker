import cv2
from ultralytics import YOLO
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import numpy as np
from collections import deque
import threading
import os
STREAM_URL = "https://jtmctrafficcctv3.gov.taipei/NVR/14834171-3d56-4081-99e9-77ac645f1362/live.m3u8"
MODEL_PATH = "yolov8n.pt"
VEHICLE_CLASSES = [2, 3]
def distance(p1, p2):
        main_container = tk.Frame(self.root, bg='#f5f5f5')
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        stats_container = tk.Frame(main_container, bg='#f5f5f5')
        stats_container.pack(fill=tk.X, pady=(0, 15))
        self.stats_labels = {}
        stats_info = [
            ('南下車輛', 'southbound', '#FF6B6B', '🔽'),
            ('北上車輛', 'northbound', '#4ECDC4', '🔼'),
            ('總計車輛', 'total', '#95E1D3', '📊'),
            ('FPS', 'fps', '#FFE66D', '⚡')
        ]
        for i, (text, key, color, icon) in enumerate(stats_info):
            card = tk.Frame(stats_container, bg='white', relief=tk.FLAT, borderwidth=0)
            card.pack(side=tk.LEFT, expand=True, padx=8, ipadx=20, ipady=15)
            card.config(highlightbackground='#e0e0e0', highlightthickness=1)
            header_frame = tk.Frame(card, bg='white')
            header_frame.pack(fill=tk.X, pady=(5, 0))
            icon_label = tk.Label(header_frame, text=icon, font=('Segoe UI Emoji', 20),
                                bg='white', fg=color)
            icon_label.pack(side=tk.LEFT, padx=(10, 5))
            title_label = tk.Label(header_frame, text=text,
                                 font=('Microsoft JhengHei', 13),
                                 bg='white', fg='#666666')
            title_label.pack(side=tk.LEFT)
            value = tk.Label(card, text='0',
                           font=('Microsoft JhengHei', 48, 'bold'),
                           bg='white', fg=color)
            value.pack(pady=(5, 10))
            self.stats_labels[key] = value
        content_frame = tk.Frame(main_container, bg='#f5f5f5')
        content_frame.pack(fill=tk.BOTH, expand=True)
        left_frame = tk.Frame(content_frame, bg='white', relief=tk.FLAT)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        left_frame.config(highlightbackground='#e0e0e0', highlightthickness=1)
        title_label = tk.Label(left_frame, text="即時監控畫面",
                               font=('Microsoft JhengHei', 16, 'bold'),
                               bg='white', fg='#333333')
        title_label.pack(pady=15)
        self.video_label = tk.Label(left_frame, bg='#000000')
        self.video_label.pack(padx=15, pady=(0, 15), fill=tk.BOTH, expand=True)
        right_frame = tk.Frame(content_frame, bg='white', relief=tk.FLAT)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        right_frame.config(width=280, highlightbackground='#e0e0e0', highlightthickness=1)
        north_frame = tk.Frame(right_frame, bg='white')
        north_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 5))
        north_title = tk.Label(north_frame, text="🔼 北上",
                              font=('Microsoft JhengHei', 12, 'bold'),
                              bg='white', fg='#4ECDC4')
        north_title.pack(pady=8)
        north_canvas = tk.Canvas(north_frame, bg='#fafafa', highlightthickness=0)
        north_scrollbar = ttk.Scrollbar(north_frame, orient="vertical", command=north_canvas.yview)
        self.north_container = tk.Frame(north_canvas, bg='#fafafa')
        self.north_container.bind(
            "<Configure>",
            lambda e: north_canvas.configure(scrollregion=north_canvas.bbox("all"))
        )
        north_canvas.create_window((0, 0), window=self.north_container, anchor="nw")
        north_canvas.configure(yscrollcommand=north_scrollbar.set)
        north_canvas.pack(side="left", fill="both", expand=True, padx=5)
        north_scrollbar.pack(side="right", fill="y")
        separator = tk.Frame(right_frame, bg='#e0e0e0', height=2)
        separator.pack(fill=tk.X, padx=10, pady=5)
        south_frame = tk.Frame(right_frame, bg='white')
        south_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        south_title = tk.Label(south_frame, text="🔽 南下",
                              font=('Microsoft JhengHei', 12, 'bold'),
                              bg='white', fg='#FF6B6B')
        south_title.pack(pady=8)
        south_canvas = tk.Canvas(south_frame, bg='#fafafa', highlightthickness=0)
        south_scrollbar = ttk.Scrollbar(south_frame, orient="vertical", command=south_canvas.yview)
        self.south_container = tk.Frame(south_canvas, bg='#fafafa')
        self.south_container.bind(
            "<Configure>",
            lambda e: south_canvas.configure(scrollregion=south_canvas.bbox("all"))
        )
        south_canvas.create_window((0, 0), window=self.south_container, anchor="nw")
        south_canvas.configure(yscrollcommand=south_scrollbar.set)
        south_canvas.pack(side="left", fill="both", expand=True, padx=5)
        south_scrollbar.pack(side="right", fill="y")
    def add_chinese_text(self, img, text, position, font_size=20, color=(255, 255, 255)):
        print("正在載入 YOLO 模型（使用 CPU 模式）...")
        self.model = YOLO(MODEL_PATH)
        self.model.to('cpu')
        print(f"正在連接視頻流: {STREAM_URL}")
        self.cap = cv2.VideoCapture(STREAM_URL)
        if not self.cap.isOpened():
            print("錯誤：無法打開視頻流")
            return
        ret, first_frame = self.cap.read()
        if ret:
            frame_height, frame_width = first_frame.shape[:2]
            self.reference_line_y = frame_height // 2
            print(f"畫面尺寸: {frame_width}x{frame_height}")
            print(f"參考線位置: y={self.reference_line_y}")
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.running = True
        detection_thread = threading.Thread(target=self.detection_loop, daemon=True)
        detection_thread.start()
    def detection_loop(self):
        matched_ids = set()
        for detection in current_detections:
            centroid = detection['centroid']
            class_name = detection['class']
            bbox = detection['bbox']
            matched_id = None
            min_dist = float('inf')
            for vehicle_id, vehicle_info in self.tracked_vehicles.items():
                if vehicle_info['class'] == class_name:
                    dist = distance(centroid, vehicle_info['centroid'])
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
                            self.southbound_images.append({
                                'image': vehicle_img,
                                'class': class_name,
                                'time': time.strftime('%H:%M:%S')
                            })
                            self.new_thumbnail = True
                    elif old_y > self.reference_line_y >= new_y:
                        self.northbound_count += 1
                        self.tracked_vehicles[matched_id]['counted'] = True
                        print(f"北上車輛 +1 ({class_name}) - 總北上: {self.northbound_count}")
                        if vehicle_img.size > 0:
                            self.northbound_images.append({
                                'image': vehicle_img,
                                'class': class_name,
                                'time': time.strftime('%H:%M:%S')
                            })
                            self.new_thumbnail = True
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
    def update_gui(self, frame):
        for widget in self.north_container.winfo_children():
            widget.destroy()
        for widget in self.south_container.winfo_children():
            widget.destroy()
        self.thumbnail_refs = []
        for i, vehicle_data in enumerate(reversed(list(self.northbound_images))):
            self.add_vehicle_thumbnail(self.north_container, vehicle_data, i, '北上')
        for i, vehicle_data in enumerate(reversed(list(self.southbound_images))):
            self.add_vehicle_thumbnail(self.south_container, vehicle_data, i, '南下')
    def add_vehicle_thumbnail(self, container, vehicle_data, index, direction):
        self.running = False
        if self.cap:
            self.cap.release()
        self.root.destroy()
def main():