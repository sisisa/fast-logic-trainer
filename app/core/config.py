from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Fast Logic Trainer API"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # トレーニングロジック関連の設定
    BASE_SCORE: float = 100.0
    TIME_PENALTY_PER_SECOND: float = 1.0
    KEYWORD_BONUS: float = 2.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore"
    )

settings = Settings()
