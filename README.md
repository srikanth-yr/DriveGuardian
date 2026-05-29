# 🚗 AI Driver Safety and Drowsiness Monitoring System

A comprehensive real-time intelligent automotive safety system that monitors drivers using computer vision and AI to detect drowsiness, fatigue, and other safety-critical behaviors.

## 🎯 Project Overview

This system uses advanced computer vision techniques to:
- **Detect Drowsiness**: Monitor eye closure duration and blink patterns using Eye Aspect Ratio (EAR)
- **Monitor Yawning**: Track mouth opening using Mouth Aspect Ratio (MAR)
- **Track Head Position**: Detect abnormal head tilt and nodding
- **Identify Phone Usage**: Use YOLOv8 for real-time phone detection that starts as soon as the camera feed is live
- **Analyze Emotions**: Detect stress and emotional states
- **Calculate Fatigue Score**: Dynamic scoring from 0-100
- **Trigger Alarms**: Audio alerts, voice warnings, and emergency notifications
- **Dashboard Monitoring**: Web-based real-time monitoring dashboard

## ✨ Key Features

### 1. **Real-time Webcam Monitoring**
- Continuous video capture from laptop webcam
- 30 FPS processing (configurable)
- Live video display with overlay metrics

### 2. **Face & Facial Landmarks Detection**
- Dlib-based face detection
- 68-point facial landmark extraction
- Head pose estimation

### 3. **Eye Blink & Drowsiness Detection**
- Eye Aspect Ratio (EAR) calculation
- Blink rate monitoring
- Drowsiness alert triggering
- Alertness percentage display

### 4. **Yawning Detection**
- Mouth Aspect Ratio (MAR) calculation
- Repeated yawn detection
- Fatigue score adjustment

### 5. **Head Tilt Tracking**
- Head pose angles (Yaw, Pitch, Roll)
- Abnormal tilt detection
- Looking away detection
- Head nodding detection

### 6. **Fatigue Score System**
- Dynamic scoring algorithm (0-100)
- Multiple factor integration
- Fatigue levels: ALERT, TIRED, DROWSY, CRITICAL
- Real-time threshold monitoring

### 7. **Alarm & Voice System**
- System beep alerts
- pyttsx3 voice warnings
- Customizable voice messages
- Alert cooldown management

### 8. **Mobile Phone Detection**
- YOLOv8 object detection
- Detects as soon as the camera stream starts, even before face landmarks are acquired
- Real-time phone usage alerts
- Usage pattern analysis
- Continuous usage detection

### 9. **Emotion & Stress Detection**
- Facial expression analysis
- Stress level classification
- Emotion timeline tracking
- Multiple emotion detection

### 10. **Emergency Alert System**
- Critical fatigue threshold monitoring
- Driver unresponsiveness detection
- Emergency notifications
- Placeholder for SMS/GPS integration

### 11. **Web Dashboard**
- Flask-based real-time dashboard
- Live camera feed streaming
- Interactive metrics display
- Alert notifications
- Data export functionality
- Session statistics

### 12. **Comprehensive Logging**
- CSV-based logging
- Fatigue logs with timestamps
- Alert history
- Emotion tracking
- Phone usage records

## 📋 System Requirements

### Hardware
- Laptop with webcam (minimum 720p)
- 4GB RAM minimum (8GB recommended)
- Multi-core processor
- GPU (optional, for faster processing)

### Software
- Python 3.8+
- Windows 10+ / macOS / Linux
- Webcam access permissions

## 🚀 Installation & Setup

### 1. Clone or Download Project
```bash
cd AI_Driver_Safety_System
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- OpenCV for image processing
- Dlib for face detection
- YOLO for phone detection
- Flask for dashboard
- TensorFlow/Keras for emotion detection
- pyttsx3 for voice alerts
- And more...

### 3. Download Required Models
The system needs both the face landmark model and the YOLO weights for phone detection:

```bash
# Create models directory
mkdir models

# Download shape_predictor_68_face_landmarks.dat
# From: https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2
# Extract to models/ directory as:
# models/shape_predictor_68_face_landmarks.dat

