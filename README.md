# Simple JWT Authentication with FastAPI

A professional and easy-to-use JWT (JSON Web Token) authentication implementation built with FastAPI. This project provides a complete authentication system including user registration, login, token generation, and protected endpoints.

## 🎯 Features

- **JWT Token-Based Authentication**: Secure token generation and validation
- **User Registration & Login**: Simple user management system
- **Protected Endpoints**: Route protection with Bearer token authentication
- **Role-Based Access Control**: Support for user roles and permissions
- **Secure Password Handling**: Password hashing and validation
- **RESTful API Design**: Clean and intuitive API structure
- **Easy Integration**: Simple to integrate into existing FastAPI applications
- **Async/Await Support**: High-performance asynchronous operations

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/DevOps255/SImple-JWT-authentification-with-FastAPI.git
cd SImple-JWT-authentification-with-FastAPI
```

### 2. Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Create a `requirements.txt` file with the following dependencies:

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
pydantic-settings==2.1.0
```

Then install:

```bash
pip install -r requirements.txt
```

## 🔧 Configuration

Create a `.env` file in the root directory with the following variables:

```env
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./test.db
```

### Environment Variables Explanation

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Secret key for JWT signing | Use `openssl rand -hex 32` |
| `ALGORITHM` | JWT algorithm | HS256, HS512 |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time | 30 (minutes) |
| `DATABASE_URL` | Database connection string | sqlite:///./test.db |

## 📚 Project Structure

```
.
├── main.py              # Application entry point
├── apiauth/             # Authentication module
│   ├── __init__.py      # Package initialization
│   ├── auth.py          # Authentication logic
│   └── schemas.py       # Pydantic models
├── routers/             # API route handlers
│   ├── __init__.py
│   ├── auth_router.py   # Authentication routes
│   └── users_router.py  # User management routes
├── data.py              # Data models and database
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create locally)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🔐 API Endpoints

### Authentication Endpoints

#### Register a New User
- **Endpoint**: `POST /auth/register`
- **Description**: Create a new user account
- **Request Body**:
  ```json
  {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
  }
  ```
- **Response** (201):
  ```json
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "message": "User created successfully"
  }
  ```

#### User Login
- **Endpoint**: `POST /auth/login`
- **Description**: Authenticate user and receive access token
- **Request Body**:
  ```json
  {
    "username": "john_doe",
    "password": "securepassword123"
  }
  ```
- **Response** (200):
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "expires_in": 1800
  }
  ```

#### Refresh Access Token
- **Endpoint**: `POST /auth/refresh`
- **Description**: Get a new access token using refresh token
- **Headers**: `Authorization: Bearer <refresh_token>`
- **Response** (200):
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
  }
  ```

### Protected User Endpoints

#### Get Current User Information
- **Endpoint**: `GET /api/users/me`
- **Description**: Get authenticated user's profile
- **Headers**: `Authorization: Bearer <access_token>`
- **Response** (200):
  ```json
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "created_at": "2026-06-12T10:30:00Z"
  }
  ```

#### Get User by ID
- **Endpoint**: `GET /api/users/{user_id}`
- **Description**: Get user details by user ID
- **Headers**: `Authorization: Bearer <access_token>`
- **Response** (200):
  ```json
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  }
  ```

#### Update User Profile
- **Endpoint**: `PUT /api/users/me`
- **Description**: Update current user's profile
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "email": "newemail@example.com"
  }
  ```
- **Response** (200): Updated user object

#### Delete User Account
- **Endpoint**: `DELETE /api/users/me`
- **Description**: Delete current user account
- **Headers**: `Authorization: Bearer <access_token>`
- **Response** (200):
  ```json
  {
    "message": "User deleted successfully"
  }
  ```

## 🏃 Running the Application

### Development Mode

```bash
# Run the FastAPI server with auto-reload
uvicorn main:app --reload

# The API will be available at http://localhost:8000
```

### Production Mode

```bash
# Run without auto-reload
uvicorn main:app --host 0.0.0.0 --port 8000

# With Gunicorn (for production)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### Interactive API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 💡 Usage Examples

### Using cURL

#### Register a User

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

#### Login

```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepassword123"
  }'
```

#### Access Protected Endpoint

```bash
curl -X GET "http://localhost:8000/api/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE"
```

### Using Python

```python
import requests

BASE_URL = "http://localhost:8000"

# Register
response = requests.post(f"{BASE_URL}/auth/register", json={
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
})
print(response.json())

# Login
response = requests.post(f"{BASE_URL}/auth/login", json={
    "username": "john_doe",
    "password": "securepassword123"
})
token = response.json()["access_token"]

# Access protected endpoint
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(f"{BASE_URL}/api/users/me", headers=headers)
print(response.json())
```

### Using JavaScript/Fetch

```javascript
const BASE_URL = "http://localhost:8000";

