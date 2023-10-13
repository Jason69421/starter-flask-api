from flask import Flask
import os
import threading
import time

app = Flask(__name__)

value = 0

# Define the function you want to run continuously
def my_method():
    global value
    os.system("yt-dlp")
    #while True:
        #time.sleep(1)
        #value += 1
        

# Create a thread to run the method
thread = threading.Thread(target=my_method)

# Start the thread when the Flask app starts
@app.before_first_request
def start_thread():
    thread.start()

@app.route('/')
def home():
    return 'Home Page Route: ' + str(value)
