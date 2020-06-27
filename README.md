# **NUS Scheduler Backend**

## **Running the Backend Locally**
- ### **Prerequisites**
    Follow these guides for installation:
    1. **Python 3** </br>
        https://www.python.org/downloads/
    
    2. **Pip** </br>
        https://pip.pypa.io/en/stable/installing/
    
    3. **Virtualenv** </br>
        https://virtualenv.pypa.io/en/latest/installation.html

    4. **Postgresql** </br>
        https://www.postgresql.org/download/
    
    5. **Django** </br>
        https://docs.djangoproject.com/en/3.0/topics/install/
    
    

- ### **Installation Guide**
    Type these step-by-step instructions into your terminal.
    1. **Clone the repository**
        ```
        https://github.com/GoneWildOrbital2020/NUS-scheduler-backend.git
        ```

    2. **Create virtual environment**
        ```
        cd NUS-scheduler-backend
        virtualenv venv
        ```

    3. **Install dependencies**
        ```
        source venv/bin/activate
        cd scheduler
        pip3 install -r requirements.txt
        ```

    4. **Create database** </br>
        Open `psql` terminal:
        ```
        sudo su postgres
        psql
        ```
        Create user:
        ```
        CREATE USER [your username] WITH PASSWORD [your user's password];
        ```
        Create database:
        ```
        CREATE DATABASE [database name] WITH OWNER [your username];
        ```

- ### **Usage Guide**
    1. **Run the frontend locally** </br>
        Follow this guide: </br>
        https://github.com/GoneWildOrbital2020/nus-scheduler-frontend

    2. **Configure the database** </br>
        From `NUS-scheduler-backend`, go to `scheduler/scheduler/settings.py` and search for `DATABASES`. Edit according to your created database.
        ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': [your database name],
                'USER': [owner of database],
                'PASSWORD': [user password],
                'HOST': 'localhost',
                'PORT': '5432'
            }
        }
        ```

    3. **Run the backend** </br>
        From `NUS-scheduler-backend`
        ```
        cd scheduler
        python3 manage.py migrate
        python3 manage.py runserver
        ```