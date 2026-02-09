from flask import Flask
from flask_cors import CORS
from config import Config
from models import init_db
from routes import api
from auth import auth_bp
from tasks import celery
import threading
import time

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    init_db(app)
    
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    return app

app = create_app()

def run_auto_scheduler():
    """Simple background thread to trigger tasks periodically without separate beat server for simplicity."""
    from tasks import run_gravity_experiment, run_quantum_job, run_prediction_job, update_leaderboard_task
    with app.app_context():
        while True:
            print("Auto-scheduler: Triggering tasks...")
            run_gravity_experiment.delay()
            run_quantum_job.delay()
            run_prediction_job.delay()
            update_leaderboard_task.delay()
            time.sleep(30) # Run every 30 seconds

if __name__ == '__main__':
    # Start auto-scheduler in a background thread
    scheduler_thread = threading.Thread(target=run_auto_scheduler, daemon=True)
    scheduler_thread.start()
    
    app.run(debug=True, port=5000)
