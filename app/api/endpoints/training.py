import random
from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.thought import ThoughtInput, ThoughtResult
from app.core.logic import evaluate_thought_speed

router = APIRouter()

# 新しい型定義（レスポンス用）
class TopicResponse(BaseModel):
    topic: str

# お題のモックデータベース
TOPICS = [
    "オブジェクト指向の3大要素を説明せよ",
    "REST APIの設計原則を3つ挙げよ",
    "RDBとNoSQLの使い分けの基準は何か",
    "「関心の分離」がもたらすメリットとは",
    "GitにおけるRebaseとMergeの違いを説明せよ"
]

@router.get("/topic", response_model=TopicResponse)
async def get_random_topic():
    """ランダムな技術的お題を提供するエンドポイント"""
    return TopicResponse(topic=random.choice(TOPICS))

@router.post("/evaluate", response_model=ThoughtResult)
async def evaluate_thought(thought: ThoughtInput):
    """思考データを評価する"""
    result = evaluate_thought_speed(thought)
    return result