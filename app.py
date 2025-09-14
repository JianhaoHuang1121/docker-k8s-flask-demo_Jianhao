from flask import Flask
import time
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# 定義指標
REQUEST_COUNT = Counter(
    'http_requests_total', 'Total HTTP Requests',
    ['method', 'endpoint']
)
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds', 'Request latency'
)

@app.route("/hello")
def hello():
    start_time = time.time()

    # 計數請求
    REQUEST_COUNT.labels(method='GET', endpoint='/hello').inc()

    # 模擬回應
    response = "Hello World!"

    # 紀錄延遲
    REQUEST_LATENCY.observe(time.time() - start_time)

    return response

# 新增 /metrics endpoint
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
