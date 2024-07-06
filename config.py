import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER_PORT = os.getenv('SERVER_PORT', 8090)
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False