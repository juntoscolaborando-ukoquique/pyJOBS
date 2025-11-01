"""
UI Components for Job Organizer
Reusable Reflex components
"""
import reflex as rx
from typing import Any
from .style import job_card_style, empty_state_style


def stat_card(title: str, value: Any, icon: str, color: str, bg_color: str) -> rx.Component:
    """Statistics card component with custom background"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(icon, size="6"),
                rx.vstack(
                    rx.text(title, size="2", color="gray.600"),
                    rx.heading(value, size="7", color=color),
                    spacing="1",
                    align="start",
                ),
                spacing="3",
            ),
            width="100%",
        ),
        padding="1.5rem",
        border_radius="lg",
        background=bg_color,
        border="1px solid var(--gray-4)",
        width="100%",
    )


def job_card(job: dict) -> rx.Component:
    """Job card component using centralized styles"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(job["title"], size="5", color="gray.800"),
                rx.badge(job["status"], color_scheme="blue", variant="soft"),
                justify="between",
                width="100%",
            ),
            rx.text(job["company"], weight="medium", size="3", color="gray.700"),
            rx.text(job["location"], size="2", color="gray.500"),
            rx.hstack(
                rx.badge(job["type"], size="1", variant="outline", color_scheme="gray"),
                rx.badge(f"Priority: {job['priority']}", size="1", variant="outline", color_scheme="gray"),
                spacing="2",
            ),
            spacing="2",
            align="start",
        ),
        **job_card_style
    )


def empty_state(message: str) -> rx.Component:
    """Empty state component using centralized styles"""
    return rx.box(
        rx.vstack(
            rx.text("🔍", size="8"),
            rx.heading("No jobs found", size="5", color="gray.700"),
            rx.text(message, color="gray.500"),
            spacing="2",
            align="center",
        ),
        **empty_state_style
    )
