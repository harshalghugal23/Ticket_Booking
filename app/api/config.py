import os

class Config:
    # Use PostgreSQL in Docker, SQLite locally
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DB_PATH",
        "sqlite:///bookings.db"  # fallback for local testing
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
