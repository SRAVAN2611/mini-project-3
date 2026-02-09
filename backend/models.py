import os
import sys

# Check if we should use the mock database
# Default to False, but can be set via env var
USE_MOCK_DB = os.environ.get('USE_MOCK_DB', 'False').lower() == 'true'

if USE_MOCK_DB:
    print("WARNING: Using Mock Database (In-Memory). Data will be lost on restart.")
    from models_mock import (
        init_db,
        create_user,
        verify_user,
        get_user_by_id,
        save_experiment,
        get_experiments,
        save_quantum_result,
        get_quantum_results,
        save_prediction,
        get_predictions,
        update_leaderboard,
        get_leaderboard
    )
else:
    from flask_pymongo import PyMongo
    from datetime import datetime
    import bcrypt

    mongo = PyMongo()

    def init_db(app):
        mongo.init_app(app)

    # User Helpers
    def create_user(username, password):
        if mongo.db.users.find_one({'username': username}):
            return False
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        mongo.db.users.insert_one({
            'username': username,
            'password': password_hash,
            'created_at': datetime.utcnow()
        })
        return True

    def verify_user(username, password):
        user = mongo.db.users.find_one({'username': username})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return user
        return None

    def get_user_by_id(user_id):
        # wrapper if using ObjectId
        pass 

    # Helper functions to interact with MongoDB collections
    def save_experiment(data):
        data['timestamp'] = datetime.utcnow()
        mongo.db.experiments.insert_one(data)

    def get_experiments(limit=10):
        return list(mongo.db.experiments.find({}, {'_id': 0}).sort('timestamp', -1).limit(limit))

    def save_quantum_result(data):
        data['timestamp'] = datetime.utcnow()
        mongo.db.quantum_results.insert_one(data)

    def get_quantum_results(limit=10):
        return list(mongo.db.quantum_results.find({}, {'_id': 0}).sort('timestamp', -1).limit(limit))

    def save_prediction(data):
        data['timestamp'] = datetime.utcnow()
        mongo.db.predictions.insert_one(data)

    def get_predictions(limit=10):
        return list(mongo.db.predictions.find({}, {'_id': 0}).sort('timestamp', -1).limit(limit))

    def update_leaderboard(user, score):
        mongo.db.leaderboard.update_one(
            {'user': user},
            {'$inc': {'score': score}},
            upsert=True
        )

    def get_leaderboard(limit=10):
        return list(mongo.db.leaderboard.find({}, {'_id': 0}).sort('score', -1).limit(limit))
