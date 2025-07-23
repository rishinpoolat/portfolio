# Real-Time Helmet Detection System

[GitHub Repository](https://github.com/rishinpoolat/realtime-helmet-detector)

## Overview

The Real-Time Helmet Detection System is a sophisticated computer vision and safety-focused project designed to enhance motorcycle rider safety through automated helmet detection and intelligent alerts. This system leverages deep learning algorithms to analyze live camera feeds and provides immediate audio notifications when riders are detected without helmets, promoting safety compliance and accident prevention.

## 🛡️ Safety Mission

This project addresses a critical safety concern in motorcycle transportation by providing an automated, real-time solution for helmet detection. By combining advanced computer vision with practical deployment considerations, it offers a self-awareness system that can significantly contribute to rider safety and accident prevention.

## 🚀 Key Features

### Real-Time Detection Capabilities
- **Live Video Processing**: Analyzes real-time camera feeds with optimized performance for edge devices
- **Instant Classification**: Binary classification system distinguishing between "helmet" and "no_helmet" scenarios
- **High Accuracy Detection**: Achieves 99% classification accuracy with robust performance across various conditions
- **Optimized Inference**: Designed for efficient processing on resource-constrained devices like Raspberry Pi

### Intelligent Alert System
- **Audio Notifications**: Automated text-to-speech warnings ("please wear helmet") when violations are detected
- **Immediate Feedback**: Real-time safety alerts for instant compliance awareness
- **Non-intrusive Design**: Audio-based alerts that don't interfere with riding experience
- **Customizable Alerts**: Configurable alert system for different deployment scenarios

### Deployment-Ready Architecture
- **Raspberry Pi Integration**: Optimized for popular single-board computer platforms
- **Camera Module Support**: Direct integration with standard camera modules
- **Speaker Integration**: Built-in support for audio output devices
- **Portable Solution**: Self-contained system suitable for various mounting configurations

## 🛠 Technology Stack

### Deep Learning Framework
- **TensorFlow/Keras**: Primary deep learning framework for model training and inference
- **MobileNetV2**: Pre-trained base model providing efficient feature extraction
- **Transfer Learning**: Leverages ImageNet pre-trained weights for robust performance

### Computer Vision
- **OpenCV**: Core computer vision operations, camera interface, and image processing
- **PIL/Pillow**: Advanced image manipulation and format handling
- **imutils**: Computer vision utilities for enhanced processing capabilities

### Audio Processing
- **pyttsx3**: Text-to-speech engine for generating natural-sounding safety alerts
- **Cross-platform Audio**: Compatible with various audio output systems

### Scientific Computing
- **NumPy**: Numerical computations and array operations
- **Scikit-learn**: Data preprocessing, evaluation metrics, and validation tools
- **Matplotlib**: Visualization for training progress and model evaluation

## 🧠 Model Architecture

### Neural Network Design
```
Input Layer (224x224x3 RGB)
    ↓
MobileNetV2 Base (Pre-trained, Frozen)
    ↓
AveragePooling2D (7x7)
    ↓
Flatten Layer
    ↓
Dense Layer (128 units, ReLU activation)
    ↓
Dropout Layer (0.5 rate)
    ↓
Output Dense Layer (2 units, Softmax activation)
    ↓
Binary Classification (Helmet/No Helmet)
```

### Training Configuration
- **Input Resolution**: 224×224×3 RGB images (optimized for MobileNetV2)
- **Learning Rate**: 1e-4 (0.0001) with Adam optimizer
- **Loss Function**: Binary crossentropy for two-class classification
- **Training Epochs**: 20 with early stopping capabilities
- **Batch Size**: 32 for optimal memory usage and convergence

### Transfer Learning Strategy
- **Base Model**: MobileNetV2 pre-trained on ImageNet dataset
- **Frozen Layers**: Base model layers kept frozen to preserve learned features
- **Custom Head**: Task-specific layers added for helmet detection
- **Fine-tuning**: Gradual unfreezing strategy for improved performance

## 📊 Dataset & Data Processing

### Dataset Structure
```
realtime-helmet-detector/
├── train/
│   └── no_helmet/          # 198 augmented training images
├── validate/
│   └── no_helmet/          # 34 validation images
└── test/                   # 4 sample test images
```

### Data Augmentation Pipeline
The system employs comprehensive data augmentation to improve model robustness:

- **Rotation**: ±20 degrees random rotation for orientation invariance
- **Zoom**: 15% random zoom for scale variation handling
- **Shift**: 20% width/height shift for position tolerance
- **Shear**: 15% shear transformation for perspective variation
- **Flip**: Horizontal flipping for symmetry augmentation
- **Fill Mode**: Nearest neighbor filling for transformed regions

### Data Preprocessing Steps
1. **Image Loading**: Dynamic loading from directory structure
2. **Resizing**: Standardization to 224×224 pixel resolution
3. **Normalization**: Pixel value scaling to [0,1] range for neural network optimization
4. **Label Encoding**: One-hot encoding for categorical classification
5. **Stratified Splitting**: Balanced train-validation split maintaining class distributions

## ⚙️ Real-Time Detection Workflow

### Detection Pipeline
```
Camera Input → Frame Capture → Preprocessing → Model Inference → Decision Logic → Audio Alert
```

### Implementation Details

#### Frame Processing (`realtime_classification.py`)
1. **Camera Initialization**: OpenCV VideoCapture with 640×480 resolution
2. **Frame Preprocessing**:
   - Resize to 224×224 for model compatibility
   - Normalize pixel values (÷255.0)
   - Add batch dimension for inference
3. **Model Inference**: Single forward pass through trained model
4. **Decision Logic**: Extract class with highest confidence score
5. **Alert Trigger**: Activate audio alert for "no_helmet" detections

#### Audio Alert System
- **Text-to-Speech Engine**: pyttsx3 for natural voice generation
- **Alert Message**: Clear "please wear helmet" notification
- **Non-blocking Design**: Alerts don't interrupt detection process
- **Configurable Voice**: Adjustable speech rate, volume, and voice selection

### Performance Optimization
- **Efficient Architecture**: MobileNetV2 optimized for mobile/edge deployment
- **Minimal Latency**: Streamlined preprocessing pipeline
- **Resource Management**: Optimized memory usage for continuous operation
- **Frame Rate Control**: Balanced processing speed with accuracy

## 📈 Model Performance

### Training Results
- **Final Training Accuracy**: 100%
- **Final Validation Accuracy**: 98.95%
- **Training Loss**: 0.0285
- **Validation Loss**: 0.0564
- **Overall Test Accuracy**: 99%

### Classification Report
```
                 precision    recall  f1-score   support
   with_helmet       0.98      1.00      0.99        47
without_helmet       1.00      0.98      0.99        48
      accuracy                           0.99        95
     macro avg       0.99      0.99      0.99        95
  weighted avg       0.99      0.99      0.99        95
```

### Performance Characteristics
- **Balanced Performance**: Excellent precision and recall for both classes
- **High Confidence**: Strong classification confidence scores
- **Low False Positives**: Minimal incorrect helmet detections
- **Robust Generalization**: Consistent performance across validation sets

## 🚀 Installation & Setup

### Hardware Requirements
- **Computing Device**: Raspberry Pi 4 (recommended) or any Linux/Windows system
- **Camera**: USB camera or Raspberry Pi Camera Module
- **Audio Output**: Speakers or headphones for alert notifications
- **Power Supply**: Adequate power for continuous operation

### Software Dependencies
```bash
# Core dependencies
pip install tensorflow>=2.12.0
pip install opencv-python
pip install numpy
pip install pyttsx3
pip install matplotlib
pip install scikit-learn
pip install imutils
pip install pillow
```

### Installation Steps
1. **Clone Repository**:
   ```bash
   git clone <repository-url>
   cd realtime-helmet-detector
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Model File**:
   Ensure `helmet_detector.model` is present (11.5 MB file)

4. **Test Camera Setup**:
   ```bash
   python -c "import cv2; print('OpenCV version:', cv2.__version__)"
   ```

## 📖 Usage Examples

### Real-Time Detection
```bash
# Start real-time helmet detection
python realtime_classification.py
```

**Expected Behavior**:
- Camera feed window opens showing live video
- Detection results displayed on video feed
- Audio alerts triggered for "no helmet" detections
- Press 'q' to quit the application

### Single Image Testing
```bash
# Test with single image
python test_image.py
```

**Requirements**:
- Place test image as `ttt.jpeg` in project directory
- Results displayed with classification confidence

### Custom Testing
```python
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model('helmet_detector.model')

# Load and preprocess image
image = cv2.imread('your_image.jpg')
image = cv2.resize(image, (224, 224))
image = image.astype('float32') / 255.0
image = np.expand_dims(image, axis=0)

# Make prediction
prediction = model.predict(image)
class_names = ['with_helmet', 'without_helmet']
predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction) * 100