// Register
async function register() {
  const response = await fetch(`${BASE_URL}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: "john_doe",
      email: "john@example.com",
      password: "securepassword123"
    })
  });
  return response.json();
}

// Login
async function login() {
  const response = await fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: "john_doe",
      password: "securepassword123"
    })
  });
  return response.json();
}

// Get current user
async function getCurrentUser(token) {
  const response = await fetch(`${BASE_URL}/api/users/me`, {
    method: "GET",
    headers: { "Authorization": `Bearer ${token}` }
  });
  return response.json();
}
```

## 🔒 Security Best Practices

### Implementation Security

1. **Secret Key Management**
   - Never commit `.env` files to version control
   - Use `openssl rand -hex 32` to generate strong keys
   - Rotate keys periodically

2. **Password Security**
   - Passwords are hashed using bcrypt (via passlib)
   - Never store plain-text passwords
   - Implement password strength requirements

3. **Token Security**
   - Set reasonable expiration times (15-30 minutes)
   - Implement refresh token rotation
   - Use HTTPS in production
   - Store tokens securely on the client side

4. **API Security**
   - Implement rate limiting on authentication endpoints
   - Use HTTPS/TLS in production
   - Validate all input data
   - Implement CORS properly

5. **Database Security**
   - Use environment variables for credentials
   - Implement proper database access controls
   - Keep dependencies updated

### Production Checklist

```markdown
- [ ] Change SECRET_KEY to a strong random value
- [ ] Set DEBUG=False in production
- [ ] Use HTTPS/TLS for all connections
- [ ] Configure CORS properly for your domain
- [ ] Set up rate limiting
- [ ] Enable logging and monitoring
- [ ] Use a production database (PostgreSQL, MySQL)
- [ ] Set up proper error handling
- [ ] Implement audit logging
- [ ] Regular security updates
```

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | 0.104+ | Web framework |
| `uvicorn` | 0.24+ | ASGI server |
| `pydantic` | 2.5+ | Data validation |
| `python-jose` | 3.3+ | JWT handling |
| `passlib` | 1.7+ | Password hashing |
| `python-multipart` | 0.0.6+ | Form data handling |

## 🧪 Testing

### Manual Testing

You can test the API directly using:

1. **Swagger UI**: http://localhost:8000/docs (interactive testing)
2. **cURL**: Command-line HTTP testing
3. **Postman**: GUI API testing tool
4. **Python requests**: Programmatic testing

### Example Test Script

```python
import pytest
import requests

BASE_URL = "http://localhost:8000"

def test_register():
    response = requests.post(f"{BASE_URL}/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 201

def test_login():
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "username": "testuser",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_protected_route():
    login_response = requests.post(f"{BASE_URL}/auth/login", json={
        "username": "testuser",
        "password": "testpass123"
    })
    token = login_response.json()["access_token"]
    
    response = requests.get(f"{BASE_URL}/api/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
```

### Running Tests

```bash
# Install pytest
pip install pytest pytest-asyncio httpx

# Run tests
pytest tests/
```

## 🐛 Troubleshooting

### Common Issues

#### 1. Token Expiration Errors

**Problem**: Getting 401 Unauthorized after some time

**Solutions**:
- Verify token hasn't expired (check `ACCESS_TOKEN_EXPIRE_MINUTES`)
- Use refresh token endpoint to get new token
- Check system clock synchronization

#### 2. Authentication Failures

**Problem**: Login failing with correct credentials

**Solutions**:
- Verify SECRET_KEY is consistent
- Check token format: `Authorization: Bearer <token>`
- Ensure user exists in database
- Check password isn't changed unexpectedly

#### 3. Database Errors

**Problem**: SQLite database errors

**Solutions**:
- Verify `DATABASE_URL` in `.env`
- Check file permissions on database file
- Delete `test.db` to reset database
- Run migrations if applicable

#### 4. CORS Issues

**Problem**: Browser blocking requests

**Solutions**:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### 5. Port Already in Use

**Problem**: Port 8000 is already in use

**Solutions**:
```bash
# Use different port
uvicorn main:app --port 8001

# Or kill process using port
# Linux/macOS: lsof -i :8000 | grep LISTEN | awk '{print $2}' | xargs kill
# Windows: netstat -ano | findstr :8000
```

## 🚀 Deployment

### Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t fastapi-jwt-auth .
docker run -p 8000:8000 --env-file .env fastapi-jwt-auth
```

### Cloud Deployment

#### Heroku

```bash
heroku create your-app-name
heroku config:set SECRET_KEY=your-secret-key
git push heroku main
```

#### AWS/DigitalOcean/GCP

Follow platform-specific guides for deploying Python FastAPI applications.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-asyncio black flake8 mypy

# Format code
black .

# Lint
flake8 .

# Type check
mypy .
```

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**DevOps255**

- GitHub: [@DevOps255](https://github.com/DevOps255)
- Repository: [SImple-JWT-authentification-with-FastAPI](https://github.com/DevOps255/SImple-JWT-authentification-with-FastAPI)

## 📞 Support & Contact

For issues, questions, or suggestions:

- Open an [Issue](https://github.com/DevOps255/SImple-JWT-authentification-with-FastAPI/issues)
- Start a [Discussion](https://github.com/DevOps255/SImple-JWT-authentification-with-FastAPI/discussions)
- Review [documentation](https://fastapi.tiangolo.com/)

## 🚀 Roadmap

- [ ] OAuth2 provider integration (Google, GitHub)
- [ ] Email verification system
- [ ] Two-factor authentication (2FA)
- [ ] Database migration system (Alembic)
- [ ] Comprehensive test suite with 90%+ coverage
- [ ] Docker Compose setup
- [ ] Kubernetes deployment templates
- [ ] GraphQL API support
- [ ] Rate limiting per endpoint
- [ ] Audit logging system

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [JWT.io Introduction](https://jwt.io/introduction)
- [OWASP Authentication Best Practices](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python-Jose Documentation](https://python-jose.readthedocs.io/)
- [Passlib Documentation](https://passlib.readthedocs.io/)

---

**Last Updated**: June 2026  
**Version**: 1.0.0  
**Status**: ✅ Production Ready
