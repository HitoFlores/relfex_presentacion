import reflex as rx
from web.components.navbar import navbar
from web.views.header import header
from web.views.links import links
from web.views.footer import footer
from web.views.sponsor import sponsors
import web.components.constants as constants 
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
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={constants.ANALITIC_TAG}"),
        rx.script(
            """ window.dataLayer = window.dataLayer || [];
                function gtag(){dataLayer.push(arguments);}
                gtag('js', new Date());
                gtag('config', 'G-44LPX2S8E6');
            """
        )
    ]
)

title = "Hitodev | Desarrollo de Software"
description = """Hola, mi nombre es Raúl Flores y tengo más de 13 años de 
                experiencia desarrollando software."""
#preview="/metadata.png"
preview= "https://github.com/HitoFlores/relfex_presentacion/blob/master/assets/metadata.png"
app.add_page(
    index,
    image= preview,
    title= title,
    description= description,
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@hitomoon"},
    ]
)
