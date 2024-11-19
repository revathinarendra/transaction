#!/bin/bash

# Ensure pip is available
/usr/bin/python3.9 -m ensurepip --upgrade

# Upgrade pip
/usr/bin/python3.9 -m pip install --upgrade pip

# Install dependencies from requirements.txt
/usr/bin/python3.9 -m pip install -r requirements.txt

# Create the public/static directory for Vercel
mkdir -p public/static

# Collect static files into the public/static directory
python3.9 manage.py collectstatic --noinput

# Apply database migrations (migrations should already exist)
python3.9 manage.py migrate
