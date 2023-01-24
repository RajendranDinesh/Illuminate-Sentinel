import sqlite3
import datetime

def save_video(video_path):
    conn = sqlite3.connect('camera.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, path TEXT, timestamp DATETIME)''')
    timestamp = datetime.datetime.now()
    c.execute("INSERT INTO videos (path, timestamp) VALUES (?,?)", (video_path, timestamp))
    conn.commit()
    video_id = c.lastrowid
    conn.close()
    return video_id
