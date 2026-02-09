from flask import Blueprint, jsonify, request
from models import get_experiments, get_quantum_results, get_predictions, get_leaderboard
from tasks import run_gravity_experiment, run_quantum_job, run_prediction_job

api = Blueprint('api', __name__)

@api.route('/dashboard', methods=['GET'])
def dashboard_stats():
    # Return aggregated stats
    experiments = get_experiments(1)
    quantum = get_quantum_results(1)
    predictions = get_predictions(1)
    
    stats = {
        'last_experiment': experiments[0] if experiments else None,
        'last_quantum': quantum[0] if quantum else None,
        'last_prediction': predictions[0] if predictions else None,
        'system_status': 'Operational'
    }
    return jsonify(stats)

@api.route('/experiments', methods=['GET'])
def list_experiments():
    return jsonify(get_experiments(10))

@api.route('/quantum', methods=['GET'])
def list_quantum():
    return jsonify(get_quantum_results(10))

@api.route('/predictions', methods=['GET'])
def list_predictions():
    return jsonify(get_predictions(10))

@api.route('/leaderboard', methods=['GET'])
def list_leaderboard():
    return jsonify(get_leaderboard(10))

@api.route('/start_simulation', methods=['POST'])
def start_simulation():
    # Trigger all tasks
    run_gravity_experiment.delay()
    run_quantum_job.delay()
    run_prediction_job.delay()
    return jsonify({'status': 'Simulation started', 'message': 'Tasks queued successfully'})
