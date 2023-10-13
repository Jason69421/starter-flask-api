from flask import Flask
import os
import threading
import time
import subprocess
import yt_dlp

app = Flask(__name__)
ydl = yt_dlp.YoutubeDL()

value = ""

options = {
    'format': 'best',  # Choose the best available video quality
    'outtmpl': 'tmp/%(title)s.%(ext)s',  # Specify the download location and filename format
}

# Define the function you want to run continuously
def my_method():
    global value
    video_url = 'https://www.youtube.com/watch?v=kfchvCyHmsc&pp=ygUONSBzZWNvbmQgdmlkZW8%3D'
    with ydl:
        result = ydl.extract_info(video_url, download=True, extra_info=options)

    if result['status'] == 'finished':
        video_filename = result['filename']
        print(f"Video downloaded to: {video_filename}")
    
        # Check the size of the downloaded file
        if os.path.exists(video_filename):
            file_size = os.path.getsize(video_filename)
            print(f"File size: {file_size} bytes")
        else:
            print("File not found.")
    #result = subprocess.check_output(["yt-dlp", "https://www.youtube.com/watch?v=eJmtVr5vptI"], text=True, stderr=subprocess.STDOUT)
    value = video_filename
    #threading.Timer(1, my_method).start()

        

# Create a thread to run the method
thread = threading.Thread(target=my_method)

# Start the thread when the Flask app starts
@app.before_first_request
def start_thread():
    my_method()
    #thread.start()

@app.route('/')
def home():
    return 'Home Page Route: ' + str(value)

if __name__ == '__main__':
    app.run()
