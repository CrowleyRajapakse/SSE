from flask import Flask, Response
import time

app = Flask(__name__)

def generate_sse():
    while True:
        time.sleep(1)
        yield f"data: The time is {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"

@app.route('/sse')
def sse():
    return Response(generate_sse(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=5000)

