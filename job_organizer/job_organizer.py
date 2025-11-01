"""
Job Organizer - Reflex App (Refactored for Production)
Clean architecture with separated concerns for Render deployment
"""
import reflex as rx
from .config import setup_logging
from .state import AppState
from .pages import index

# Setup logging
setup_logging()

# Create the app
app = rx.App()
app.add_page(index, route="/", title="Job Organizer - Reflex")
