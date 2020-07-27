# **NUS Scheduler Backend**

## **Is Now Online**

The backend admin page can be visited on https://nus-scheduler-backend.herokuapp.com/admin/, but requires a superuser or admin account to access. 

## **Running the Backend Locally**
If you are on windows, the following commands may not be compatible with Windows PowerShell or Command Prompt. We recommend to use WSL2.
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

## **API Endpoints**

## **Calendar**

- ### **`/calendars/:year/:month/:day`**
    Get, create or update events in a specific day. </br>
    ### **GET**
    **Request**
    ```
    {
        method: 'GET',
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    [
        {
            "model": ...,
            "pk": ...,
            "fields": {
                "index": ...,
                "title": ...,
                "description": ...,
                "start": ...,
                "end": ...,
                "location": ...,
                "color": ...,
                "day": ...,
                "group": ...,
                "repeated_event": ...
            }
        }
    ]
    ```

    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: [{
            "index": ...,
            "color": ...,
            "title": ...,
            "description": ...,
            "start": ...,
            "end": ...,
            "location": ...,
        }]
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/calendars/:year/:month`**
    Get events in a specific month. </br>
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    [
        {
            "id": ...,
            "day": ...,
            "index": ...,
            "title": ...,
            "description": ...,
            "start": ...,
            "end": ...,
            "location": ...,
            "color": ...,
            "group": ...,
            "repeated_event": ...
        },
    ]
    ```

- ### **`/calendars/deleteyear/:year`**
    Delete a specific year. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/calendars//addyear/:year`**
    Delete a specific year. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/calendars/checkleap/:year`**
    Check if a year is a leap year. </br>
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {
        "leap": ...
    }
    ```

- ### **`/calendars/getyear/`**
    Get all years that have been created. </br>
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    [
        {
            "model": ...,
            "pk": ...,
            "fields": {
                "index": ...,
                "user": ...,
                "is_leap": ...
            }
        }
    ]
    ```

- ### **`/calendars/:year`**
    Get the number of events in a specific year. </br>
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {
        "count": ...
    }
    ```

## **Events**

- ### **`/events/rep/:name`**
    Create a new repeated event. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "name": ...,
        }
    }
    ```
    **Response**
    ```
    {
        "id": ...
    }
    ```

- ### **`/events/nusmod/`**
    Parse .ics file from NUSMods and update the scheduler. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "ics": ...,
        }
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/events/activity/:name`**
    Get or delete an event group. </br>
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "name": ...,
        }
    }
    ```
    **Response**
    ```
    {
        "name": ...,
        "rep": [
            {
                "name": ...,
                "events": [
                    {
                        "index": ...,
                        "title": ...,
                        "description": ...,
                        "start": ...,
                        "end": ...,
                        "location": ...,
                        "color": ...,
                        "day": ...,
                        "month": ...,
                        "year": ...,
                        "id": ...
                    }
                ]
            }
        ]
    }
    ```
    ### **DELETE**
    **Request**
    ```
    {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/events/:event_id`**
    Update or delete a specific event. </br>
    ### **PUT**
    **Request**
    ```
    {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "title": ...,
            "description": ...,
            "start": ...,
            "end": ...,
            "location": ...,
            "color": ...,
        }
    }
    ```
    **Response**
    ```
    {}
    ```
    ### **DELETE**
    **Request**
    ```
    {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/events`**
    Get all event group or create a new one. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "name": ...,
        }
    }
    ```
    **Response**
    ```
    {}
    ```
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    [
        {
            "model": ...,
            "pk": ...,
            "fields": {
                "name": ...
            }
        }
    ]
    ```

- ### **`/events/:name/:rep_id/all`**
    Delete all a specific event group. </br>
    ### **DELETE**
    **Request**
    ```
    {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/events/:name/:rep_id`**
    Delete or update all events in an activity or create a new event in an activity. </br>
    ### **DELETE**
    **Request**
    ```
    {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {}
    ```
    ### **PUT**
    **Request**
    ```
    {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "data": {
                "title": ...,
                "description": ...,
                "start": ...,
                "end": ...,
                "location": ...,
                "color": ...,
            },
        },
    }
    ```
    **Response**
    ```
    {}
    ```
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "data": {
                "title": ...,
                "description": ...,
                "start": ...,
                "end": ...,
                "location": ...,
                "color": ...,
            },
            "day": ...,
            "month": ...,
            "year": ...,
        },
    }
    ```
    **Response**
    ```
    {
        "color": ...,
        "day": ...,
        "description": ...,
        "end": ...,
        "id": ...,
        "index": ...,
        "location": ...,
        "month": ...,
        "start": ...,
        "title": ...,
        "year": ...
    }
    ```
## **Tasks**

- ### **`/tasks/:name/:id`**
    Delete or update a task. </br>
    ### **DELETE**
    **Request**
    ```
    {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {}
    ```
    ### **PUT**
    **Request**
    ```
    {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "data": {
                "index": ...,
                "column_id": ...,
            },
        },
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/tasks/:name`**
    Get all tasks or create a new task. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "data": {
                "title": ...,
                "description": ...,
                "due_date": ...,
                "column_id": ...,
                "index": ...,
            },
        },
    }
    ```
    **Response**
    ```
    {
        "id": ...
    }
    ```
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    [
        {
            "model": ...,
            "pk": ...,
            "fields": {
                "title": ...,
                "description": ...,
                "due_date": ...,
                "column_id": ...,
                "index": ...,
                "event_group": ...
            }
        }
    ]
    ```

