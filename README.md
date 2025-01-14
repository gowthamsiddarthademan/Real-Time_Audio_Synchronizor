# Real-Time_Audio_Synchronizor
This project enables real-time synchronization of audio playback across multiple devices connected to the same server. Users can upload audio files, which are then streamed and synchronized seamlessly on all connected devices. The system handles network latency dynamically to ensure near-perfect sync.
Here's the information you can use for your GitHub repository:

---

### **Key Features**:
- Real-time audio playback synchronization.
- Dynamic file upload and broadcasting to all devices.
- Latency compensation for smooth playback across devices.
- Intuitive user interface for easy interaction.
- Uses **Flask** for the backend and **Socket.IO** for real-time communication.

---

### **Technologies Used**:
- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Real-time Communication**: Socket.IO
- **Deployment**: Flask development server (can be adapted for production)

---

### **How It Works**:
1. **Upload Audio File**: A user uploads an audio file using the upload form.
2. **Broadcast the File**: The uploaded file is shared with all connected devices.
3. **Real-Time Playback Synchronization**: When one device plays, pauses, or seeks the audio, all devices sync their playback state in real time.
4. **Latency Adjustment**: The system calculates network latency and adjusts playback to minimize delays.

---

### **Getting Started**:

#### 1. Install Dependencies:
```bash
pip install flask flask-socketio
```

#### 2. Run the Application:
```bash
python app.py
```

#### 3. Access the Application:
Open your web browser and go to `http://127.0.0.1:5000`.

---

### **Usage Instructions**:
1. Upload an audio file using the file upload form.
2. The uploaded file will be playable across all connected devices.
3. Actions like play, pause, seek, and end are synchronized in real time.

---
