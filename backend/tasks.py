import os
import random
from config import Config
from models import save_experiment, save_quantum_result, save_prediction, update_leaderboard
from quantum_sim import run_quantum_simulation
from ml_model import PropulsionPredictor

# Check if we should use the mock database/backend
USE_MOCK_DB = os.environ.get('USE_MOCK_DB', 'False').lower() == 'true'

# Initialize Celery or Mock
if USE_MOCK_DB:
    print("WARNING: Using Mock Celery (Synchronous Execution).")
    class MockCelery:
        def task(self, f):
            def delay(*args, **kwargs):
                print(f"Mock Celery: Executing {f.__name__} synchronously...")
                return f(*args, **kwargs)
            f.delay = delay
            return f
    celery = MockCelery()
else:
    from celery import Celery
    celery = Celery(__name__, broker=Config.CELERY_BROKER_URL, backend=Config.CELERY_RESULT_BACKEND)

# Initialize ML Predictor
predictor = PropulsionPredictor()

@celery.task
def run_gravity_experiment():
    """Generates a simulated gravity experiment result."""
    # Simulation logic: fluctuating gravity force
    base_gravity = 9.81
    fluctuation = random.uniform(-0.1, 0.1)
    antigravity_effect = random.uniform(0, 5.0) # hypothetical force
    
    experiment_data = {
        'gravity_force': base_gravity + fluctuation,
        'antigravity_force': antigravity_effect,
        'stability_score': max(0, 1.0 - (antigravity_effect / 10.0)),
        'energy_input': random.randint(100, 5000),
        'status': 'Completed'
    }
    save_experiment(experiment_data)
    return f"Experiment completed. Anti-gravity force: {antigravity_effect}"

@celery.task
def run_quantum_job():
    """Runs a quantum simulation."""
    result = run_quantum_simulation()
    
    # Store result
    save_quantum_result(result)
    return f"Quantum Job Completed. Coherence: {result.get('coherence_score')}"

@celery.task
def run_prediction_job():
    """Runs a propulsion efficiency prediction."""
    # Mock input for prediction
    fuel_types = ['Ion', 'Plasma', 'Antimatter', 'Warp']
    fuel_code = random.randint(0, len(fuel_types)-1)
    thrust = random.uniform(10.0, 1000.0)
    heat = random.uniform(100.0, 5000.0)
    
    efficiency = predictor.predict(fuel_code, thrust, heat)
    
    prediction_data = {
        'fuel_type': fuel_types[fuel_code],
        'thrust': thrust,
        'heat_dissipation': heat,
        'predicted_efficiency': efficiency
    }
    save_prediction(prediction_data)
    return f"Prediction: {efficiency:.2f}"

@celery.task
def update_leaderboard_task():
    """Updates user scores randomly."""
    users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
    user = random.choice(users)
    score_increment = random.randint(10, 100)
    update_leaderboard(user, score_increment)
    return f"Updated {user} score by {score_increment}"
