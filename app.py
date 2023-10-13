from flask import Flask, jsonify
import os
import threading
import time
import requests
import yt_dlp


app = Flask(__name__)


value = ""

url = 'https://webcast.tiktok.com/webcast/feed/?WebIdLastTime=1646566625&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-GB&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F117.0.0.0%20Safari%2F537.36&channel=tiktok_web&channel_id=42&content_type=1&cookie_enabled=true&device_id=7071949719337600517&device_platform=web_pc&device_type=web_h265&focus_state=false&from_page=live&hidden_banner=true&history_len=3&is_fullscreen=false&is_page_visible=true&max_time=0&os=windows&priority_region=GB&referer=https%3A%2F%2Fwww.tiktok.com%2F%40pablobrimeux%2Fvideo%2F7264241919406951713%3F_r%3D1%26_t%3D8fKQoMg1Mcz&region=DE&req_from=pc_web_side_follow_default&root_referer=https%3A%2F%2Fwww.tiktok.com%2F%40pablobrimeux%2Fvideo%2F7264241919406951713%3F_r%3D1%26_t%3D8fKQoMg1Mcz&screen_height=864&screen_width=1536&tz_name=Asia%2FCalcutta&webcast_language=en&msToken=PCvRi0o_xFphyStCjqy45huwDn54g5DULHEl37IXid_MWNlLyfIVldiwCUoDPq8-d5tol-QkrLm5YqCWfK_BsZu4B2YILnpVdnB7BxUlPJAPCnFUIv9Cf2t55x-K0tVAhrJk5FGPvTEIVWq5LJbZ8Q==&X-Bogus=DFSzswVYX-sANykmtT90FU9WcBnK&_signature=_02B4Z6wo00001iI9bpgAAIDCIj1umAODMvoiPWoAAO20b4'
headers = {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "cookie": "cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22criteo%22:true%2C%22version%22:%22v9%22}; uid_tt=d1777a39aab95efc6175838d834ee66c1771f6c3177d2f394cfed250dcd9a00d; uid_tt_ss=d1777a39aab95efc6175838d834ee66c1771f6c3177d2f394cfed250dcd9a00d; sid_tt=ab8661858cb6876d5947e405c159af57; sessionid=ab8661858cb6876d5947e405c159af57; sessionid_ss=ab8661858cb6876d5947e405c159af57; store-country-code=gb; store-country-code-src=uid; tt-target-idc-sign=dMr6f8tSFDDNS5TTXZ2ouyv6X_ZeBKkOc-p-kbkMQaFU-EO_aTUt8J6kzpAME5KaQAv-9BSc4UwaQbgjMxKHuQj8OokXOSFUTL6O3zqyfKg5DGfgAWQcih6Ilvsji85nGWp0peGJrv7bPmt5EcUf9RxtPiJnZKI0o9OJPKnV-pTCCRnjZRcctDEjOudhxBAkObYttuB0TtTvJXVc5dQL14Aeipaz2SW5jViD4qyAPkiflx2QinFHYM4ikbR5HG6BKcZ8TMj6brBNa7Wm8Y-BNaJXME23N4VRgDc0mzcutqXSJs8L_-lKEF0eKmCNiwDBa8Gu8QMdUgV0KXaLaxe87yZKM--oqwwJS76yp2ci3_3jboUmYQMMsDkBET0Pkc9OvuGxg5tB6iB9ic87FwyHW1moUsrNJmF3stQ2w-YGlQdXDVhtN0cE08LTKcLEqejM-wmxc1UCzOUv0gnQlLJ_23S9kI_S1PrKYZVvYzTvrk7B5yEIid8AJwKbRyFfuyTx; _abck=52453BBEABCBA8205D9DB00B4B7FFCA9~0~YAAQhfxIF+qkmZaGAQAAsM9YmQm5MQT21/GsA7cP+yC01X403PlUGNeUH8LnvepzzIl840ZP4wia0xOQ/XwHz08JH5IbB/jyyN8Vkw9K0bFbTZ2i8tnajNN81JUsZVKFzNgZpWukEpvhKGQogr3qHnjzLgnZvwkDBxEOWYx+8dJGXu5oHwtUM+AfWWAB1V4HYplLqJrufudpQrZVmOEC4kdHmy3w9dXXhvzIPtbWLw4tN2MGfwcRNMcPU3PpfyqlEns/3QHwvXu9BQYKbrR8im8e9zUWnuPY6CLqrkcNUBqjUnljUvdW2K2QODGwUvHn63LJqcQt/M+PVc0onv6m/UANFB8wxuD6KdzfnLtE0LD92SbN32yd3JVhHGT149cQhWOsSf8ve/y486uJCxQssa3sRcrJlLSi~-1~-1~-1; tt-target-idc=useast2a; odin_tt=1fdf34686190760e6f78515235b861e08a0f07acfd8d5f236e3a793fc53926bf6202ffe03b73bd496322c3aa182c4dbe56cae9ca700203b0483215ac8580013961134503dbfd397b0bcc403b76ea9e9a; store-idc=useast2a; tt_chain_token=LfbsG+QP0KfSMC6RDI2ErQ==; sid_guard=ab8661858cb6876d5947e405c159af57%7C1696252128%7C15552000%7CSat%2C+30-Mar-2024+13%3A08%3A48+GMT; sid_ucp_v1=1.0.0-KDJiNmQxZDliM2JlYTkzYjExNjllNGRkY2UxNDQwMTE1NmY5ZGZjMGEKFwiGiIvAgcvHjmMQ4IHrqAYYsws4CEAsEAMaCHVzZWFzdDJhIiBhYjg2NjE4NThjYjY4NzZkNTk0N2U0MDVjMTU5YWY1Nw; ssid_ucp_v1=1.0.0-KDJiNmQxZDliM2JlYTkzYjExNjllNGRkY2UxNDQwMTE1NmY5ZGZjMGEKFwiGiIvAgcvHjmMQ4IHrqAYYsws4CEAsEAMaCHVzZWFzdDJhIiBhYjg2NjE4NThjYjY4NzZkNTk0N2U0MDVjMTU5YWY1Nw; tt_csrf_token=S9Z9avXE-8TPaQt8xGVRJuyeSISwRW2PuxHk; ttwid=1%7C97ynp7Iej7K2KR_2XspVI1L2_7V56T_Pvn8Es3CUdpU%7C1697204662%7C8605a9b8cf0c8ffed3d46b8eb6463ccd06a6f54e6aea9884da9e0c1e1644eee1; csrf_session_id=c73d265a4cedf1c1e80316c4e1edc765; msToken=PCvRi0o_xFphyStCjqy45huwDn54g5DULHEl37IXid_MWNlLyfIVldiwCUoDPq8-d5tol-QkrLm5YqCWfK_BsZu4B2YILnpVdnB7BxUlPJAPCnFUIv9Cf2t55x-K0tVAhrJk5FGPvTEIVWq5LJbZ8Q==",
    "Referer": "https://www.tiktok.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

output_dir = os.path.join(os.getcwd(), "tmp") + "/%(title)s.%(ext)s"
    
    
options = {
    'format': 'best',
    'outtmpl': output_dir
}

ydl = yt_dlp.YoutubeDL(options)


# Define the function you want to run continuously
def my_method():
    global value

    #result = subprocess.check_output(["yt-dlp", "https://www.youtube.com/watch?v=eJmtVr5vptI"], text=True, stderr=subprocess.STDOUT)

    #threading.Timer(1, my_method).start()

        

# Create a thread to run the method
thread = threading.Thread(target=my_method)

# Start the thread when the Flask app starts
@app.before_first_request
def start_thread():
    my_method()
    #thread.start()

@app.route('/test')
def write():
    content = "hi"

    # Specify the file path
    file_path = "/tmp/test.txt"
    
    # Open the file in write mode and write the content
    with open(file_path, 'w') as file:
        file.write(content)
    return "test"

@app.route('/')
def home():

    
    video_url = 'https://www.youtube.com/shorts/SyKF198WZB0'
    """
    with ydl:
          ydl.download(video_url)"""

    
    r = requests.get(url, headers=headers)
    json_data = r.json()  # Parse the JSON response
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
