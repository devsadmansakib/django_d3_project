# Django D3 Project

A Django web application that showcases user authentication, D3.js data visualization, and a REST API with token-based authentication. This project also includes a signup and login system, a secure dashboard, and a responsive design using Bootstrap.

## Project Overview

This project demonstrates the following:
- **D3.js Visualization**: Interactive data visualization with D3.js, displaying a pie chart with sample data.
- **REST API**: Secure API endpoints for retrieving data with JWT-based authentication.
- **User Authentication**: Features signup, login, and logout functionality.
- **Bootstrap UI**: Responsive design for a clean user interface.

## Features

- **User Signup and Login**: Allows new users to register and existing users to log in.
- **D3.js Chart**: Displays a pie chart using D3.js after successful login.
- **JWT Authentication**: Secure API endpoints with JSON Web Token (JWT) authentication.
- **Responsive Design**: Clean and responsive design using Bootstrap.

## Setup Instructions

### Prerequisites

- **Python** 3.x installed on your machine.
- **Django** and **Django REST Framework** installed.
- **PostgreSQL** or **SQLite** database (optional, depending on your setup).

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Step 2: Set Up Virtual Environment

Create and activate a virtual environment named `env`:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### Step 3: Install Dependencies

Install all dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database

Run the migrations to set up the database:

```bash
python manage.py migrate
```

### Step 5: Create a Superuser

To access the Django admin, create a superuser:

```bash
python manage.py createsuperuser
```

### Step 6: Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the application.

## Usage

1. **Sign Up**: Register a new user account on the signup page.
2. **Login**: Log in to access the dashboard and view the D3.js chart.
3. **REST API**: Access API endpoints for retrieving chart data using JWT tokens.

### API Endpoints

- **Get JWT Token**: `/api/token/` - Obtain access and refresh tokens by providing username and password.
- **Refresh Token**: `/api/token/refresh/` - Refresh the access token using the refresh token.
- **Chart Data**: `/api/chart-data/` - Authenticated endpoint for retrieving chart data in JSON format.

Once deployed, you will be able to access the site at: [https://d3.sadman.dev](https://d3.sadman.dev)

## Directory Structure

- **`chart`**: Contains the Django app with views, models, templates, and static files.
- **`templates`**: HTML templates for signup, login, and chart pages.
- **`static`**: Static files for styling and scripts.

## Technologies Used

- **Django**: Backend framework for web development.
- **Django REST Framework**: For building RESTful APIs.
- **D3.js**: Data visualization library for charts.
- **Bootstrap**: For responsive design and layout.
- **JWT**: Token-based authentication.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
