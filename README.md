# django-email-login
A simple django app for registration of new user and sending an email to the user for email confirmation. 
The User model is CustomUser model which is a subclass of AbstractUser model.

## How to install
1. Download or clone this repository.

2. Create a virtual environment.
```
python3 -m venv env
```

3. Activate the virtual environment.
```
source env/bin/activate
```

4. Install the requirements.
```
pip install -r requirements.txt
```

5. Run migrations.
```
python manage.py makemigrations
python manage.py migrate
```

6. Finally, run the server.
```
python manage.py runserver
```
