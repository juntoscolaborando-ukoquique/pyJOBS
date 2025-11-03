import reflex as rx
import os

config = rx.Config(
    app_name="job_organizer",
    frontend_port=int(os.getenv("PORT", "3000")),
    backend_port=int(os.getenv("BACKEND_PORT", "8001")),
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
