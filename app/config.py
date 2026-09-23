import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DB_HOST: str = os.getenv("DB_HOST", "")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "postgres")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")

    @property
    def database_url(self) -> str:
        host = os.getenv("DB_HOST", "").strip()
        if not host or host.startswith("tu-") or host == "localhost":
            return "sqlite:///./test.db"
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{host}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()