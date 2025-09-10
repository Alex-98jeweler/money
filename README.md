# Django REST Framework Project Setup

## Project Overview

This is a Django REST Framework (DRF) project designed for building robust web APIs. The project uses Python 3.8.10+ and SQLite3 database.

## Prerequisites

- **Python**: Version 3.8.10 or higher
- **Database**: SQLite3 (included with Python)
- **Operating System**: Windows, Linux, or macOS

## Manual Setup Guide

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

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver