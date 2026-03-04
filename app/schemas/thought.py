from pydantic import BaseModel, Field
from typing import List

class ThoughtInput(BaseModel):
    topic: str = Field(..., description="思考の対象となるトピック", example="FastAPIの利点")
    keywords: List[str] = Field(..., min_items=1, description="抽出されたキーワード群")
    time_taken_ms: int = Field(..., gt=0, description="思考整理に要したミリ秒（反射神経の指標）")

class ThoughtResult(BaseModel):
    score: float = Field(..., description="算出されたスコア")
    feedback: str = Field(..., description="パフォーマンスに対する論理的なフィードバック")