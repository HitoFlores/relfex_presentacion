import reflex as rx
from web.styles.styles import Size, title_style, SizeInt

def title(title: str) -> rx.Component:
    return rx.heading(
        title,
        style=title_style
    )

def title_header(title: str) -> rx.Component:
    return rx.heading(
        title,
        style=title_style,
        margin=Size.ZERO.value,
        padding=Size.ZERO.value, 
    )
