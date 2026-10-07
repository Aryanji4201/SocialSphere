# SocialSphere

SocialSphere is a Flask-based social platform designed to provide a foundation for building social networking features with user authentication, database-backed application logic, and a structured web application architecture.

## Overview

The project is built with **Python and Flask**, with SQLAlchemy handling database interaction and Flask-Login providing user session management.

Database migrations are handled through **Flask-Migrate/Alembic**, while PyMySQL provides MySQL database connectivity.

## Tech Stack

| Technology       | Purpose                                    |
| ---------------- | ------------------------------------------ |
| Python           | Core programming language                  |
| Flask            | Web application framework                  |
| Flask-Login      | User authentication and session management |
| Flask-SQLAlchemy | Database integration and ORM               |
| SQLAlchemy       | Database abstraction                       |
| Flask-Migrate    | Database migrations                        |
| Alembic          | Migration engine                           |
| PyMySQL          | MySQL database driver                      |
| Jinja2           | Server-side templating                     |
| python-dotenv    | Environment variable management            |

## Project Structure

```text
SocialSphere/
├── app/                # Main Flask application
├── migrations/         # Database migration files
├── manage.py           # Application management entry point
├── run.py              # Development server entry point
├── requirements.txt    # Python dependencies
└── .gitignore          # Git ignore rules
```

## Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3
* pip
* MySQL
* Git

### 1. Clone the repository

```bash
git clone https://github.com/Aryanji4201/SocialSphere.git
cd SocialSphere
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and configure the database/application settings required by the application.

Keep credentials and other secrets out of version control.

### 5. Set up the database

The project includes Flask-Migrate/Alembic migration support. After configuring the database, apply the available migrations using the project's Flask migration commands.

```bash
flask db upgrade
```

### 6. Run the application

```bash
python run.py
```

The Flask development server will start locally.

## Database & Migrations

SocialSphere uses **SQLAlchemy** for database interaction and **Flask-Migrate** for schema migrations.

Migration files are stored in:

```text
migrations/
```

After making model changes, migrations can be generated and applied with:

```bash
flask db migrate -m "Describe your changes"
flask db upgrade
```

## Development

The application entry point is exposed through `run.py`, which creates the Flask application and starts the development server.

The project also contains `manage.py` for Flask application management and database-related development workflows.

## Security

Environment-specific configuration and sensitive credentials should be stored in `.env` rather than committed to the repository.

The project also uses **Flask-Login** for managing authenticated user sessions.

## Contributing

Contributions and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the changes locally.
5. Commit your changes with a clear message.
6. Open a pull request.

## License

No license is currently specified in this repository.