# Download YOLOv8 nano weights
# From: https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8n.pt
# Save to:
# models/yolov8n.pt
```

### 4. Create Sound Files (Optional)
For alarm sounds, place audio files in `sounds/`:
- `alarm.wav` - Drowsiness alarm
- `warning.wav` - Warning sound

### 5. Start the System
```bash
python desktop_app.py
```

## 📊 Configuration

Edit `config.py` to customize:

### Eye Detection Thresholds
```python
EYE_ASPECT_RATIO_THRESHOLD = 0.2
EYE_ASPECT_RATIO_FRAMES = 30
BLINK_THRESHOLD_FRAMES = 5
```

### Yawning Detection
```python
MOUTH_ASPECT_RATIO_THRESHOLD = 0.6
YAWN_DURATION_FRAMES = 15
```

### Fatigue Scoring
```python
DROWSINESS_INCREMENT = 5
YAWNING_INCREMENT = 3
PHONE_DETECTION_INCREMENT = 8
```

### Emergency Settings
```python
EMERGENCY_THRESHOLD = 80
EMERGENCY_UNRESPONSIVE_DURATION = 10
```

### Dashboard Configuration
```python
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True
```

## 🎮 Usage

### Running the System
```bash
python desktop_app.py
```

For the classic OpenCV window-only mode, you can still run:
```bash
python main.py
```

### Keyboard Controls
- **Q** - Quit the application
- **S** - Take screenshot
- **P** - Pause/resume video
- **ESC** - Exit

### Web Dashboard
Access the dashboard at: `http://localhost:5000`

Features:
- Real-time metrics display
- Live camera feed
- Fatigue score chart
- Emotion distribution
- Alert notifications
- Data export
- Recording toggle

## 📁 Project Structure

```
AI_Driver_Safety_System/
├── main.py                          # Main execution file
├── config.py                        # Configuration settings
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
├── modules/                         # Core modules
│   ├── camera.py                   # Camera capture
│   ├── face_detection.py           # Face & landmark detection
│   ├── eye_detection.py            # Eye blink & drowsiness
│   ├── yawn_detection.py           # Yawn detection
│   ├── head_tracking.py            # Head pose estimation
│   ├── fatigue_score.py            # Fatigue calculation
│   ├── alarm_system.py             # Alarm & visual alerts
│   ├── voice_assistant.py          # Voice warnings
│   ├── phone_detection.py          # Phone detection (YOLO)
│   ├── emotion_detection.py        # Emotion analysis
│   ├── emergency_alert.py          # Emergency system
│   └── utils.py                    # Utility functions
│
├── dashboard/                       # Flask dashboard
│   ├── app.py                      # Flask application
│   └── routes.py                   # API routes
│
├── templates/                       # HTML templates
│   ├── index.html                  # Dashboard page
│   └── dashboard.html              # Full dashboard
│
├── static/                          # Static files
│   ├── css/
│   │   └── style.css               # Dashboard styles
│   ├── js/
│   │   └── dashboard.js            # Dashboard scripts
│   └── images/
│
├── models/                          # Pre-trained models
│   ├── shape_predictor_68_face_landmarks.dat
│   ├── yolov8n.pt
│   └── emotion_model.h5
│
├── sounds/                          # Audio files
│   ├── alarm.wav
│   └── warning.wav
│
├── data/                            # Data storage
│   ├── logs/                       # CSV logs
│   ├── screenshots/
│   └── recordings/
│
└── outputs/                         # Output files
    ├── screenshots/
    ├── reports/
    └── graphs/
```

## 🔍 Detailed Feature Documentation

### Eye Aspect Ratio (EAR)
- Formula: (||p2 - p6|| + ||p3 - p5||) / (2 * ||p1 - p4||)
- Threshold: < 0.2 indicates closed eyes
- Used for: Blink detection, drowsiness monitoring

### Mouth Aspect Ratio (MAR)
- Formula: (||p2 - p7|| + ||p3 - p6|| + ||p4 - p5||) / (3 * ||p1 - p5||)
- Threshold: > 0.6 indicates open mouth
- Used for: Yawn detection

### Fatigue Score Components
1. **Drowsiness** (+5 points) - Prolonged eye closure
2. **Yawning** (+3 points) - Detected yawns
3. **Head Tilt** (+2 points) - Abnormal head angles
4. **Phone Usage** (+8 points) - Phone detected
5. **Stress** (+4 points) - High stress emotions
6. **Eye Closure Duration** - Extended closure penalty
7. **Blink Rate Anomaly** - Abnormal blink patterns
8. **Decay** (-1 point/sec) - Score recovery

### Fatigue Levels
- **ALERT** (0-25): Normal, safe driving
- **TIRED** (25-50): Mild fatigue detected
- **DROWSY** (50-75): Significant drowsiness
- **CRITICAL** (75-100): Severe fatigue, emergency

## 📈 Dashboard Features

### Metrics Display
- Fatigue Score (0-100)
- Alertness Percentage
- Eye Aspect Ratio
- Mouth Aspect Ratio
- Blink Rate (blinks/minute)
- Head Pose Angles
- Emotion Status
- Stress Level

