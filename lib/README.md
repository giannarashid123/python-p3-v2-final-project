# Language Learning CLI App

This is a simple command-line application that allows users to sign up, log in, update their email, and delete their accounts while tracking language learning progress. The app is built with Python and uses SQLAlchemy ORM for database management along with Alembic to handle database migrations. The CLI design cleanly separates menu-driven scripted elements from core functions, with each feature implemented as a dedicated function. User inputs are validated to ensure data integrity, such as checking for existing usernames and confirming actions like account deletion. Throughout the application, clear and detailed prompts guide the user, providing friendly feedback and instructions. The project utilizes Python data structures such as dictionaries (via SQLAlchemy query filters) and lists to manage and display collections of data, ensuring smooth and organized CLI interactions. To get started, clone the repository, create and activate a virtual environment (`python3 -m venv venv`), install dependencies using `pip install -r requirements.txt`, and run database migrations with `alembic upgrade head` to set up the database schema. Launch the app by running `python lib/cli.py` and follow the interactive prompts to navigate available options. Overall, this application demonstrates best practices in CLI design, effective use of data structures, and clean separation of concerns, resulting in a maintainable and user-friendly Python CLI tool.

## Setup & Installation

Clone the repository, then create and activate a virtual environment:

```bash
git clone <your-repo-url>
cd python-p3-v2-final-project
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
