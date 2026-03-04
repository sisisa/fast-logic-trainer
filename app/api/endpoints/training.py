from fastapi import APIRouter
from app.schemas.thought import ThoughtInput, ThoughtResult
from app.core.logic import evaluate_thought_speed

router = APIRouter()

@router.post("/evaluate", response_model=ThoughtResult)
async def evaluate_thought(thought: ThoughtInput):
    """
    ユーザーの思考データを入力とし、反射神経スコアを返却するエンドポイント。
    """
    # ビジネスロジックの呼び出しのみを行い、ルーティング層にはロジックを書かない
    result = evaluate_thought_speed(thought)
    return result