### Real-time Charts
- Fatigue Score Trend (line chart)
- Emotion Distribution (pie chart)

### Controls
- Start/Stop Recording
- Take Screenshots
- Export Reports (JSON)
- Pause/Resume Monitoring

### Alerts Section
- Active alert notifications
- Alert severity indicators
- Timestamp tracking

## 🚨 Alert System

### Alert Types
1. **Drowsiness Alert**
   - Triggered: Eyes closed > 1 second
   - Response: Alarm + "Please stay alert" voice

2. **Yawning Alert**
   - Triggered: Yawn detected
   - Response: Voice notification

3. **Phone Alert**
   - Triggered: Phone detected in hand
   - Response: Warning sound + voice alert

4. **Stress Alert**
   - Triggered: High stress emotions
   - Response: Calming voice message

5. **Emergency Alert**
   - Triggered: Fatigue score > 80 for 3+ seconds
   - Response: Continuous alarm + critical voice alert

### Alert Cooldown
- Default: 5 seconds between same alert type
- Prevents alert spam
- Configurable per alert type

## 📊 Logging & Data Export

### Log Files (CSV Format)
- **Fatigue Log**: `fatigue_log_YYYYMMDD_HHMMSS.csv`
  - Fatigue score, drowsy status, yawning, etc.
  
- **Alert Log**: `alert_log_YYYYMMDD_HHMMSS.csv`
  - Alert types, timestamps, severity
  
- **Emotion Log**: `emotion_log_YYYYMMDD_HHMMSS.csv`
  - Detected emotions, stress levels
  
- **Phone Log**: `phone_log_YYYYMMDD_HHMMSS.csv`
  - Phone detection events, confidence scores

### Export Options
- JSON report export
- CSV data download
- Screenshot capture
- Video recording (optional)

## 🔮 Future Enhancements

### Planned Features
1. **SMS Integration**: Send emergency SMS to contacts
2. **GPS Integration**: Track location for emergency response
3. **Cloud Storage**: Store data in cloud (Azure/AWS)
4. **Mobile App**: Companion mobile app for alerts
5. **ML Model Improvements**: Custom trained models
6. **Multi-Camera Support**: Monitor multiple drivers
7. **Advanced Analytics**: Prediction models
8. **Integration with Vehicle**: OBD-II interface
9. **Driver Profile**: Personalized thresholds
10. **Real-time Notifications**: Push notifications

## 🛠️ Troubleshooting

### Camera Not Detected
```python
# Try different camera ID
camera = CameraHandler(camera_id=1)  # Try 1, 2, 3...
```

### Face Not Detected
- Ensure good lighting
- Face should be clearly visible
- Adjust minimum face size in config

### Model Download Issues
- Download models manually from provided links
- Place in `models/` directory
- Check file names match config

### Phone Detected Late or Not At Startup
- Phone detection now runs even before face detection locks on
- Confirm `models/yolov8n.pt` exists locally
- Lower `PHONE_CONFIDENCE_THRESHOLD` slightly if your camera is dim or noisy
- Keep the phone clearly visible to the camera

### Slow Performance
- Reduce frame resolution
- Increase FRAME_SKIP
- Disable GPU features if causing issues
- Use lighter model (YOLOv8n instead of larger)

### Voice Not Working
```python
# Check audio device
import pyttsx3
engine = pyttsx3.init()
engine.say("test")
engine.runAndWait()
```

## 📚 References & Resources

### Computer Vision
- **OpenCV**: https://opencv.org/
- **Dlib**: http://dlib.net/
- **MediaPipe**: https://mediapipe.dev/

### Deep Learning
- **YOLO**: https://github.com/ultralytics/yolov5
- **DeepFace**: https://github.com/serengp/deepface
- **TensorFlow**: https://www.tensorflow.org/

### Academic Papers
- Eye tracking and blink detection
- Facial expression recognition
- Driver drowsiness detection
- Head pose estimation

## 📝 License

This project is provided as-is for educational and research purposes.

## 👨‍💻 Author

AI Driver Safety Monitoring System
Version 1.0.0

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Submit pull request

## 📧 Contact & Support

For issues, feature requests, or questions:
- Create an issue on GitHub
- Check existing documentation
- Review troubleshooting section

## ⚠️ Disclaimer

This system is designed as a driver assistance tool and should not be relied upon as the sole safety mechanism. Always:
- Keep eyes on the road
- Follow traffic laws
- Ensure proper vehicle maintenance
- Take regular breaks during long drives

**Your safety is your responsibility!** This system is meant to help, not replace, proper driving practices.

---

**Last Updated**: 2024
**Status**: Active Development
