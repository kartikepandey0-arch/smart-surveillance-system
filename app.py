from flask import Flask, render_template, Response, request, redirect, session, jsonify
import cv2
import sqlite3
import random
from yolo_tracker import process_frame

app = Flask(__name__)
app.secret_key = "secret123"

def init_db():
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )""")
    conn.commit()
    conn.close()

init_db()

camera = cv2.VideoCapture(0)

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        frame, people, alert, heatmap = process_frame(frame)

        app.people = people
        app.count = len(people)
        app.alert = alert
        app.heatmap = heatmap.tolist()

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    if 'user' in session:
        return redirect('/dashboard')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    u = request.form['username']
    p = request.form['password']

    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (u,p))
    user = c.fetchone()
    conn.close()

    if user:
        session['user'] = u
        return redirect('/dashboard')
    return "Login Failed"

@app.route('/register', methods=['POST'])
def register():
    u = request.form['username']
    p = request.form['password']

    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("INSERT INTO users(username,password) VALUES (?,?)", (u,p))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/data')
def data():
    alert_msg = "Normal"
    if getattr(app, "alert", False):
        alert_msg = "🚨 Restricted Zone Breach!"

    return jsonify({
        "energy": random.randint(50,100),
        "temp": random.randint(20,35),
        "occupancy": getattr(app, "count", 0),
        "alerts": alert_msg,
        "positions": getattr(app, "people", []),
        "heatmap": getattr(app, "heatmap", [])
    })

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == "__main__":
 app.run(host="127.0.0.1", port=8000, debug=True)