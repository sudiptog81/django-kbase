# KBase

This is a knowledge base meant for listing articles built in Django.

## Quick Start

Clone this repository.

Change to the directory where you cloned the repsository.

Copy `.env.sample` to `.env` and enter a new secret key.

Run the following command to setup a virtual environment and install the requirements:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
```

Run migrations and create superuser for Django Admin.

```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py createsuperuser --username=admin
Email address: <your-email>
Password: *********
Password (again): *********
```

Run the application :)

```bash
python3 manage.py runserver
```

## Author

Sudipto Ghosh
(For NIT Kurukshetra)
