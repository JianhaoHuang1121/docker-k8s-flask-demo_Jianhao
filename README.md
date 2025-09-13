# 🚀 Docker + Kubernetes Flask Demo

這是一個最小可行版本（MVP）的專案，展示如何將 **Flask API** 使用 **Docker 容器化**，並部署到 **Kubernetes (Minikube)**，同時驗證 **Rolling Update** 與 **HPA 自動擴展**。  
此專案作為 **DevOps 入門作品集**，展現從開發 → 容器化 → 部署 → 叢集管理的完整流程。

---

## 📂 專案架構
```
docker-k8s-flask-demo/
│── app.py                # Flask API
│── requirements.txt      # 套件需求
│── Dockerfile            # Docker 映像檔設定
│── flask-deployment.yaml # K8s Deployment + Service
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

## 📊 成果展示
✅ 使用 Docker 將 Flask API 容器化  
✅ 部署於 Kubernetes (Minikube)  
✅ 測試 Rolling Update 與 HPA 自動擴展  
✅ 適合作為 DevOps / Cloud-Native 入門展示專案  

---


「使用 Docker 將 Flask API 容器化，部署於 Minikube，實作 Rolling Update 與 HPA，展示雲原生服務彈性擴展。」

---

## 📎 參考資源
- [Flask](https://flask.palletsprojects.com/)  
- [Docker](https://docs.docker.com/)  
- [Kubernetes](https://kubernetes.io/)  
- [Minikube](https://minikube.sigs.k8s.io/docs/)  
