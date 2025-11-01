"""
Page layouts for Job Organizer
"""
import reflex as rx
from .state import AppState
from .components import stat_card, job_card, empty_state
from .style import ThemeColors, filter_box_style


def dashboard_section() -> rx.Component:
    """Dashboard with statistics"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading("Dashboard", size="7", color="gray.800"),
                rx.button(
                    "🔄 Refresh Stats",
                    on_click=AppState.fetch_stats,
                    color_scheme="blue",
                    size="2",
                ),
                justify="between",
                width="100%",
            ),
            rx.cond(
                AppState.total_jobs > 0,
                rx.vstack(
                    rx.grid(
                        stat_card("Total Jobs", AppState.total_jobs, "📊", "blue.600", "blue.50"),
                        stat_card("Wishlist", AppState.status_counts.get("WISHLIST", 0), "⭐", "purple.600", "purple.50"),
                        stat_card("Active", AppState.status_counts.get("ACTIVE", 0), "🚀", "green.600", "green.50"),
                        stat_card("Applied", AppState.status_counts.get("APPLIED", 0), "📝", "orange.600", "orange.50"),
                        columns="4",
                        spacing="4",
                        width="100%",
                    ),
                    spacing="4",
                    width="100%",
                ),
                rx.text("Click 'Refresh Stats' to load dashboard data", size="2", color="gray.600"),
            ),
            spacing="4",
            width="100%",
        ),
        padding="2rem",
        background="transparent",  # Remove harsh white background
        border_radius="xl",
        box_shadow="sm",
        width="100%",
    )


def jobs_section() -> rx.Component:
    """Jobs list section with filters"""
    return rx.box(
        rx.vstack(
            # Header with Load button
            rx.hstack(
                rx.heading("Job List", size="6", color="gray.800"),
                rx.button(
                    "📋 Load All Jobs",
                    on_click=[AppState.clear_filters, AppState.fetch_jobs],
                    color_scheme="green",
                    size="2",
                ),
                justify="between",
                width="100%",
            ),
            
            # Filters
            rx.box(
                rx.hstack(
                    rx.vstack(
                        rx.text("Status", size="2", weight="medium", color="gray.700"),
                        rx.select(
                            ["ALL", "WISHLIST", "APPLIED", "INTERVIEW", "ACTIVE", "ALPHA", "POTENTIAL"],
                            placeholder="Filter by status",
                            on_change=lambda value: AppState.set_status_filter(value),
                            size="2",
                        ),
                        spacing="1",
                        align="start",
                    ),
                    rx.vstack(
                        rx.text("Priority", size="2", weight="medium", color="gray.700"),
                        rx.select(
                            ["ALL", "HIGH", "MEDIUM", "LOW"],
                            placeholder="Filter by priority",
                            on_change=lambda value: AppState.set_priority_filter(value),
                            size="2",
                        ),
                        spacing="1",
                        align="start",
                    ),
                    rx.button(
                        "🔄 Apply Filters",
                        on_click=AppState.fetch_jobs,
                        color_scheme="blue",
                        size="2",
                    ),
                    rx.button(
                        "✖ Clear",
                        on_click=[AppState.clear_filters, AppState.fetch_jobs],
                        color_scheme="gray",
                        variant="soft",
                        size="2",
                    ),
                    spacing="4",
                    width="100%",
                ),
                **filter_box_style
            ),
            
            # Job list
            rx.cond(
                AppState.jobs_loaded,
                rx.vstack(
                    rx.text(
                        "Showing ",
                        rx.text(AppState.jobs.length(), as_="span", weight="bold", color="gray.800"),
                        " jobs",
                        size="2",
                        color="gray.600",
                    ),
                    rx.cond(
                        AppState.jobs.length() > 0,
                        rx.vstack(
                            rx.foreach(AppState.jobs, job_card),
                            spacing="3",
                            width="100%",
                        ),
                        empty_state("Try adjusting your filters or click 'Clear' to see all jobs"),
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.text("Click 'Load Jobs' to fetch jobs from the database", size="2", color="gray.600"),
            ),
            spacing="4",
            width="100%",
        ),
        padding="2rem",
        background="transparent",  # Remove harsh white background
        border_radius="xl",
        box_shadow="sm",
        width="100%",
        margin_top="2rem",
    )


def index() -> rx.Component:
    """Main page layout"""
    return rx.box(
        rx.container(
            rx.vstack(
                # Header
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Job Organizer",
                            size="9",
                            color="white",
                        ),
                        rx.text(
                            "Pure Python Full-Stack Application with Reflex",
                            size="3",
                            color="gray.300",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    width="100%",
                    padding="3rem",
                    background=ThemeColors.HEADER,
                    border_radius="xl",
                    margin_bottom="2rem",
                ),
                
                # Dashboard Section
                dashboard_section(),
                
                # Jobs List Section
                jobs_section(),
                
                # Footer
                rx.box(
                    rx.text(
                        "Built with Python & Reflex",
                        size="2",
                        color="gray.500",
                        align="center",
                    ),
                    width="100%",
                    margin_top="4rem",
                    padding_y="2rem",
                ),
                
                spacing="6",
                width="100%",
                max_width="1200px",
                margin_y="2rem",
            ),
            center_content=True,
        ),
        background=ThemeColors.BACKGROUND,
        min_height="100vh",
    )