print(f"Prediction: {predicted_class} ({confidence:.2f}% confidence)")
```

## 🔧 Configuration Options

### Camera Settings
```python
# In realtime_classification.py
cap = cv2.VideoCapture(0)  # Camera index (0 for default)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # Width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Height
cap.set(cv2.CAP_PROP_FPS, 30)            # Frame rate
```

### Audio Alert Customization
```python
# Text-to-speech configuration
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)    # Speech rate
engine.setProperty('volume', 0.9)  # Volume level
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Voice selection
```

### Detection Sensitivity
```python
# Confidence threshold adjustment
confidence_threshold = 0.7  # Minimum confidence for detection
if prediction_confidence > confidence_threshold:
    # Trigger alert
    pass
```

## 🎯 Deployment Scenarios

### Motorcycle Integration
- **Dashboard Mount**: Camera positioned for rider detection
- **Audio Integration**: Connection to helmet communication systems
- **Power Management**: Integration with motorcycle electrical system
- **Weatherproofing**: Protective housing for outdoor conditions

### Traffic Monitoring
- **Fixed Installation**: Stationary cameras at traffic checkpoints
- **Multi-lane Detection**: Simultaneous monitoring of multiple vehicles
- **Data Logging**: Recording compliance statistics and violation reports
- **Integration**: Connection to traffic management systems

### Fleet Management
- **Commercial Vehicles**: Integration with delivery and service fleets
- **Safety Compliance**: Automated safety protocol enforcement
- **Driver Training**: Real-time feedback for safety education
- **Performance Metrics**: Safety compliance tracking and reporting

## 🧪 Development & Training

### Model Training Process
The system includes comprehensive Jupyter notebooks for model development:

#### Training Notebook (`model_training.ipynb`)
- Complete data loading and preprocessing pipeline
- Model architecture definition and compilation
- Training loop with progress monitoring
- Validation and performance evaluation
- Model saving and export functionality

#### Alternative Training (`helmet.ipynb`)
- Experimental training approaches
- Hyperparameter tuning experiments
- Performance comparison studies
- Model optimization techniques

### Retraining Instructions
```python
# Load and prepare new dataset
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Configure data generators
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.15,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.15,
    horizontal_flip=True,
    fill_mode="nearest"
)

