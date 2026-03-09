import random
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List

from app.schemas.thought import ThoughtInput, ThoughtResult
from app.core.logic import evaluate_thought_speed
from app.core.topics import get_topics

router = APIRouter()

# 新しい型定義（レスポンス用）
class TopicResponse(BaseModel):
    topic: str

def get_random_topic_logic(topics: List[str] = Depends(get_topics)) -> str:
    """ランダムなトピックを取得するロジック（依存性注入用）"""
    return random.choice(topics)

@router.get("/topic", response_model=TopicResponse)
async def get_random_topic(topic: str = Depends(get_random_topic_logic)):
    """ランダムな技術的お題を提供するエンドポイント"""
    return TopicResponse(topic=topic)

@router.post("/evaluate", response_model=ThoughtResult)
async def evaluate_thought(thought: ThoughtInput, evaluator: callable = Depends(lambda: evaluate_thought_speed)):
    """思考データを評価する"""
    result = evaluator(thought)
    return result