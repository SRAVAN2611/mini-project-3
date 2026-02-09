from datetime import datetime
import bcrypt

class MockDB:
    def __init__(self):
        self.users = [{
            'username': 'admin',
            'password': bcrypt.hashpw('password123'.encode('utf-8'), bcrypt.gensalt()),
            'created_at': datetime.utcnow()
        }]
        self.experiments = []
        self.quantum_results = []
        self.predictions = []
        self.leaderboard = {'admin': 1500}

mock_db = MockDB()

def init_db(app):
    print("Initialize Mock DB (In-Memory)")

# User Helpers
def create_user(username, password):
    if any(u['username'] == username for u in mock_db.users):
        return False
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    mock_db.users.append({
        'username': username,
        'password': password_hash,
        'created_at': datetime.utcnow()
    })
    return True

def verify_user(username, password):
    user = next((u for u in mock_db.users if u['username'] == username), None)
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return user
    return None

def get_user_by_id(user_id):
    pass 

# Helper functions to interact with Mock DB
def save_experiment(data):
    data['timestamp'] = datetime.utcnow()
    mock_db.experiments.append(data)

def get_experiments(limit=10):
    sorted_experiments = sorted(mock_db.experiments, key=lambda x: x['timestamp'], reverse=True)
    return sorted_experiments[:limit]

def save_quantum_result(data):
    data['timestamp'] = datetime.utcnow()
    mock_db.quantum_results.append(data)

def get_quantum_results(limit=10):
    sorted_results = sorted(mock_db.quantum_results, key=lambda x: x['timestamp'], reverse=True)
    return sorted_results[:limit]

def save_prediction(data):
    data['timestamp'] = datetime.utcnow()
    mock_db.predictions.append(data)

def get_predictions(limit=10):
    sorted_predictions = sorted(mock_db.predictions, key=lambda x: x['timestamp'], reverse=True)
    return sorted_predictions[:limit]

def update_leaderboard(user, score):
    current_score = mock_db.leaderboard.get(user, 0)
    mock_db.leaderboard[user] = current_score + score

def get_leaderboard(limit=10):
    sorted_leaderboard = sorted(mock_db.leaderboard.items(), key=lambda x: x[1], reverse=True)
    return [{'user': k, 'score': v} for k, v in sorted_leaderboard[:limit]]
