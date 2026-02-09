@echo off
TITLE Antigravity Simulator - Mock Mode
echo ===================================================
echo   ANTIGRAVITY SIMULATION (DEMO / MOCK MODE)
echo ===================================================
echo.
echo NOTE: Using in-memory database. Data will be lost on restart.
echo NOTE: No MongoDB or Redis required.
echo.

set USE_MOCK_DB=true

echo [1/2] Starting Backend...
start "Backend API (Mock)" cmd /k "cd backend && python app.py"

echo [2/2] Starting Frontend...
start "Frontend Dashboard" cmd /k "cd frontend && npm start"

echo.
echo Platform is initializing...
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo.
pause
