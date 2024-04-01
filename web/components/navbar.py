import reflex as rx
import web.styles.styles as styles 
from web.styles.styles import Size
from web.styles.colors import Colors, TextColors

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.chakra.span(
                "hito", color=Colors.PRIMARY.value
            ),
            rx.chakra.span(
                "dev", color=Colors.SECONDARY.value
            ),
            style=styles.navbar_title_style
        ),
        position="sticky",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        bg=Colors.CONTENT.value,
        z_index="999",
        top="0"

    )