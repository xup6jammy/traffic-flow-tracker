# YOLO 模型文件目錄

## 📁 目錄說明

此目錄用於存放 YOLO 模型文件（.pt 格式）。

## 📥 模型下載

### 自動下載

首次運行程式時，Ultralytics 會自動下載所需模型：

```bash
python traffic_stream_detection_gui.py
# 或
python backend/app.py
```

模型會自動下載到：
- Windows: `C:\Users\<用戶名>\.cache\ultralytics\`
- Linux/Mac: `~/.cache/ultralytics/`

### 手動下載

如果需要手動下載並放置到此目錄：

#### YOLOv8 系列

```bash
# YOLOv8n（推薦，6.3 MB）
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt

# YOLOv8s（22 MB）
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt

# YOLOv8m（52 MB）
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m.pt
```

#### YOLOv11 系列

```bash
# YOLOv11n（5.5 MB）
wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt

# YOLOv11s（20 MB）
wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11s.pt
```

或使用 Python：

```python
from ultralytics import YOLO

# 下載 YOLOv8n
model = YOLO('yolov8n.pt')

# 下載 YOLOv11n
model = YOLO('yolo11n.pt')
```

## 🔧 使用自定義模型

如果您訓練了自定義模型，請將 `.pt` 文件放在此目錄，並修改配置：

```python
# 在 traffic_stream_detection_gui.py 中
MODEL_PATH = "models/your_custom_model.pt"
```

## 📊 模型比較

| 模型 | 大小 | 速度 | 準確度 | 推薦用途 |
|------|------|------|--------|---------|
| yolov8n.pt ⭐ | 6.3 MB | ★★★★★ | ★★★ | 即時監控（預設）|
| yolov8s.pt | 22 MB | ★★★★ | ★★★★ | 平衡性能 |
| yolov8m.pt | 52 MB | ★★★ | ★★★★★ | 高準確度 |
| yolo11n.pt | 5.5 MB | ★★★★★ | ★★★★ | 最新優化 |

詳細對比請參考：[MODEL_COMPARISON.md](../docs/MODEL_COMPARISON.md)

## 🚫 .gitignore

模型文件通常較大，建議添加到 `.gitignore`：

```
# YOLO models
*.pt
*.onnx
*.torchscript
```

## 📝 許可證

YOLO 模型遵循 AGPL-3.0 許可證。
商業使用請參考：https://ultralytics.com/license
