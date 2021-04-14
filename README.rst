REST_HospitalRegister
=======================

**REST_HospitalRegister** provides backend functionality for HospitalRegester project.

Meta
----

Author:
    Hristo Todev

Status:
    in development

Django Version:
    2.1.15

Python Version:
    3.8

Usage
-----

How to activate venv and install package requirements
======================================================

::

    > install python 3.8

    > python -m {PATH_TO_VENV_FOLDER}

    > <PATH_TO_VENV_FOLDER>\Scripts\activate

    > pip install -r requirements.txt

    * (Windows)


    $ sudo apt-get install python3.8

    $ virtualenv --python=/usr/bin/python3.8 ${PATH_TO_VENV}

    $ source ${PATH_TO_VENV}/bin/activate

    $ pip install -r requirements.txt

    * (Linux)

---------------------------------------------

Urls
======================================================

::

    hospital_units(public)
    # /patients/
    # /accounts/all/

    Authentication
        # /accounts/register/
        # /accounts/login/
        # /accounts/profile/
        # /accounts/verify-registration/
        # /accounts/reset-password/
        # /accounts/logout/
        # /accounts/change-password/

    Enrollment(authenticated)
        # /enrollments/
        # /enrollments/<int:pk>/

    Administration
        # /Smudge/


How to load dummy data from fixtures.
======================================================

::

    $ python manage.py loaddata ./project_apps/*/fixtures/test/*.json