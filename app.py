from flask import Flask, render_template, request, send_from_directory, jsonify
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        # Notify all clients about the uploaded file
        file_url = f'/uploads/{file.filename}'
        socketio.emit('new_file', {"file_url": file_url})
        return jsonify({"filename": file.filename}), 200

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Socket.IO events
@socketio.on('play')
def handle_play(data):
    emit('play', data, broadcast=True)

@socketio.on('pause')
def handle_pause():
    emit('pause', broadcast=True)

@socketio.on('seek')
def handle_seek(data):
    emit('seek', data, broadcast=True)

@socketio.on('ended')
def handle_ended():
    emit('ended', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