## **Upload**

- ### **`/upload/file/:name`**
    Upload file to database. </br>
    ### **POST**
    **Request**
    ```
    FormData keys: "identifier", "name", "file"
    {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
        body: FormData()
    }
    ```
    **Response**
    ```
    {
        "identifier": ...,
        "file": ...,
        "name": ...
    }
    ```

- ### **`/upload/image/:name`**
    Upload image to database. </br>
    ### **POST**
    **Request**
    ```
    FormData keys: "identifier", "name", "image"
    {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
        body: FormData()
    }
    ```
    **Response**
    ```
    {
        "identifier": ...,
        "image": ...,
        "name": ...
    }
    ```

- ### **`/upload/note/:name`**
    Upload note to database. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "identifier": ...,
            "total": ...,
            "title": ...,
            "text": ...,
        },
    }
    ```
    **Response**
    ```
    {
        "identifier": ...,
        "title": ...,
        "text": ...
    }
    ```

- ### **`/upload/get/file/:name`**
    Get all files for a specific event group. </br>
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    [
        {
            "model": ...,
            "pk": ...,
            "fields": {
                "identifier": ...,
                "name": ...,
                "file": ...,
                "group": ...,
                "created_date": ...
            }
        }
    ]
    ```

- ### **`/upload/get/image/:name`**
    Get all images for a specific event group. </br>
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    [
        {
            "model": ...,
            "pk": ...,
            "fields": {
                "identifier": ...,
                "name": ...,
                "image": ...,
                "group": ...,
                "created_date": ...
            }
        }
    ]
    ```

- ### **`/upload/get/note/:name`**
    Get all notes for a specific event group. </br>
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    [
        {
            "model": ...,
            "pk": ...,
            "fields": {
                "identifier": ...,
                "title": ...,
                "text": ...,
                "group": ...,
            }
        }
    ]
    ```

- ### **`/upload/delete/note/:name`**
    Delete a note. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "identifier": ...,
        },
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/upload/delete/files/:name`**
    Delete a file or image. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "identifier": ...,
        },
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/upload/get/totalnotes/`**
    Get the number of notes a user has created. </br>
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {
        "total": ...
    }
    ```

- ### **`/upload/get/totalfiles/`**
    Get the number of files and images a user has created. </br>
    ### **GET**
    **Request**
    ```
    {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    }
    ```
    **Response**
    ```
    {
        "total": ...
    }
    ```

## **Users**

- ### **`/users/create/`**
    Create a new account. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: {
            "email": ...,
            "username": ...,
            "password": ...,
        },
    }
    ```
    **Response**
    ```
    {
        "email": ...,
        "username": ...,
        "date_joined": ...
    }
    ```

- ### **`/users/login/`**
    Login to an account. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "email": ...,
            "password": ...,
        },
    }
    ```
    **Response**
    ```
    {
        "email": ...,
        "username": ...,
        "token": ...,
        "logout_time": ...,
        "avatar": ...
    }
    ```

- ### **`/users/update/`**
    Update user credentials. </br>
    ### **POST**
    **Request**
    ```
    FormData keys: "email", "username", "avatar", "password"
    {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
        body: FormData(),
    }
    ```
    **Response**
    ```
    {
        "username": ...,
        "avatar": ...
    }
    ```

- ### **`/users/activate/`**
    Activate an account. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "email": ...,
        },
    }
    ```
    **Response**
    ```
    {
        "email": ...,
        "username": ...,
        "token": ...,
        "logout_time": ...,
        "avatar": ...
    }
    ```

- ### **`/users/remember/`**
    Create reset password link. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: {
            "email": ...,
        },
    }
    ```
    **Response**
    ```
    {}
    ```

- ### **`/users/reset/`**
    Reset password of an account. </br>
    ### **POST**
    **Request**
    ```
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: {
            "email": ...,
            "password": ...,
        },
    }
    ```
    **Response**
    ```
    {}
    ```