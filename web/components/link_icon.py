import reflex as rx
from web.styles.styles import Size

def link_icon(alt: str, url: str, src: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=src,
            width=Size.LARGE.value,
            alt=alt
        ),
        href= url,
        is_external=True
    )