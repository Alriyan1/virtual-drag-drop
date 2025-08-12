# Virtual Drag & Drop

An interactive computer vision application that allows you to drag and drop virtual objects using hand gestures captured through your webcam. Built with MediaPipe and OpenCV, this project demonstrates real-time hand tracking and gesture recognition for intuitive virtual object manipulation.

## 🚀 Features

- **Real-time Hand Tracking**: Uses MediaPipe for accurate hand landmark detection
- **Gesture Recognition**: Detects pinch gestures (thumb and index finger) for object selection
- **Virtual Object Manipulation**: Drag multiple rectangular objects around the screen
- **Visual Feedback**: Real-time visual indicators for hand position and object boundaries
- **Cross-platform**: Works on Windows, macOS, and Linux
- **High Performance**: Optimized for real-time processing with 30 FPS target

## 📋 Prerequisites

- Python 3.7+
- Webcam (built-in or external)
- 4GB+ RAM recommended
- OpenGL-compatible graphics card (optional, for better performance)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd virtual_drag&drop
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install mediapipe opencv-python numpy
   ```

## 🚀 Usage

### Running the Application

1. **Start the virtual drag & drop app:**
   ```bash
   python main.py
   ```

2. **Position your hand** in front of the webcam
3. **Make a pinch gesture** by bringing your thumb and index finger close together
4. **Drag objects** by moving your hand while maintaining the pinch gesture
5. **Release objects** by opening your hand (increasing distance between fingers)
6. **Press ESC** to exit the application

### Gesture Controls

- **Pinch Gesture**: Bring thumb (landmark 4) and index finger (landmark 8) close together (< 45 pixels)
- **Drag**: Move your hand while maintaining the pinch gesture
- **Release**: Open your hand to drop objects
- **Exit**: Press ESC key

## 🏗️ Project Structure

```
virtual_drag&drop/
├── main.py                    # Main application file
├── handtrackmodule.py         # Hand tracking and detection module
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## 🔧 Technical Details

### Core Components

#### Hand Detection (`handtrackmodule.py`)
- **MediaPipe Integration**: Uses Google's MediaPipe for hand landmark detection
- **Landmark Tracking**: Tracks 21 hand landmarks in real-time
- **Gesture Recognition**: Calculates distances between specific landmarks
- **Visual Feedback**: Draws hand skeleton and bounding boxes

#### Main Application (`main.py`)
- **Video Capture**: Real-time webcam feed processing
- **Object Management**: Creates and manages draggable virtual objects
- **Collision Detection**: Detects when hand cursor overlaps with objects
- **Rendering**: Combines camera feed with virtual objects using alpha blending

### Hand Landmarks Used

- **Landmark 4**: Thumb tip (for pinch gesture detection)
- **Landmark 8**: Index finger tip (for pinch gesture detection)
- **Landmark 12**: Middle finger tip (alternative pinch detection)

### Object System

- **DragRect Class**: Manages individual draggable objects
- **Position Tracking**: Updates object positions based on hand cursor
- **Collision Detection**: Checks if hand cursor is within object boundaries
- **Visual Markers**: Corner markers and filled rectangles for clear object representation

## 🎮 How It Works

1. **Initialization**: Creates 5 draggable rectangles positioned horizontally
2. **Hand Detection**: Continuously processes webcam frames for hand landmarks
3. **Gesture Recognition**: Monitors distance between thumb and index finger
4. **Object Selection**: When pinch gesture is detected, hand becomes cursor
5. **Drag Operation**: Objects follow hand movement while gesture is maintained
6. **Object Release**: Objects stay in place when pinch gesture is released

## 🌟 Advanced Features

### Real-time Processing
- **30 FPS Target**: Optimized for smooth interaction
- **Efficient Rendering**: Uses NumPy for fast array operations
- **Memory Management**: Minimal memory footprint for continuous operation

### Visual Enhancements
- **Alpha Blending**: Smooth integration of virtual objects with camera feed
- **Corner Markers**: Green cross markers at object corners for precise positioning
- **Hand Visualization**: Real-time hand skeleton and landmark display
- **Bounding Boxes**: Visual feedback for hand detection area

### Gesture Customization
- **Configurable Thresholds**: Adjustable distance thresholds for gesture recognition
- **Multiple Hand Support**: Can be extended to support multiple hands
- **Custom Gestures**: Framework for implementing additional gesture types

## 🐛 Troubleshooting

### Common Issues

1. **No hand detection**
   - Ensure good lighting conditions
   - Keep hand clearly visible in camera frame
   - Check webcam permissions and connections

2. **Poor tracking accuracy**
   - Maintain consistent lighting
   - Keep hand at appropriate distance from camera
   - Avoid rapid hand movements

3. **Performance issues**
   - Close other applications using the webcam
   - Reduce camera resolution if needed
   - Check system resources

### Performance Tips

- **Lighting**: Ensure even, consistent lighting for better hand detection
- **Camera Position**: Position webcam at eye level for optimal tracking
- **Hand Position**: Keep hand within camera frame and at appropriate distance
- **Background**: Use plain backgrounds for better contrast

## 🔮 Future Enhancements

- [ ] **Multi-hand Support**: Simultaneous tracking of multiple hands
- [ ] **3D Object Manipulation**: Add depth perception for 3D objects
- [ ] **Gesture Library**: Expand gesture recognition capabilities
- [ ] **Object Physics**: Add realistic physics and collision detection
- [ ] **Touchscreen Integration**: Support for touch devices
- [ ] **Custom Object Types**: Support for images, 3D models, and animations
- [ ] **Gesture Recording**: Save and replay custom gesture sequences
- [ ] **API Integration**: Connect with other applications and services

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test changes with different hand positions and lighting conditions
- Update documentation for new features

## 🙏 Acknowledgments

- **Google MediaPipe**: Hand tracking and landmark detection
- **OpenCV**: Computer vision and image processing
- **NumPy**: Numerical computing and array operations
- **Computer Vision Community**: Inspiration and technical guidance

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the code comments for implementation details

## 🔗 Related Projects

- **Virtual Mouse**: Hand gesture-based mouse control
- **Volume Control**: Hand gesture-based system volume management
- **Hand Distance Measurement**: Precise hand gesture measurement tools

---

**Happy virtual dragging! 🖐️✨**

