# Project-Management-API
This is a Django REST API, the backend of a project management system.

## Setting up project
1. With python3.12.2 installed. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```
    OBS: You can use a `virtualenv` or `pyenv` to install the requirements if you want.

2. Install [postgresql 14](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart-pt) with the following configurations:
    ```
    user: postgres
    password: postgres
    database: project-management
    ```
    - If your postgres is already installed, just create a database named `project-management`.
        ```bash
        createdb project-management -U postgres
        ```
    OBS: If you want to use another database settings, you must create and change the database variables in `.env` file (copy it if from [.env.dev](./.env.dev) file).


3. Run the migrations:
    ```bash
    python manage.py makemigrations && python manage.py migrate
    ```

4. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

5. Check if everything is working
    ```bash
    python manage.py runserver
    ```
Go to [localhost:8000/admin](localhost:8000/admin) and check if it's working