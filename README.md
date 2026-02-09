# Autonomous Antigravity Simulation & Learning Platform

A full-stack platform that simulates gravity/antigravity experiments, runs quantum field simulations using Qiskit, predicts propulsion efficiency using AI/ML, and gamifies the experience with a live leaderboard.

## Features
- **Gravity Experiments**: Simulated data visualization of gravity vs. antigravity forces.
- **Quantum Simulation**: Run Bell state simulations on Qiskit (or mock) and visualize qubit coherence.
- **AI Propulsion Prediction**: Predict engine efficiency based on fuel type and thrust using Scikit-Learn.
- **Live Leaderboard**: Gamification element tracking user contributions.
- **Automated Tasks**: Background Celery workers handling simulations and updates.

## Tech Stack
- **Frontend**: React.js, Chart.js, CSS3 (Glassmorphism)
- **Backend**: Flask, Python
- **Database**: MongoDB
- **Task Queue**: Celery + Redis
- **AI/ML**: Scikit-learn, Pandas
- **Quantum**: Qiskit

## Prerequisites
- Python 3.8+
- Node.js 14+
- MongoDB (Running locally on default port 27017)
- Redis (Running locally on default port 6379)

## Setup Instructions

### 1. Backend Setup
```bash
cd backend
# Create virtual environment (optional but recommended)
python -m venv venv
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask App (includes auto-scheduler for tasks)
python app.py
```
The backend runs at `http://localhost:5000`.

### 2. Frontend Setup
```bash
cd frontend
# Install dependencies
npm install

# Start the React App
npm start
```
The frontend runs at `http://localhost:3000`.

## Worker Setup (Optional for Scale)
To run Celery workers separately instead of the thread-based scheduler in `app.py`:
```bash
cd backend
celery -A tasks worker --loglevel=info
```

## Datasets
Mock datasets are located in `datasets/`:
- `gravity_data.csv`
- `quantum_field.csv`
- `propulsion.csv`
