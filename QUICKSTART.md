# 🚀 快速開始指南

## 5 分鐘快速部署

### 步驟 1: 安裝 Python

確保您已安裝 Python 3.8 或更高版本：

```bash
python --version
# 應顯示：Python 3.8.x 或更高
```

如未安裝，請訪問：https://www.python.org/downloads/

### 步驟 2: 克隆專案

```bash
git clone https://github.com/yourusername/traffic-monitor-system.git
cd traffic-monitor-system
```

### 步驟 3: 安裝依賴

```bash
pip install -r backend/requirements.txt
```

### 步驟 4: 運行應用

#### 選項 A：GUI 桌面版（推薦新手）

```bash
python traffic_stream_detection_gui.py
```

#### 選項 B：Web 版本

**Windows:**
```bash
start_web.bat
```

**Linux/Mac:**
```bash
cd backend
python app.py
```

然後在瀏覽器訪問：http://localhost:5000

## ✅ 驗證安裝

成功啟動後，您應該看到：

### GUI 版本
- 現代白色界面
- 頂部有 4 個彩色統計卡片
- 中間顯示即時視頻
- 右側顯示車輛縮略圖

### Web 版本
- 瀏覽器自動打開
- 顯示即時監控畫面
- 統計數據即時更新

## 🐛 常見問題

### 問題 1：無法連接視頻流

**解決方案：**
1. 檢查網絡連接
2. 確認視頻流 URL 有效
3. 嘗試重啟應用

### 問題 2：CUDA/GPU 錯誤

**解決方案：**
```python
# 在代碼中強制使用 CPU
model.to('cpu')
```

### 問題 3：模塊未找到

**解決方案：**
```bash
pip install --upgrade -r backend/requirements.txt
```

### 問題 4：中文字體顯示問題（僅 GUI 版）

**解決方案：**
確保系統已安裝 Microsoft JhengHei 字體（Windows 自帶）

## 📊 使用技巧

### 調整檢測參數

編輯 `traffic_stream_detection_gui.py` 或 `backend/detector.py`：

```python
# 調整信心閾值（預設 0.25）
results = model(frame, conf=0.35)  # 減少誤報

# 調整 IOU 閾值（預設 0.45）
results = model(frame, iou=0.55)  # 減少重複檢測
```

### 切換模型

```python
# 在配置文件中修改
MODEL_PATH = "yolov8n.pt"  # 改為 "yolov8s.pt" 或其他
```

### 調整參考線位置

```python
# 在 VehicleDetector.__init__ 中
self.reference_line_y = frame_height // 2  # 中間
self.reference_line_y = frame_height // 3  # 上方 1/3
```

## 🎓 下一步

1. 閱讀完整 [README.md](README.md)
2. 查看 [MODEL_COMPARISON.md](docs/MODEL_COMPARISON.md) 了解模型選擇
3. 自定義界面顏色和樣式
4. 部署到生產環境

## 💬 獲取幫助

- 📖 查看文檔：[README.md](README.md)
- 🐛 報告問題：[GitHub Issues](https://github.com/yourusername/traffic-monitor-system/issues)
- 💡 討論功能：[Discussions](https://github.com/yourusername/traffic-monitor-system/discussions)

## 🎉 開始使用！

現在您已經成功安裝並運行了系統，開始監控交通吧！

---

有問題？查看 [README.md](README.md) 獲取更多詳細信息。
