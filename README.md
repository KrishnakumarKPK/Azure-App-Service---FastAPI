# Azure App Service – FastAPI Deployment 🚀

This repository demonstrates how to deploy a FastAPI application to **Azure App Service** using **GitHub Actions** for CI/CD.

## 🔧 Tech Stack
- FastAPI
- Uvicorn
- GitHub Actions
- Azure App Service

## 📁 Structure
```
├── app/
│   └── main.py            # FastAPI application code
├── requirements.txt       # Python dependencies
├── .github/workflows/
│   └── azure.yml          # GitHub Actions workflow for deployment
```

## 🚀 Getting Started Locally

```bash
# 1. Clone the repository
git clone https://github.com/KrishnakumarKPK/Azure-App-Service---FastAPI.git
cd Azure-App-Service---FastAPI

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000` to see it live.

## 🌐 Live URL
> Replace below with your actual Azure App Service URL  
https://your-app-name.azurewebsites.net

## ⚙️ GitHub Actions Deployment

This repo includes a workflow `.github/workflows/azure.yml` to deploy to Azure automatically when changes are pushed to `main`.

### 🛡️ Secrets Required:
- `AZURE_WEBAPP_PUBLISH_PROFILE`: Found in Azure Portal → App Service → "Get publish profile"

## 🧪 Test Endpoints

- `GET /` → `{ "message": "Hello, Azure with FastAPI!" }`  
- Swagger UI → `/docs`  
- ReDoc UI → `/redoc`

## 📄 requirements.txt

```
fastapi
uvicorn
```

## 👤 Author
**Krishna Kumar K P**  
🔗 [LinkedIn](https://www.linkedin.com/in/krishna-kumar-kondooru-731044256/)

---

⭐ *Star this repo if you found it helpful!*
