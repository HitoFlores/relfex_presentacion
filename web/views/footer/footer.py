import reflex as rx
import datetime
from web.styles.styles import Size, SizeInt
from web.styles.colors import TextColors, Colors
import web.components.constants as constants

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png", height=Size.XXBIG.value,
            width=Size.XXBIG.value, alt="Logitipo hitodev",
            border_radius="15px",
            border=f"2px solid {TextColors.BODY.value}",
        ),
        rx.link(
            f"© 2012-{datetime.date.today().year} HitoDev by Raúl Flores v2.",
            href=constants.LINKEDIN_URL, is_external=True,
            color=TextColors.FOOTER.value,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "CONSTRUYENDO SOFTWARE CON ♥ DESDE MI CASA HACIA EL MUNDO.", 
            font_size=Size.MEDIUM.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_left=Size.DEFAULT.value,
        padding_right=Size.DEFAULT.value,
        align="center",
        color=TextColors.FOOTER.value,
        spacing=SizeInt.ZERO.value
    )