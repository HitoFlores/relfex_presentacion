import reflex as rx
from enum import Enum
from .colors import Colors as Color
from .colors import TextColors as TextColors
from .fonts import Fonts as Fonts, FontWeigth

MAX_WIDTH="600PX"

STYKESHEETS = [
    "https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@200;400&display=swap",
    "https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100..900;1,100..900&family=Noto+Serif+JP&display=swap",
    "https://fonts.googleapis.com/css2?family=Noto+Sans+Mono:wght@100..900&family=Noto+Sans:ital,wght@0,100..900;1,100..900&family=Noto+Serif+JP&display=swap"
]

class Size(Enum):
    ZERO="0px !important"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    XBIG="3em"
    XXBIG="4em"

class SizeInt(Enum):
    ZERO="0"
    VERYSAMLL="1"
    SMALL="2"
    DEFAULT="4"
    BIG="6"
    EXTRABIG="9"

BASE_STYLE= {
    "background_color": Color.BACKGROUND.value,
    "font_family": Fonts.DEFAULT.value,
    "font_weigth": FontWeigth.VERYLIGTH.value,
    rx.heading: {
        "color" : TextColors.HEADER.value,
        "font_family":Fonts.TITLE.value,
        "font_weigth": FontWeigth.VERYLIGTH.value
    },
    rx.button: {
        "width" : "100%",
        "height" : "100%",
        "paddin" : Size.SMALL.value,
        #"display" : "block",
        "border_radius" :Size.DEFAULT.value,
        "color": TextColors.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space":"normal",
        "text_align":"start",
        "_hover":{
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.link: {
        "text_decoration" : "none",
        "_hover" : {}
    }
}

title_style = dict(
    weight="100%",
    font_size=Size.LARGE.value,
    padding_top=Size.DEFAULT.value,
)

navbar_title_style = dict(
    font_family=Fonts.LOGO.value,
    font_weigth= FontWeigth.LIGTH.value,
    font_size=Size.LARGE.value
)

button_title_style = dict(
    font_family=Fonts.TITLE.value,
    font_weigth= FontWeigth.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    color= TextColors.HEADER.value,
)

button_body_style = dict(
    font_family=Fonts.DEFAULT.value,
    font_weigth= FontWeigth.VERYLIGTH.value,
    font_size=Size.MEDIUM.value,
    color= TextColors.BODY.value,
)