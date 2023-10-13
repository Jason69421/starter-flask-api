from flask import Flask
import os
import threading
import time
import subprocess

app = Flask(__name__)

value = ""

# Define the function you want to run continuously
def my_method():
    global value
    result = subprocess.check_output(["yt-dlp", "https://www.youtube.com/watch?v=eJmtVr5vptI"], text=True, stderr=subprocess.STDOUT)
    value = result
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
