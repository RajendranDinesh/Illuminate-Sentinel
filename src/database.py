import sqlite3
import datetime

def store_image_path(image_path):
    # Connect to the database
    conn = sqlite3.connect('light_sources.db')
    c = conn.cursor()

    # Create a table for storing image paths if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS image_paths (id INTEGER PRIMARY KEY, path TEXT, timestamp TIMESTAMP)''')

    # Get the current timestamp
    timestamp = datetime.datetime.now()

    # Insert the image path and timestamp into the database
    c.execute("INSERT INTO image_paths (path, timestamp) VALUES (?, ?)", (image_path, timestamp))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
