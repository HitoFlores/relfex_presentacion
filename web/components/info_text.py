import reflex as rx
import web.styles.styles as styles
from web.styles.colors import TextColors
from web.styles.colors import Colors

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.chakra.span(
            title,
            font_weigth="bold",
            color=Colors.PRIMARY.value
        ),
        f" {body}", font_size=styles.Size.MEDIUM.value, color=TextColors.BODY.value
    )