# Creating a Django Project


## 1. Create a Virtual Environment (Recommended)
```bash
python -m venv env 
```


## 2. Activate Environment
#### Windows
```bash
env\Scripts\activate
```
#### Linux
```bash
source env/bin/activate  
```




## 3. Deactivate Environment
```bash
deactivate
```




## 4. Install Django and Others Importent package
```bash
pip install django
```
```bash
python -m pip install Pillow
```
```bash
python -m pip install requests
```
```bash
pip install django-extensions
```
```bash
pip install django-cleanup
```
```bash
pip install python-dotenv
```
```bash
python -m pip install django-environ
```




## 5. Create a New Django Project
```bash
django-admin startproject config .
```



## 6. Setup Django-Extensions
```bash
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```



## 7. Run the Development Server
```bash
python manage.py runserver
```



# PostgreSQL Setup with Django 

## 1. Install Required Packages
```bash
pip install psycopg2-binary  # PostgreSQL adapter for Python
# or for production:
pip install psycopg2
```

## 2. Update your .env file
```bash
# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=localhost
DB_PORT=5432

# Or as a single DATABASE_URL (recommended)
DATABASE_URL=postgres://myuser:mypassword@localhost:5432/mydatabase
```


## 3. Configure settings.py
```bash
DATABASES = {
    "default": {
        "ENGINE"   : "django.db.backends.postgresql",
        "NAME"     : DB_NAME,
        "USER"     : DB_USER,
        "PASSWORD" : DB_PASSWORD,
        "HOST"     : DB_HOST,
        "PORT"     : DB_PORT,
    }
}
```