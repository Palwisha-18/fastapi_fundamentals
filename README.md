# Implementation of Car Sharing App using FastAPI

This Car Sharing app is built as part of the FastAPI Fundamentals Course on Pluralsight by Reindert-Jan Ekker.
The app includes several endpoint to add, edit and remove cars as well as add trips for each car.
All the data is stored in a database using mobile classes written using a library called SQLModel.
User authentication is added via OAuth2 and endpoints are tested using pytest.

### Learnings from the course:
- How to build a REST APIs with FastAPI
- Writing schemas using pydantic models and learnt about FastAPI's automatic data validation and conversion
- Integrating SQLModel
- Dealing with Session, APIRouter, Middleware, Headers and Cookies
- Adding OAuth2 authentication, serving HTML pages, and processing HTML form data
- Unit testing using pytest, TestClient and Mock
- Deployment using gunicorn and nginx