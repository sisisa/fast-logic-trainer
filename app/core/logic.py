from app.schemas.thought import ThoughtInput, ThoughtResult
from app.core.config import settings

def evaluate_thought_speed(data: ThoughtInput) -> ThoughtResult:
    """思考の速度と情報量からパフォーマンスを評価する純粋関数"""
    
    # 設定ファイルからスコアリング情報を取得
    base_score = settings.BASE_SCORE
    
    # 1秒（1000ms）ごとのペナルティとキーワード加点
    time_penalty = (data.time_taken_ms / 1000.0) * settings.TIME_PENALTY_PER_SECOND
    keyword_bonus = len(data.keywords) * settings.KEYWORD_BONUS
    
    final_score = max(0.0, base_score - time_penalty + keyword_bonus)
    
    feedback = "最適化された反射神経です" if final_score > 80 else "レイテンシの改善が必要です"
    
    return ThoughtResult(
        score=round(final_score, 2),
        feedback=feedback
    )