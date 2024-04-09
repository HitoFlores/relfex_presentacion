import reflex as rx
from web.components.link_button import link_button
from web.components.title import title
import web.components.constants as constants


def links() -> rx.Component:
    return rx.vstack(
        title("Social"),
        link_button("LinkedIn", "Mi perfil publico profesional", constants.LINKEDIN_URL, "/icons/linkedin.svg"),
        link_button("Twitch", "Entretenimiento personal via streaming", constants.TWITCH_URL, "/icons/twitch.svg"),
        link_button("Youtube", "Videos que pueden ser interesantes", constants.YOUTUBE_URL, "/icons/youtube.svg"),
        link_button("Instagram", "Publicaciones de temas interesantes", constants.INTAGRAM_URL, "/icons/instagram.svg"),
        title("Contacto"),
        link_button("My Public Inbox", "Respuesta rapida y con preferencia", constants.PUBLICINBOX_URL, "/icons/inbox.svg"),
        link_button("Email", constants.EMAIL_URL, f"mailto:{constants.EMAIL_URL}", "/icons/mail.svg"),
        link_button("Discord", "Para reuniones más profesionales", constants.DISCORD_URL, "/icons/discord.svg"),
        link_button("Telegram", "Para mensajes más casuales", constants.TELEGRAM_URL, "/icons/telegram.svg"),
        width="100%",
        spacing="3"
    )