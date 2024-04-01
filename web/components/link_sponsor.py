import reflex as rx
import web.styles.styles as style
from web.styles.styles import Size, SizeInt

def link_sponsor(img: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            heigth=Size.XXBIG.value,
            weigth="auto",
            src=img,
            alt=alt
        ),
        href=url,
        is_external=True
    )