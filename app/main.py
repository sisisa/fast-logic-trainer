from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.endpoints import training

app = FastAPI(
    title="Fast Logic Trainer API",
    description="エンジニアの思考の反射神経を計測・最適化するためのAPI基盤",
    version="0.1.0"
)

# APIルーターの登録（プレフィックスでバージョン管理を実施）
app.include_router(training.router, prefix="/api/v1/training", tags=["Training"])

@app.get("/health")
def health_check():
    """本番運用を見据えたヘルスチェック用エンドポイント"""
    return {"status": "ok", "latency": "low"}

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    """
    ルートパスへのアクセスを自動的にAPIドキュメントへリダイレクトする。
    include_in_schema=False により、このルート自体はドキュメントに表示させない。
    """
    return RedirectResponse(url="/docs")