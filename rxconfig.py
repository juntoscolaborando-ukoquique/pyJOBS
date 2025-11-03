import reflex as rx
import os

config = rx.Config(
    app_name="job_organizer",
    backend_host="0.0.0.0",
    backend_port=int(os.getenv("PORT", "8000")),
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