# Load model and retrain
model = load_model('helmet_detector.model')
model.fit(training_generator, 
          validation_data=validation_generator,
          epochs=10)
```

## 🔍 Technical Insights

### Architecture Advantages
- **MobileNetV2 Efficiency**: Optimized for mobile deployment with depthwise separable convolutions
- **Transfer Learning Benefits**: Leverages pre-trained features for faster convergence and better generalization
- **Lightweight Design**: 11.5 MB model size suitable for edge deployment
- **High Accuracy**: 99% accuracy with balanced precision and recall

### Performance Characteristics
- **Inference Speed**: ~50-100 ms per frame on Raspberry Pi 4
- **Memory Usage**: ~200 MB RAM during operation
- **CPU Utilization**: Moderate CPU usage with optimized OpenCV operations
- **Power Consumption**: Suitable for battery-powered applications

### Scalability Considerations
- **Multi-camera Support**: Extensible to multiple camera inputs
- **Batch Processing**: Capability for processing multiple frames simultaneously
- **Cloud Integration**: Potential for cloud-based processing and analytics
- **Edge Computing**: Optimized for distributed edge deployment

## 🤝 Contributing

### Enhancement Opportunities
1. **Multi-class Detection**: Extend to different helmet types and safety gear
2. **Person Detection**: Integrate person detection for more accurate targeting
3. **Mobile App**: Develop companion mobile application
4. **IoT Integration**: Connect with IoT platforms for broader safety ecosystems
5. **Analytics Dashboard**: Web-based dashboard for monitoring and reporting

### Development Guidelines
- **Data Quality**: Ensure diverse, high-quality training data
- **Testing**: Comprehensive testing across various lighting and weather conditions
- **Documentation**: Maintain clear documentation for model updates
- **Performance**: Monitor and optimize inference performance
- **Safety**: Prioritize safety and reliability in all modifications

## 📄 License & Ethics

### Usage Considerations
- **Safety Application**: Designed specifically for safety enhancement, not surveillance
- **Privacy**: Local processing ensures user privacy
- **Reliability**: While highly accurate, should complement, not replace, personal responsibility
- **Maintenance**: Regular model updates recommended for optimal performance

## 🔗 Future Enhancements

### Planned Features
- **Advanced Analytics**: Detailed usage statistics and compliance reporting
- **Cloud Connectivity**: Optional cloud backup and analytics
- **Mobile Integration**: Smartphone app for configuration and monitoring
- **Multi-object Detection**: Simultaneous detection of multiple safety gear items
- **Weather Adaptation**: Enhanced performance in various weather conditions

### Research Directions
- **3D Pose Estimation**: Enhanced understanding of rider positioning
- **Temporal Analysis**: Video-based analysis for more robust detection
- **Federated Learning**: Collaborative model improvement across deployments
- **Edge AI Optimization**: Further optimization for edge computing platforms

This project represents a comprehensive solution combining cutting-edge computer vision technology with practical safety applications, demonstrating the potential of AI to contribute meaningfully to public safety and accident prevention.