@echo off
echo ===== Django Portfolio Website Setup =====
echo.

echo [1] Running migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo Error running migrations!
    pause
    exit /b 1
)
echo ✓ Migrations completed

echo.
echo [2] Creating superuser...
echo Please enter superuser credentials:
python manage.py createsuperuser
if %errorlevel% neq 0 (
    echo Error creating superuser!
    pause
    exit /b 1
)
echo ✓ Superuser created

echo.
echo ===== Setup Complete! =====
echo.
echo Starting development server...
echo Access the website at: http://localhost:8000/
echo Admin panel at: http://localhost:8000/admin/
echo.
python manage.py runserver

pause
