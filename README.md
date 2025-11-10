# Neunetix Backend

A Django REST framework backend with JWT-based authentication.

## Features

- User registration with email, firstname, lastname, and password
- User login with JWT token authentication
- SQLite database for development
- Custom user model with email as username
- Secure password validation
- Admin interface for user management

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## API Endpoints

### Register User
- **URL**: `/api/auth/register/`
- **Method**: `POST`
- **Auth Required**: No
- **Request Body**:
```json
{
    "email": "user@example.com",
    "firstname": "John",
    "lastname": "Doe",
    "password": "securepassword123",
    "password2": "securepassword123"
}
```
- **Success Response** (201):
```json
{
    "message": "User registered successfully",
    "user": {
        "id": 1,
        "email": "user@example.com",
        "firstname": "John",
        "lastname": "Doe",
        "date_joined": "2025-11-10T05:42:00Z"
    },
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
    }
}
```

### Login User
- **URL**: `/api/auth/login/`
- **Method**: `POST`
- **Auth Required**: No
- **Request Body**:
```json
{
    "email": "user@example.com",
    "password": "securepassword123"
}
```
- **Success Response** (200):
```json
{
    "message": "Login successful",
    "user": {
        "id": 1,
        "email": "user@example.com",
        "firstname": "John",
        "lastname": "Doe",
        "date_joined": "2025-11-10T05:42:00Z"
    },
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
    }
}
```
- **Error Response** (401):
```json
{
    "error": "Invalid email or password"
}
```

## Authentication

After logging in or registering, use the `access` token in the Authorization header for protected endpoints:

```
Authorization: Bearer <access_token>
```

The access token expires after 1 hour. Use the refresh token to obtain a new access token.

## Admin Interface

Access the admin interface at `http://localhost:8000/admin/` to manage users and other data.

## Database

The project uses SQLite for development. The database file is `db.sqlite3` and is excluded from version control.

## Project Structure

```
neunetix-backend/
├── accounts/               # Authentication app
│   ├── models.py          # Custom User model
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── backends.py        # Email authentication backend
│   └── urls.py            # App URLs
├── neunetix/              # Project settings
│   ├── settings.py        # Django settings
│   └── urls.py            # Main URL configuration
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```