# Django REST Framework Project Setup

## Project Overview

This is a Django REST Framework (DRF) project for money movements. The project uses Python 3.8.10+ and SQLite3 database.

## Prerequisites

- **Python**: Version 3.8.10 or higher
- **Database**: SQLite3 (included with Python)
- **Operating System**: Windows, Linux, or macOS

## Setup Guide

### For Windows Users

```bash
# Clone the repository
git clone <repository-url>
cd <project-directory>

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser for django admin available
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### For Linux/macOS Users

```bash
# Clone the repository
git clone <repository-url>
cd <project-directory>

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser for django admina available
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

After setup, you can open http://127.0.0.1:8000/ for login in django admin site. On this site you can 
edit entities of this project.


## Documentation

API documentation is available at:
http://127.0.0.1:8000/doc/


## Explanation 
This project contains RESTFull api endpoints, you can test it on postman or or in any other way convenient for you. Body, params and etc you can see on the documenattion url.