import reflex as rx
from web.components.navbar import navbar
from web.views.header.header import header
from web.views.links.links import links
from web.views.footer.footer import footer
from web.views.sponsors.sponsor import sponsors
import web.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width = styles.MAX_WIDTH,
                align = "center",
                margin_y = styles.Size.DEFAULT.value,
                padding=styles.Size.BIG.value
            ),
        ),
        footer()
    )

app  = rx.App(
    stylesheets=styles.STYKESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    image="/metadata.png",
    title="Hitodev | Desarrollo de Software",
    description="""Hola, mi nombre es Raúl Flores y tengo más de 13 años de 
                    experiencia desarrollando software."""
)
app.compile