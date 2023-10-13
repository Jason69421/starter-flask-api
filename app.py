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
    value += 1
    threading.Timer(1, my_method).start()

        

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
