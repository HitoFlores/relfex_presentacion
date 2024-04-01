import reflex as rx
import web.styles.styles as style
from web.styles.styles import Size, SizeInt

def link_button(title: str, body: str, url: str, icon: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=icon,
                    width=Size.LARGE.value,
                    heigth=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(
                        title, style=style.button_title_style
                    ),
                    rx.text(
                        body, style=style.button_body_style
                    ),
                    align_items="start",
                    spacing=SizeInt.ZERO.value,
                    margin=SizeInt.ZERO.value,
                    padding_y=SizeInt.SMALL.value,
                    paddin=SizeInt.SMALL.value
                ),
                width="100%",
                spacing=SizeInt.SMALL.value,
                margin_top=Size.SMALL.value,
                margin_bottom=Size.SMALL.value
            )
        ),
        href= url,
        is_external=True,
        width="100%",
        text_decoration="none"
    )

