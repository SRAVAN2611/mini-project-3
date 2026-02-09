# System Architecture

```mermaid
graph TD
    User[User] -->|Interacts| Frontend[React Frontend]
    
    subgraph Frontend Layer
        Frontend -->|HTTP Requests| API[Flask API]
        Charts[Chart.js / Visualizers]
    end
    
    subgraph Backend Layer
        API -->|Read/Write| DB[(MongoDB)]
        API -->|Trigger Tasks| Celery[Celery Workers]
        
        Celery -->|Run Simulation| Qiskit[Quantum Engine (Qiskit)]
        Celery -->|Predict| ML[AI Model (Scikit-Learn)]
        Celery -->|Generate| Sim[Physics Engine]
        
        Scheduler[Auto Scheduler] -->|Periodic Triggers| Celery
    end
    
    subgraph Data Layer
        DB -->|Store| Experiments[Experiments Data]
        DB -->|Store| Quantum[Quantum Results]
        DB -->|Store| Users[User Profiles]
        Datasets[CSV Files] -->|Load| ML
    end
```

## Data Flow
1. **Experiment Trigger**: User or Scheduler triggers a simulation.
2. **Processing**: Celery worker picks up the task.
   - For **Gravity**: Generates physics data based on random fluctuations.
   - For **Quantum**: Runs Qiskit circuit and returns measurement counts.
   - For **Prediction**: Loads latest dataset features and predicts efficiency.
3. **Storage**: Results are stored in MongoDB.
4. **Visualization**: React Frontend polls API endpoint and updates charts/leaderboards in real-time.
