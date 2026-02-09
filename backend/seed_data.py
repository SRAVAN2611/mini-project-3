from app import create_app
from models import save_experiment, save_quantum_result, save_prediction, update_leaderboard
from datetime import datetime
import random

app = create_app()

def seed_database():
    print("Seeding database with initial data...")
    with app.app_context():
        # Seed Experiments
        for i in range(20):
            save_experiment({
                'gravity_force': 9.81 + random.uniform(-0.5, 0.5),
                'antigravity_force': random.uniform(0, 3.0),
                'stability_score': random.uniform(0.7, 1.0),
                'energy_input': random.randint(100, 1000),
                'status': 'Completed'
            })
            
        # Seed Quantum Results
        for i in range(10):
            save_quantum_result({
                'counts': {'00': random.randint(400, 600), '11': random.randint(400, 600)},
                'coherence_score': random.uniform(0.8, 0.99),
                'status': 'Success'
            })
            
        # Seed Predictions
        fuel_types = ['Ion', 'Plasma', 'Antimatter', 'Warp']
        for i in range(10):
            save_prediction({
                'fuel_type': random.choice(fuel_types),
                'thrust': random.uniform(100, 5000),
                'heat_dissipation': random.uniform(200, 1000),
                'predicted_efficiency': random.uniform(0.5, 0.99)
            })

        # Seed Leaderboard
        users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace']
        for user in users:
            update_leaderboard(user, random.randint(100, 5000))
            
    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
