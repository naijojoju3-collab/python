#!/bin/bash
echo "===== Django Portfolio Website Setup ====="
echo ""

echo "[1] Running migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Error running migrations!"
    exit 1
fi
echo "✓ Migrations completed"

echo ""
echo "[2] Creating superuser..."
echo "Please enter superuser credentials:"
python manage.py createsuperuser
if [ $? -ne 0 ]; then
    echo "Error creating superuser!"
    exit 1
fi
echo "✓ Superuser created"

echo ""
echo "===== Setup Complete! ====="
echo ""
echo "Starting development server..."
echo "Access the website at: http://localhost:8000/"
echo "Admin panel at: http://localhost:8000/admin/"
echo ""
python manage.py runserver
