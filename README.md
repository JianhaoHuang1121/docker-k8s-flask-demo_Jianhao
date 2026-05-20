# 🚀 Docker + Kubernetes Flask Demo

這是一個最小可行版本（MVP）的專案，展示如何將 Flask API 使用 Docker 容器化，並部署到 Kubernetes (Minikube)，同時驗證 Rolling Update 與 HPA 自動擴展。  
此專案作為 DevOps 入門作品集，展現從開發 → 容器化 → 部署 → 叢集管理的完整流程，並延伸到 系統監控與可觀察性（Prometheus + Grafana）。

---

## 📂 專案架構
```
docker-k8s-flask-demo/
│── app.py                # Flask API
│── requirements.txt      # 套件需求
│── Dockerfile            # Docker 映像檔設定
│── flask-deployment.yaml # K8s Deployment + Service
│── prometheus.yml        # Prometheus 設定
│── docker-compose.yml    # 一次啟動 Flask + Prometheus + Grafana
│── README.md             # 文件說明
```

---

## 🛠️ 環境需求
- Python 3.9+
- Docker
- Minikube
- kubectl
- Git (用於版本控制與上傳 GitHub)

---

## 📝 使用步驟

### 1. 啟動 Flask API (本地測試)
```bash
pip install -r requirements.txt
python app.py
```
打開 [http://127.0.0.1:5000](http://127.0.0.1:5000)  
應該會看到：
```
Hello from Docker + K8s!
```

---

### 2. 建立 Docker 映像檔
```bash
docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app
```
再打開 [http://127.0.0.1:5000](http://127.0.0.1:5000)。

---

### 3. 啟動 Minikube
```bash
minikube start --driver=docker
```

---

### 4. 部署到 Kubernetes
```bash
eval $(minikube -p minikube docker-env)   # 切換到 Minikube Docker
docker build -t my-flask-app .            # 在 Minikube 內重新 build image
kubectl apply -f flask-deployment.yaml
```

確認 Pod 狀態：
```bash
kubectl get pods
```

---

### 5. 開啟服務
```bash
minikube service flask-service
```
會自動跳出瀏覽器，顯示服務網址，例如：
```
http://127.0.0.1:30007
```

打開後應該會看到：
```
Hello from Docker + K8s!
```

---

### 6. 測試 Rolling Update
```bash
kubectl set image deployment/flask-deployment flask=my-flask-app:v2
kubectl rollout status deployment/flask-deployment
```

---

### 7. 測試 HPA 自動擴展
```bash
kubectl autoscale deployment flask-deployment --cpu-percent=50 --min=2 --max=5
kubectl get hpa
```

---

## 📈 加入監控 (Prometheus + Grafana)

除了基本的 Docker + Kubernetes 部署，本專案還整合了 **Prometheus** 與 **Grafana**，用來監控 Flask API 的請求數量、速率與延遲。

### 🔧 新增檔案
```
prometheus.yml        # Prometheus 設定
docker-compose.yml    # 一次啟動 Flask + Prometheus + Grafana
```

### 🚀 使用步驟

#### 1. 啟動整個監控環境
```bash
docker-compose up -d
```

#### 2. 開啟服務
- Flask: [http://localhost:5000/hello](http://localhost:5000/hello)  
- Prometheus: [http://localhost:9090](http://localhost:9090)  
- Grafana: [http://localhost:3000](http://localhost:3000) （預設帳密：`admin / admin`）

#### 3. 建立 Grafana Dashboard
- 在 Grafana 新增 **Prometheus Data Source**（URL: `http://host.docker.internal:9090`）  
- 建立三個 Panel：
  - `http_requests_total` → 總請求數  
  - `rate(http_requests_total[1m])` → 每秒請求速率  
  - `rate(http_request_duration_seconds_sum[1m]) / rate(http_request_duration_seconds_count[1m])` → 平均延遲  

### 📊 成果展示
- Prometheus 成功抓取 Flask API 的 `/metrics`  
- Grafana 可視化 API 請求數量、速率與延遲  
- 展現完整 **DevOps 監控 + 可觀察性** 能力  

---

## 📎 參考資源
- [Flask](https://flask.palletsprojects.com/)  
- [Docker](https://docs.docker.com/)  
- [Kubernetes](https://kubernetes.io/)  
- [Minikube](https://minikube.sigs.k8s.io/docs/)  
- [Prometheus](https://prometheus.io/)  
- [Grafana](https://grafana.com/)  
