#!/bin/bash

# Start backend server
echo "Starting backend server..."
cd backend
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 &

# Wait a bit for backend to start
sleep 2

# Start frontend development server
echo "Starting frontend development server..."
cd ../frontend
npm start 