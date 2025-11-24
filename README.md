# 🚦 台北市交通監控系統 - 車輛方向檢測

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![YOLO](https://img.shields.io/badge/YOLO-v8n-green.svg)](https://github.com/ultralytics/ultralytics)

### 語言 / Language

**[繁體中文](README.md)** | **[English](README_EN.md)**

</div>

---

一個基於 YOLOv8 的即時交通監控系統，能夠自動檢測並統計南下與北上車輛數量，支援 GUI 桌面版和 Web 版本。
<img width="<img width="1280" height="747" alt="3" src="https://github.com/user-attachments/assets/38c6a0b5-b7c1-4b13-a77e-f5fbb47a5d67" />

<img width="1280" height="764" alt="30" src="https://github.com/user-attachments/assets/c287d7a1-62ec-4590-8b10-e30a311b971e" />
<img width="1280" height="747" alt="40" src="https://github.com/user-attachments/assets/467d4bea-b496-473c-a1b8-2d6f12a608f6" />

## 📋 目錄

- [專案簡介](#專案簡介)
- [功能特色](#功能特色)
- [系統架構](#系統架構)
- [快速開始](#快速開始)
- [YOLO 模型選擇](#yolo-模型選擇)
- [使用說明](#使用說明)
- [技術棧](#技術棧)
- [貢獻指南](#貢獻指南)
- [授權協議](#授權協議)

## 🎯 專案簡介

本系統專為交通管理與執法人員設計，提供以下核心功能：

- **即時車輛檢測**：使用 YOLOv8 模型進行高效的車輛識別
- **方向統計**：自動判斷車輛行駛方向（南下/北上）
- **車輛截圖**：自動捕捉穿越參考線的車輛影像
- **繁體中文支援**：完整的繁體中文界面
- **雙版本支援**：提供 GUI 桌面版和 Web 網頁版

### 應用場景

- 交通流量監控
- 違規車輛追蹤
- 交通數據分析
- 智慧城市建設

## ✨ 功能特色

### 核心功能

✅ **智能車輛檢測**
- 支援汽車（car）和摩托車（motorcycle）識別
- 高準確率的即時檢測
- 可調整的信心閾值

✅ **方向判斷系統**
- 自動識別南下/北上方向
- 基於參考線的穿越檢測
- 防止重複計數

✅ **視覺化界面**
- 現代化白色風格設計
- 超大號統計數字顯示（48pt）
- 彩色卡片式布局
- 即時 FPS 監控

✅ **車輛記錄**
- 自動截圖保存
- 顯示車輛類型和時間戳
- 分類展示（北上/南下）
- 最多保存 10 張記錄

## 🏗️ 系統架構

```
traffic-monitor-system/
├── frontend/               # Web 前端
│   ├── index.html         # 主頁面
│   ├── css/
│   │   └── style.css      # 樣式表
│   └── js/
│       └── app.js         # 前端邏輯
├── backend/               # Python 後端
│   ├── app.py            # Flask 應用主程式
│   ├── detector.py       # YOLO 檢測器
│   └── requirements.txt  # Python 依賴
├── models/               # YOLO 模型文件
│   └── README.md         # 模型說明
├── docs/                 # 文檔
│   └── MODEL_COMPARISON.md
├── traffic_stream_detection_gui.py  # GUI 桌面版
└── README.md             # 本文件
```

## 🚀 快速開始

### 前置需求

- Python 3.8 或更高版本
- pip 套件管理器
- 支援 CUDA 的 GPU

### 安裝步驟

#### 1. 克隆專案

```bash
git clone https://github.com/yourusername/traffic-monitor-system.git
cd traffic-monitor-system
```

#### 2. 創建虛擬環境

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

#### 3. 安裝依賴

```bash
pip install -r backend/requirements.txt
```

#### 4. 下載 YOLO 模型

```bash
# 模型會在首次運行時自動下載
# 或手動下載到 models/ 目錄
```

### 運行應用

#### GUI 桌面版

```bash
python traffic_stream_detection_gui.py
```

#### Web 版本

```bash
# 啟動後端服務
cd backend
python app.py

# 在瀏覽器中訪問
# http://localhost:5000
```

## 📊 YOLO 模型選擇

本系統支援多種 YOLO 模型，以下是詳細對比：

| 模型 | 大小 | 速度 (FPS) | mAP | 準確度 | 記憶體使用 | 推薦場景 |
|------|------|-----------|-----|--------|-----------|---------|
| **YOLOv8n** ⭐ | 6.3 MB | 45-60 | 37.3% | ⭐⭐⭐ | 低 | 即時監控、CPU運行 |
| YOLOv8s | 22 MB | 35-45 | 44.9% | ⭐⭐⭐⭐ | 中 | 平衡性能與準確度 |
| YOLOv8m | 52 MB | 25-35 | 50.2% | ⭐⭐⭐⭐⭐ | 高 | 高準確度需求 |
| YOLOv11n | 5.5 MB | 50-65 | 39.5% | ⭐⭐⭐⭐ | 低 | 最新優化、航拍視角 |

### 為什麼使用 YOLOv8n？

✅ **速度優勢**
- CUDA GPU環境下運行
- YOLOv8n模型適中，低延遲，適合即時應用

✅ **資源友好**
- 模型僅 6.3 MB，快速加載
- 記憶體佔用低，適合長時間運行

✅ **準確度足夠**
- 對於汽車和摩托車檢測，準確度已滿足需求
- mAP 37.3% 在小目標檢測上表現良好

✅ **生態成熟**
- Ultralytics 官方支援
- 社群資源豐富

### 切換模型

修改配置文件中的模型路徑：

```python
# 在 traffic_stream_detection_gui.py 中
MODEL_PATH = "yolov8n.pt"  # 改為其他模型，如 "yolov8s.pt"
```

## 📖 使用說明

### GUI 桌面版操作

1. **啟動應用**
   ```bash
   python traffic_stream_detection_gui.py
   ```

2. **界面說明**
   - **頂部卡片**：顯示南下、北上、總計車輛數和 FPS
   - **左側視窗**：即時監控畫面，紅色參考線橫跨中央
   - **右側列表**：最近通過的車輛截圖（上：北上，下：南下）

3. **關鍵功能**
   - 系統自動連接到台北市交通攝像頭
   - 車輛穿越紅線時自動統計和截圖
   - 點擊關閉按鈕退出

### Web 版本操作

1. **訪問網頁**
   - 打開瀏覽器訪問 `http://localhost:5000`

2. **功能使用**
   - 即時查看監控畫面
   - 查看統計數據
   - 瀏覽車輛記錄

## 🛠️ 技術棧

### 桌面版

- **Python 3.8+**
- **OpenCV** - 影像處理
- **Ultralytics YOLO** - 物件檢測
- **Tkinter** - GUI 框架
- **Pillow** - 圖像處理和中文字體支援

### Web 版

#### 前端
- **HTML5** - 結構
- **CSS3** - 樣式（現代白色風格）
- **JavaScript (ES6+)** - 互動邏輯
- **WebSocket** - 即時通訊

#### 後端
- **Flask** - Web 框架
- **Flask-SocketIO** - WebSocket 支援
- **OpenCV** - 影像處理
- **Ultralytics YOLO** - 物件檢測

## 📁 專案文件說明

### 核心文件

- `traffic_stream_detection_gui.py` - GUI 桌面版主程式
- `backend/app.py` - Flask 後端服務
- `backend/detector.py` - YOLO 檢測器封裝
- `frontend/index.html` - Web 版前端頁面

### 配置文件

- `backend/requirements.txt` - Python 依賴列表
- `.gitignore` - Git 忽略規則

## 🤝 貢獻指南

歡迎貢獻！請遵循以下步驟：

1. Fork 本專案
2. 創建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

### 開發規範

- 遵循 PEP 8 代碼風格
- 添加適當的註釋
- 更新相關文檔

## 🐛 問題回報

如遇到問題，請在 [Issues](https://github.com/yourusername/traffic-monitor-system/issues) 頁面提交。

提交時請包含：
- 系統環境（OS、Python 版本）
- 錯誤訊息
- 復現步驟

## 📝 更新日誌

### v1.0.0 (2024-01-XX)
- ✨ 初始版本發布
- ✅ GUI 桌面版
- ✅ Web 網頁版
- ✅ 繁體中文支援
- ✅ 車輛方向檢測
- ✅ 自動截圖功能

## 📜 授權協議

本專案採用 MIT 授權協議 - 詳見 [LICENSE](LICENSE) 文件

## 👥 作者

- **JammyLin**

## 🙏 致謝

- [Ultralytics](https://github.com/ultralytics/ultralytics) - YOLO 模型
- [台北市政府](https://gov.taipei/) - 開放資料交通攝像頭數據源

---

⭐ 如果這個專案對您有幫助，請給個 Star！
