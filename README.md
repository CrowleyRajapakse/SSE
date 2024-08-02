## SSE POC for APK

### Build SSE Backends

1. ) Switch to chat_server and run docker build command

docker build -t sse-chat-server:latest .

2. ) Switch to sse_server and run docker build command

docker build -t sse-server:latest .

### Build Envoy Image

Switch to envoy and run docker build command

docker build -t envoy-proxy:latest .

(Optional) If need change the envoy.yaml and rebuild the image


### Apply K8s resources

Switch to K8sresources and run following commands

kubectl create namespace apk

kubectl apply -f . -n apk

kubectl port-forward service/envoy-proxy 9095:9095 9901:9901 -n apk


### Try Out Use case

#### SSE Stream

curl http://localhost:9095/sse


#### SSE Chat

curl http://localhost:9095/chat/stream

curl http://localhost:9095/chat/send -X POST -d "message=Hello"










