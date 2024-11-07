# Expense_tracker
This is the problem link: https://roadmap.sh/projects/expense-tracker

Building an Expense Tracker API in Python is a great way to consolidate backend development skills. We can create a RESTful API using FastAPI (a modern and fast Python web framework) and SQLAlchemy as the ORM to interact with a database like SQLite. FastAPI also integrates well with JWT for authentication, and Pydantic for data validation.

## Project Structure

Create a project structure as follows:

    expense_tracker/
    ├── main.py                # Entry point for the FastAPI app
    ├── models.py              # Database models
    ├── schemas.py             # Pydantic schemas
    ├── database.py            # Database connection
    ├── auth.py                # JWT authentication helpers
    └── crud.py                # CRUD operations

## Running the API

Run the FastAPI app with `uvicorn`:

    uvicorn main:app --reload
    
This setup will get you a fully functional API that can be extended as per the requirements, including adding filters for expenses and more JWT authentication functionalities.
