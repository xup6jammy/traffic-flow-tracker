# 📁 專案結構說明

## 目錄樹狀圖

```
traffic-monitor-system/
├── 📄 README.md                          # 專案主要文檔
├── 📄 QUICKSTART.md                      # 快速開始指南
├── 📄 LICENSE                            # MIT 授權協議
├── 📄 .gitignore                         # Git 忽略規則
├── 📄 start_web.bat                      # Web 版啟動腳本(Windows)
├── 📄 traffic_stream_detection_gui.py   # GUI 桌面版主程式
│
├── 📂 frontend/                          # Web 前端
│   ├── 📄 index.html                    # 主頁面
│   ├── 📂 css/
│   │   └── 📄 style.css                 # 樣式表（現代白色風格）
│   └── 📂 js/
│       └── 📄 app.js                    # 前端邏輯（Socket.IO 通訊）
│
├── 📂 backend/                           # Python 後端
│   ├── 📄 app.py                        # Flask 應用主程式
│   ├── 📄 detector.py                   # YOLO 檢測器封裝
│   └── 📄 requirements.txt              # Python 依賴列表
│
├── 📂 models/                            # YOLO 模型文件
│   └── 📄 README.md                     # 模型下載和使用說明
│
└── 📂 docs/                              # 文檔目錄
    └── 📄 MODEL_COMPARISON.md           # YOLO 模型詳細對比
```

## 📄 文件說明

### 根目錄文件

| 文件 | 說明 | 用途 |
|------|------|------|
| `README.md` | 專案主要文檔 | 專案介紹、安裝指南、使用說明 |
| `QUICKSTART.md` | 快速開始指南 | 5 分鐘快速部署教程 |
| `LICENSE` | 授權協議 | MIT 開源許可證 |
| `.gitignore` | Git 忽略配置 | 指定不納入版本控制的文件 |
| `start_web.bat` | 啟動腳本 | Windows 快速啟動 Web 版本 |
| `traffic_stream_detection_gui.py` | GUI 版主程式 | Tkinter 桌面應用程式 |

### frontend/ - Web 前端

#### index.html
```html
<!-- 主要結構 -->
<div class="stats-container">     <!-- 頂部統計卡片 -->
<div class="video-section">       <!-- 左側視頻區域 -->
<div class="thumbnails-section">  <!-- 右側縮略圖 -->
```

**技術棧：**
- HTML5 - 結構
- CSS3 - 樣式（Flexbox, Grid）
- JavaScript ES6+ - 互動邏輯
- Socket.IO Client - 即時通訊

#### css/style.css
- 現代白色風格設計
- 響應式布局
- 自定義滾動條
- 動畫效果（淡入、懸停）
- 卡片式設計

**主要樣式：**
```css
.stats-container    # 統計卡片容器（Grid 布局）
.stat-card          # 單個統計卡片
.video-section      # 視頻顯示區域
.thumbnails-section # 縮略圖側邊欄
```

#### js/app.js
- Socket.IO 連接管理
- 視頻幀即時更新
- 統計數據動畫
- 車輛縮略圖管理
- 連接狀態監控

**主要功能：**
```javascript
socket.on('video_frame')    # 接收視頻幀
socket.on('stats_update')   # 更新統計數據
socket.on('new_vehicle')    # 新增車輛縮略圖
animateValue()              # 數字動畫效果
```

### backend/ - Python 後端

#### app.py - Flask 應用
**主要功能：**
- Flask 伺服器初始化
- Socket.IO 事件處理
- 靜態文件服務
- 視頻處理線程管理

**關鍵端點：**
```python
@app.route('/')              # 主頁面
@socketio.on('connect')      # 客戶端連接
video_processing_thread()    # 視頻處理
```

**架構：**
```
Flask App
  ├─ SocketIO (WebSocket)
  ├─ Video Thread (背景處理)
  └─ VehicleDetector (檢測器)
```

#### detector.py - 檢測器
**類：VehicleDetector**

