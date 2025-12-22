from flask import Blueprint

# Import the blueprint so it can be used as `from app.main import main`
from .routes import main  # noqa: F401
