@echo off
TITLE Antigravity Simulator Platform
echo ===================================================
echo   AUTONOMOUS ANTIGRAVITY SIMULATION & LEARNING
echo ===================================================
echo.

echo [1/4] Installing Backend Dependencies...
cd backend
pip install --upgrade pip
pip install -r requirements.txt
pip install Flask-PyMongo==2.3.0 bcrypt==4.0.1 celery==5.3.6 redis==5.0.1 qiskit==1.0.0 scikit-learn==1.3.2 pandas==2.1.3 numpy==1.26.2 python-dotenv==1.0.0 gunicorn==21.2.0 PyJWT==2.8.0
if %errorlevel% neq 0 (
    echo Error installing backend dependencies. Check python installation.
    pause
    exit /b
)

echo [2/4] Seeding Database...
python seed_data.py
if %errorlevel% neq 0 (
    echo Error seeding database. Ensure MongoDB is running!
    pause
    exit /b
)

echo [3/4] Installing Frontend Dependencies...
cd ../frontend
call npm install
if %errorlevel% neq 0 (
    echo Error installing frontend dependencies. Check node installation.
    pause
    exit /b
)

echo [4/4] Starting Services...
start "Backend API" cmd /k "cd ../backend && python app.py"
start "Frontend Dashboard" cmd /k "npm start"

echo.
echo Platform is initializing...
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo.
pause
