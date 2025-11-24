# 🤝 貢獻指南

感謝您考慮為台北市交通監控系統做出貢獻！

## 📋 目錄

- [行為準則](#行為準則)
- [如何貢獻](#如何貢獻)
- [開發流程](#開發流程)
- [代碼規範](#代碼規範)
- [提交規範](#提交規範)
- [測試要求](#測試要求)

## 🌟 行為準則

### 我們的承諾

- 尊重所有貢獻者
- 接受建設性的批評
- 專注於對社群最有利的事情
- 展現同理心

### 不可接受的行為

- 使用性別化語言或圖像
- 侮辱性評論或人身攻擊
- 公開或私下騷擾
- 未經許可發布他人私人信息

## 💡 如何貢獻

### 報告 Bug

在提交 Bug 之前：
1. 確認 Bug 在最新版本中仍存在
2. 查看 [Issues](https://github.com/yourusername/traffic-monitor-system/issues) 確認未被報告

提交 Bug 時請包含：
```markdown
**環境：**
- OS: [e.g., Windows 10]
- Python: [e.g., 3.9.7]
- 版本: [e.g., v1.0.0]

**重現步驟：**
1. 做了什麼
2. 預期結果
3. 實際結果

**截圖：**
（如適用）

**額外信息：**
任何其他相關信息
```

### 建議新功能

提交功能建議時請說明：
1. 功能的詳細描述
2. 為什麼需要這個功能
3. 如何使用這個功能
4. 可能的實現方式

### 提交代碼

1. **Fork 專案**
   ```bash
   git clone https://github.com/yourusername/traffic-monitor-system.git
   ```

2. **創建分支**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **編寫代碼**
   - 遵循代碼規範
   - 添加必要的註釋
   - 編寫測試

4. **提交更改**
   ```bash
   git commit -m "✨ Add amazing feature"
   ```

5. **推送分支**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **開啟 Pull Request**

## 🔧 開發流程

### 設置開發環境

1. **克隆倉庫**
   ```bash
   git clone https://github.com/yourusername/traffic-monitor-system.git
   cd traffic-monitor-system
   ```

2. **創建虛擬環境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **安裝依賴**
   ```bash
   pip install -r backend/requirements.txt
   pip install -r requirements-dev.txt  # 開發依賴
   ```

4. **安裝 pre-commit hooks**
   ```bash
   pre-commit install
   ```

### 分支策略

- `main` - 穩定版本
- `develop` - 開發版本
- `feature/*` - 新功能
- `bugfix/*` - Bug 修復
- `hotfix/*` - 緊急修復

## 📝 代碼規範

### Python 代碼（PEP 8）

**使用 Black 格式化：**
```bash
black backend/
```

**使用 isort 排序 imports：**
```bash
isort backend/
```

**使用 flake8 檢查：**
```bash
flake8 backend/ --max-line-length=100
```

**範例：**
```python
"""
模組說明
"""

import os
from typing import Dict, List

from ultralytics import YOLO
import cv2


class VehicleDetector:
    """車輛檢測器類"""

    def __init__(self, stream_url: str, model_path: str = 'yolov8n.pt'):
        """
        初始化檢測器

        Args:
            stream_url: M3U8 視頻流 URL
            model_path: YOLO 模型路徑
        """
        self.stream_url = stream_url
        self.model = YOLO(model_path)

    def process_frame(self) -> Dict:
        """處理單幀"""
        pass
```

### JavaScript 代碼

**使用 ESLint：**
```bash
eslint frontend/js/
```

**使用 Prettier 格式化：**
```bash
prettier --write "frontend/**/*.js"
```

**範例：**
```javascript
// Socket.IO 連接
const socket = io('http://localhost:5000');

/**
 * 更新統計顯示
 * @param {Object} stats - 統計數據
 */
function updateStatsDisplay(stats) {
    const { southbound, northbound, total, fps } = stats;
    // 更新邏輯...
}
```

### HTML/CSS

- 使用 2 空格縮排
- class 名稱使用 kebab-case
- 保持語義化的 HTML 結構

## 📌 提交規範

使用 [Conventional Commits](https://www.conventionalcommits.org/)：

```
<類型>: <簡短描述>

<詳細描述>

<footer>
```

### 類型

- `✨ feat:` 新功能
- `🐛 fix:` Bug 修復
- `📝 docs:` 文檔更新
- `💄 style:` 代碼格式（不影響功能）
- `♻️ refactor:` 重構
- `⚡ perf:` 性能優化
- `✅ test:` 測試相關
- `🔧 chore:` 構建/工具相關

### 範例

```bash
git commit -m "✨ feat: 添加車輛速度檢測功能"
git commit -m "🐛 fix: 修復北上車輛統計錯誤"
git commit -m "📝 docs: 更新 README 安裝說明"
```

## ✅ 測試要求

### 單元測試

使用 pytest：

```python
# tests/test_detector.py
import pytest
from backend.detector import VehicleDetector


def test_detector_initialization():
    detector = VehicleDetector('test_url')
    assert detector.stream_url == 'test_url'


def test_distance_calculation():
    detector = VehicleDetector('test_url')
    distance = detector.distance((0, 0), (3, 4))
    assert distance == 5.0
```

運行測試：
```bash
pytest tests/
```

### 代碼覆蓋率

```bash
pytest --cov=backend tests/
```

目標：>80% 覆蓋率

### 集成測試

測試完整流程：
```python
def test_full_detection_flow():
    # 初始化檢測器
    # 處理幀
    # 驗證結果
    pass
```

## 📦 Pull Request 清單

在提交 PR 之前，請確認：

- [ ] 代碼遵循專案風格指南
- [ ] 已添加必要的註釋
- [ ] 文檔已更新
- [ ] 所有測試通過
- [ ] 沒有新的警告
- [ ] PR 標題清晰描述更改
- [ ] 已連結相關 Issue

## 🎯 優先開發任務

### 高優先級

- [ ] 添加車輛速度檢測
- [ ] 支援更多視頻格式
- [ ] 添加資料庫存儲
- [ ] 多攝像頭支援

### 中優先級

- [ ] 導出統計報表（CSV/Excel）
- [ ] 車牌識別功能
- [ ] 異常事件檢測
- [ ] 移動端適配

### 低優先級

- [ ] 暗色主題選項
- [ ] 多語言支援
- [ ] 歷史數據回放
- [ ] AI 訓練自定義模型

## 🏆 貢獻者

感謝所有貢獻者！

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## 📬 聯繫方式

如有問題，請：
- 提交 [Issue](https://github.com/yourusername/traffic-monitor-system/issues)
- 發送郵件至：your.email@example.com
- 加入 Discord 社群：[連結]

## 📚 參考資源

- [Python 風格指南](https://www.python.org/dev/peps/pep-0008/)
- [JavaScript 風格指南](https://github.com/airbnb/javascript)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [開源貢獻指南](https://opensource.guide/how-to-contribute/)

---

再次感謝您的貢獻！🙏
