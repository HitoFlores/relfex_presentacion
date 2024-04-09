import reflex as rx
from web.components.title import title
from web.components.link_sponsor import link_sponsor
from web.styles.styles import SizeInt
import web.components.constants as constants

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboradores"),
        rx.hstack(
            link_sponsor("logo-musst-gray.svg", constants.MUSST_URL, "Logitipo de MUSST"),
            link_sponsor("logo-musst-gray.svg", constants.MUSST_URL, "Logitipo de MUSST"),
            spacing=SizeInt.EXTRABIG.value
        ),
        align_items="start",
        width="100%"
    )
