import reflex as rx
from web.components.link_icon import link_icon
from web.components.info_text import info_text
from web.components.title import title_header
import web.components.constants as constants
from web.styles.styles import SizeInt, Size, Fonts
from web.styles.colors import TextColors, Colors

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="avatar_hito", src="avatar.png", 
                size=SizeInt.BIG.value, padding="3px",
                border="4px", border_color=Colors.PRIMARY.value,
                radius="full", fallback="RF",
                color_scheme="jade", variant="solid",
                margin=Size.SMALL.value
            ),
            rx.vstack(
                title_header(
                    "Raul Flores"
                ),
                rx.text(
                    "@HitoMoon", size=SizeInt.SMALL.value, 
                    margin=Size.ZERO.value, padding=Size.ZERO.value, 
                    color=TextColors.BODY.value
                ),
                rx.hstack(
                    link_icon("LinkedIn", constants.LINKEDIN_URL, "/icons/linkedin.svg"),
                    link_icon("Twitch", constants.TWITCH_URL, "/icons/twitch.svg"),
                    link_icon("Youtube", constants.YOUTUBE_URL, "/icons/youtube.svg"),
                    link_icon("Instagram", constants.INTAGRAM_URL, "/icons/instagram.svg"),
                    link_icon("Discord", constants.DISCORD_URL, "/icons/discord.svg"),
                    link_icon("Telegram", constants.TELEGRAM_URL, "/icons/telegram.svg"),
                    margin_top=Size.SMALL.value,
                    spacing="3"
                ),
                align_items="start",
                width="100%",
                spacing=SizeInt.ZERO.value
            ),
            width="100%",
            spacing=SizeInt.DEFAULT.value
        ),
        rx.flex(
                info_text("12", "años de experiencia"),
                rx.spacer(),
                info_text("Lenguajes", "Java -- Kotlin -- Python"),
                rx.spacer(),
                info_text("Puesto", "FullStack Developer"),
                width="100%"
        ),
        rx.text("""
                Watashi wa your father... Deberias de estar haciendo algo mejor 
                que estar perdiendo tu tiempo en esta pagina web, ponte a estudiar,
                cocinar, meditar o mejor aun, ya muerete, de seguro no le haces
                bien a nadie...
                """,
                color=TextColors.BODY.value,
                font_size=Size.DEFAULT.value,
                text_align="justify"
        ),
        spacing="3"
    )