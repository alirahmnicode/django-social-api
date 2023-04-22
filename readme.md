# Social App

Welcome to the Social App, a Django and Django REST Framework (DRF) project for a social networking web application. This project includes JWT authentication for secure user account management.
# Description

The Social App is a platform for users to create profiles, connect with friends, and share content such as posts, photos, and videos. The project uses Django and DRF to build a RESTful API for creating, reading, updating, and deleting user accounts, posts, and other related data. The app includes features such as authentication and authorization, pagination, filtering, search, and JWT token-based authentication.
# Installation

1. Clone the repository:

````
git clone https://github.com/your-username/social-app.git
````
2. Create a virtual environment and activate it:
```
python -m venv env
source env/bin/activate   # on Linux/MacOS
env\Scripts\activate.bat  # on Windows
```
3. Install the project dependencies:

```
pip install -r requirements.txt
```

4. Run the database migrations to create the database tables:

```
python manage.py migrate
```

5. Start the development server:
```
python manage.py runserver
```
Open the web browser and go to http://localhost:8000 to see the home page.

API Endpoints

The Social App API provides the following endpoints:

    /api/token/ - Obtain JWT token for authentication
    /api/token/refresh/ - Refresh JWT token
    /api/token/verify/ - Verify JWT token
    /api/users/ - User list/create view
    /api/users/<int:pk>/ - User detail/update/delete view
    /api/posts/ - Post list/create view
    /api/posts/<int:pk>/ - Post detail/update/delete view

For more information on how to use these endpoints, please refer to the API documentation.
License

This project is licensed under the MIT License. See the LICENSE file for details.