**主要方法：**
```python
__init__()           # 初始化模型和視頻流
process_frame()      # 處理單幀並返回結果
track_vehicles()     # 車輛跟踪和方向判斷
get_stats()          # 獲取統計數據
```

**檢測流程：**
```
視頻流 → YOLO 檢測 → 車輛跟踪 → 方向判斷 → 截圖保存
```

#### requirements.txt
**依賴分類：**
- Web 框架：Flask, Flask-SocketIO
- 電腦視覺：OpenCV, Ultralytics
- 深度學習：PyTorch, TorchVision
- 其他：NumPy, Pillow, Requests

### models/ - 模型目錄

存放 YOLO 模型文件（`.pt` 格式）

**支援模型：**
- yolov8n.pt（6.3 MB）- 預設
- yolov8s.pt（22 MB）
- yolov8m.pt（52 MB）
- yolo11n.pt（5.5 MB）

### docs/ - 文檔目錄

#### MODEL_COMPARISON.md
詳細的 YOLO 模型對比文檔：
- 性能測試數據
- 準確度對比
- 使用場景建議
- 優化技巧
- 成本效益分析

## 🔄 數據流程圖

### GUI 版本
```
用戶啟動程式
    ↓
初始化 YOLO 模型
    ↓
連接 M3U8 視頻流
    ↓
主循環 ←─────────┐
  ├─ 讀取幀      │
  ├─ YOLO 檢測   │
  ├─ 車輛跟踪    │
  ├─ 方向判斷    │
  ├─ 更新 GUI    │
  └────────────→┘
```

### Web 版本
```
用戶訪問網頁
    ↓
前端建立 Socket 連接
    ↓
後端初始化檢測器
    ↓
視頻處理線程 ←────────┐
  ├─ 處理視頻幀       │
  ├─ YOLO 檢測        │
  ├─ 車輛跟踪         │
  ├─ 編碼為 Base64    │
  ├─ Socket 發送      │
  └──────────────→  ┘
    ↓
前端接收並顯示
```

## 🛠️ 擴展指南

### 添加新功能

#### 1. 新增統計類型

**前端（index.html）：**
```html
<div class="stat-card custom">
    <div class="stat-value" id="custom-value">0</div>
</div>
```

**後端（detector.py）：**
```python
def get_stats(self):
    return {
        'custom': self.custom_count
    }
```

#### 2. 修改檢測類別

**detector.py：**
```python
# 添加更多車輛類型
self.vehicle_classes = [2, 3, 5, 7]  # car, motorcycle, bus, truck
```

#### 3. 自定義參考線

**detector.py：**
```python
# 修改參考線位置
self.reference_line_y = frame_height // 3  # 上方 1/3 處
```

### 部署到生產環境

#### 1. 使用 Gunicorn（Linux）

```bash
pip install gunicorn
gunicorn -k eventlet -w 1 --bind 0.0.0.0:5000 backend.app:app
```

#### 2. 使用 Nginx 反向代理

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

#### 3. 使用 Docker

創建 `Dockerfile`：
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "backend/app.py"]
```

## 📊 性能優化

### 前端優化
- 使用 CDN 加載 Socket.IO
- 圖片懶加載
- 減少不必要的 DOM 操作

### 後端優化
- 調整視頻幀率（30 FPS → 15 FPS）
- 降低圖像解析度
- 使用 GPU 加速（如可用）

## 🔐 安全建議

1. **生產環境配置：**
   ```python
   app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
   ```

2. **HTTPS 部署：**
   使用 Let's Encrypt 免費證書

3. **CORS 限制：**
   ```python
   CORS(app, resources={r"/*": {"origins": "https://your-domain.com"}})
   ```

## 📚 參考資源

- [Flask 文檔](https://flask.palletsprojects.com/)
- [Socket.IO 文檔](https://socket.io/docs/)
- [Ultralytics YOLO](https://docs.ultralytics.com/)
- [OpenCV 教程](https://docs.opencv.org/)

---

需要更多幫助？查看 [README.md](README.md) 或提交 [Issue](https://github.com/yourusername/traffic-monitor-system/issues)。
