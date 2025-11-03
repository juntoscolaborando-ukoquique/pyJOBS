import reflex as rx
import os

# In production, both frontend and backend use the same PORT
port = int(os.getenv("PORT", "3000"))

config = rx.Config(
    app_name="job_organizer",
    frontend_port=port,
    backend_port=port,
    backend_host="0.0.0.0",
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
