from flask import Flask, Response, request
import queue

app = Flask(__name__)

clients = []

def notify_clients(message):
    for client in clients:
        client.put(message)

def event_stream(client):
    while True:
        message = client.get()
        yield f'data: {message}\n\n'

@app.route('/chat/send', methods=['POST'])
def send_message():
    if request.is_json:
        data = request.get_json()
        print(f"Received data: {data}")
        notify_clients(data)
        return {"status": "success", "message": "Message sent!"}, 200
    return {"status": "error", "message": "Invalid JSON"}, 400

@app.route('/chat/stream')
def stream():
    def new_messages():
        client = queue.Queue()
        clients.append(client)
        return event_stream(client)
    return Response(new_messages(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=5000)
