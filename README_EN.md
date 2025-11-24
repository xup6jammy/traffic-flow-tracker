# 🚦 Taipei Traffic Monitoring System - Vehicle Direction Detection

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![YOLO](https://img.shields.io/badge/YOLO-v8n-green.svg)](https://github.com/ultralytics/ultralytics)

### 語言 / Language

**[繁體中文](README.md)** | **[English](README_EN.md)**

</div>

---

A real-time traffic monitoring system based on YOLOv8 that automatically detects and counts southbound and northbound vehicles. Supports both GUI desktop and Web versions.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Quick Start](#quick-start)
- [YOLO Model Selection](#yolo-model-selection)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Project Overview

This system is designed for traffic management and law enforcement personnel, providing the following core features:

- **Real-time Vehicle Detection**: Efficient vehicle recognition using YOLOv8 model
- **Direction Statistics**: Automatic detection of vehicle direction (southbound/northbound)
- **Vehicle Snapshots**: Automatic capture of vehicle images crossing reference line
- **Traditional Chinese Support**: Complete Traditional Chinese interface
- **Dual Version Support**: Both GUI desktop and Web versions available

### Use Cases

- Traffic flow monitoring
- Violation vehicle tracking
- Traffic data analysis
- Smart city construction

## ✨ Features

### Core Functionality

✅ **Intelligent Vehicle Detection**
- Support for car and motorcycle recognition
- High accuracy real-time detection
- Adjustable confidence threshold

✅ **Direction Detection System**
- Automatic southbound/northbound direction identification
- Reference line-based crossing detection
- Duplicate counting prevention

✅ **Visualization Interface**
- Modern white theme design
- Extra-large statistical numbers display (48pt)
- Colorful card-based layout
- Real-time FPS monitoring

✅ **Vehicle Recording**
- Automatic screenshot saving
- Display vehicle type and timestamp
- Categorized display (northbound/southbound)
- Save up to 10 records

## 🏗️ System Architecture

```
traffic-monitor-system/
├── frontend/               # Web Frontend
│   ├── index.html         # Main page
│   ├── css/
│   │   └── style.css      # Stylesheets
│   └── js/
│       └── app.js         # Frontend logic
├── backend/               # Python Backend
│   ├── app.py            # Flask application
│   ├── detector.py       # YOLO detector
│   └── requirements.txt  # Python dependencies
├── models/               # YOLO model files
│   └── README.md         # Model documentation
├── docs/                 # Documentation
│   └── MODEL_COMPARISON.md
├── traffic_stream_detection_gui.py  # GUI desktop version
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) CUDA-capable GPU

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/traffic-monitor-system.git
cd traffic-monitor-system
```

#### 2. Create Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

#### 4. Download YOLO Model

```bash
# Models will be automatically downloaded on first run
# Or manually download to models/ directory
```

### Run the Application

#### GUI Desktop Version

```bash
python traffic_stream_detection_gui.py
```

#### Web Version

```bash
# Start backend service
cd backend
python app.py

# Access in browser
# http://localhost:5000
```

## 📊 YOLO Model Selection

This system supports multiple YOLO models. Here's a detailed comparison:

| Model | Size | Speed (FPS) | mAP | Accuracy | Memory | Recommended For |
|------|------|-----------|-----|--------|--------|---------|
| **YOLOv8n** ⭐ | 6.3 MB | 45-60 | 37.3% | ⭐⭐⭐ | Low | Real-time monitoring, CPU |
| YOLOv8s | 22 MB | 35-45 | 44.9% | ⭐⭐⭐⭐ | Medium | Balanced performance |
| YOLOv8m | 52 MB | 25-35 | 50.2% | ⭐⭐⭐⭐⭐ | High | High accuracy needs |
| YOLOv11n | 5.5 MB | 50-65 | 39.5% | ⭐⭐⭐⭐ | Low | Latest optimization |

### Why YOLOv8n?

✅ **Speed Advantage**
- Achieves 45-60 FPS even on CPU
- Low latency, suitable for real-time applications

✅ **Resource Friendly**
- Model size only 6.3 MB, fast loading
- Low memory usage, suitable for long-term operation

✅ **Sufficient Accuracy**
- Accuracy meets requirements for car and motorcycle detection
- mAP 37.3% performs well on small object detection

✅ **Mature Ecosystem**
- Official Ultralytics support
- Rich community resources

### Switch Models

Modify the model path in configuration file:

```python
# In traffic_stream_detection_gui.py
MODEL_PATH = "yolov8n.pt"  # Change to other models like "yolov8s.pt"
```

## 📖 Usage

### GUI Desktop Version

1. **Launch Application**
   ```bash
   python traffic_stream_detection_gui.py
   ```

2. **Interface Description**
   - **Top Cards**: Display southbound, northbound, total vehicle count and FPS
   - **Left Window**: Live monitoring view with red reference line across center
   - **Right Panel**: Recent vehicle snapshots (top: northbound, bottom: southbound)

3. **Key Features**
   - System automatically connects to Taipei traffic camera
   - Automatic counting and screenshot when vehicles cross red line
   - Click close button to exit

### Web Version

1. **Access Webpage**
   - Open browser and visit `http://localhost:5000`

2. **Features**
   - View real-time monitoring
   - Check statistics
   - Browse vehicle records

## 🛠️ Tech Stack

### Desktop Version

- **Python 3.8+**
- **OpenCV** - Image processing
- **Ultralytics YOLO** - Object detection
- **Tkinter** - GUI framework
- **Pillow** - Image processing and Chinese font support

### Web Version

#### Frontend
- **HTML5** - Structure
- **CSS3** - Styling (modern white theme)
- **JavaScript (ES6+)** - Interactive logic
- **WebSocket** - Real-time communication

#### Backend
- **Flask** - Web framework
- **Flask-SocketIO** - WebSocket support
- **OpenCV** - Image processing
- **Ultralytics YOLO** - Object detection

## 📁 Project Files

### Core Files

- `traffic_stream_detection_gui.py` - GUI desktop version main program
- `backend/app.py` - Flask backend service
- `backend/detector.py` - YOLO detector wrapper
- `frontend/index.html` - Web frontend page

### Configuration Files

- `backend/requirements.txt` - Python dependencies
- `.gitignore` - Git ignore rules

## 🤝 Contributing

Contributions welcome! Please follow these steps:

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Development Guidelines

- Follow PEP 8 code style
- Add appropriate comments
- Update related documentation

## 🐛 Issue Reporting

If you encounter issues, please submit on [Issues](https://github.com/yourusername/traffic-monitor-system/issues) page.

Please include when submitting:
- System environment (OS, Python version)
- Error messages
- Steps to reproduce

## 📝 Changelog

### v1.0.0 (2024-01-XX)
- ✨ Initial release
- ✅ GUI desktop version
- ✅ Web version
- ✅ Traditional Chinese support
- ✅ Vehicle direction detection
- ✅ Automatic screenshot feature

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details

## 👥 Authors

- **Your Name** - *Initial work*

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) - YOLO models
- [Taipei City Government](https://gov.taipei/) - Traffic camera data source
- All contributors

## 📞 Contact

- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)

---

⭐ If this project helps you, please give it a star!
