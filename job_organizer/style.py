"""
UI Styles for Job Organizer

This module centralizes the application's color palette and common styles
to ensure consistency and improve maintainability.
"""

# Color Palette for the Green Theme
class ThemeColors:
    BACKGROUND = "linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)"
    HEADER = "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    CARD_BACKGROUND = "rgba(255, 255, 255, 0.85)"
    FILTER_BACKGROUND = "rgba(255, 255, 255, 0.7)"
    EMPTY_STATE_BACKGROUND = "rgba(255, 255, 255, 0.6)"
    BORDER = "1px solid var(--green-3)"
    HOVER_BORDER = "var(--green-6)"

# Common Component Styles
base_card_style = {
    "border_radius": "lg",
    "width": "100%",
}

job_card_style = {
    **base_card_style,
    "padding": "1.25rem",
    "background": ThemeColors.CARD_BACKGROUND,
    "border": ThemeColors.BORDER,
    "_hover": {"box_shadow": "md", "border_color": ThemeColors.HOVER_BORDER},
}

filter_box_style = {
    **base_card_style,
    "padding": "1rem",
    "background": ThemeColors.FILTER_BACKGROUND,
    "border": ThemeColors.BORDER,
}

empty_state_style = {
    **base_card_style,
    "padding": "4rem",
    "background": ThemeColors.EMPTY_STATE_BACKGROUND,
    "border": ThemeColors.BORDER,
}
