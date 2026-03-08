from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.api.endpoints import training

app = FastAPI(
    title="Fast Logic Trainer API",
    description="エンジニアの思考の反射神経を計測・最適化するためのAPI基盤",
    version="0.1.0"
)

# テンプレートエンジンのマウント
templates = Jinja2Templates(directory="app/templates")

app.include_router(training.router, prefix="/api/v1/training", tags=["Training"])

@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    """
    ブラウザ用トレーニングUIを提供するエンドポイント。
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health_check():
    """ヘルスチェック用エンドポイント"""
    return {"status": "ok", "latency": "low"}