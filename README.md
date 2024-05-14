# SimTracker

A web-based application used by healthcare simulationists to help keep track of inventory
and all sim related things.

!!! NOTICE !!! - THIS PROJECT IS A WORK-IN-PROGRESS AND SHOULD NOT BE CURRENTLY USED IN PRODUCTION.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Donate](#donate)

## Installation

Initial steps are as follows:

1. Clone repository.
2. Create a virtual environment using `python -m venv .venv` or your preferred method.
3. Activate your environment.
4. Install environment dependencies from the requirements.txt file by using `pip install -r requirements.txt`. Point to the proper path to the requirements.txt file as needed.
5. Create a .env file in the root directory of the project. "Same directory where the 'manage.py' file lives" and on the first line add `SECRET_KEY=myrandomesecretkey`.
6. Run migrations for the database: `python manage.py migrate`.
7. Create your superuser: `python manage.py createsuperuser`.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Donate
Bitcoin: [bc1q3whpjztrpw6hj8hhs8xen59r38g3ncs22emyce](bitcoin:bc1q3whpjztrpw6hj8hhs8xen59r38g3ncs22emyce?message=GitHub%20-%20SimTracker%20Project%20Donation)