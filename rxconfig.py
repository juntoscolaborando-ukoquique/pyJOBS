import reflex as rx
import os

config = rx.Config(
    app_name="job_organizer",
    frontend_port=3000,
    backend_port=int(os.getenv("PORT", "8001")),
)
