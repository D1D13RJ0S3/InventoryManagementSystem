@echo off
:: Activate virtual environment
call venv\Scripts\activate.bat

:: Run the application with Uvicorn on port 5000
uvicorn app:app --reload --host 0.0.0.0 --port 5000
