import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'antigravity-secret-key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/antigravity_db'
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') or 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') or 'redis://localhost:6379/0'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'datasets')
