Get Started
1. Create a Virtual Environment:
    ```
    # Windows
    python -m venv venv
    # Linux|MacOS
    python3 -m venv venv
    ```
2. Activate the Virtual Environment:
    ```
    # Windows
    .\venv\Scripts\activate
    # Linux|MacOS
    source ./venv/bin/activate
    ```
3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```
4. Edit the `.env` file
5. Run the migrations:
    ```
    python manage.py makemigrations
    ```
6. Run the server:
    ```
    python manage.py runserver
    ```
    Or build the Docker image and run it:
    ```
    docker build -t django-api .
    docker run -p 8000:80 django-api
    ```
