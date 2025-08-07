@echo off
echo Starting FastAPI server...
start cmd /k "python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

timeout /t 3 /nobreak >nul

echo Testing webhook endpoints...
python webhook_client.py

echo.
echo Webhook server is running at http://localhost:8000
echo Press Ctrl+C in the server window to stop
pause
