"""Portfolio Personal de Javier Curto - Desarrollador Backend Java Spring"""

import reflex as rx
from rxconfig import config
import os
from dotenv import load_dotenv
from datetime import datetime

# Cargar variables de entorno desde .env
load_dotenv()


import smtplib
from email.message import EmailMessage

# Configuración SMTP desde variables de entorno
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")


class State(rx.State):
    """The app state."""

    show_mobile_menu: bool = False
    show_success_modal: bool = False
    sending: bool = False
    error_message: str = ""

    def toggle_menu(self):
        """Toggle mobile menu visibility"""
        self.show_mobile_menu = not self.show_mobile_menu

    def close_menu(self):
        """Close mobile menu"""
        self.show_mobile_menu = False

    def close_modal(self):
        """Close success modal"""
        self.show_success_modal = False
        self.error_message = ""

    def handle_submit(self, form_data: dict):
        """Maneja el envío del formulario de contacto usando SMTP clásico"""
        self.sending = True
        self.error_message = ""

        try:
            if not SMTP_USER or not SMTP_PASS:
                raise Exception("SMTP_USER o SMTP_PASS no configurados en .env")

            # Obtener datos del formulario
            nombre = form_data.get("name", "").strip()
            email = form_data.get("email", "").strip()
            telefono = form_data.get("phone", "").strip()
            mensaje = form_data.get("message", "").strip()

            # Validaciones básicas
            if not nombre or not email or not mensaje:
                raise Exception("Por favor completa todos los campos obligatorios")

            # Preparar el email
            msg = EmailMessage()
            msg["From"] = SMTP_USER
            msg["To"] = "curto.brull.javier@jcurtobr.eu"
            msg["Subject"] = "Nuevo mensaje desde Portfolio Web"
            html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <style>
                        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                        .header {{ background-color: #d19617; color: white; padding: 20px; text-align: center; }}
                        .content {{ background-color: #f4f4f4; padding: 20px; margin-top: 20px; }}
                        .field {{ margin-bottom: 15px; }}
                        .field strong {{ color: #d19617; }}
                        .message-box {{ background-color: white; padding: 15px; border-left: 4px solid #d19617; margin-top: 10px; }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <h2>📧 Nuevo Mensaje de Contacto</h2>
                        </div>
                        <div class="content">
                            <div class="field">
                                <strong>Nombre:</strong> {nombre}
                            </div>
                            <div class="field">
                                <strong>Email:</strong> {email}
                            </div>
                            <div class="field">
                                <strong>Teléfono:</strong> {telefono if telefono else "No proporcionado"}
                            </div>
                            <div class="field">
                                <strong>Mensaje:</strong>
                                <div class="message-box">
                                    {mensaje.replace(chr(10), "<br>")}
                                </div>
                            </div>
                        </div>
                    </div>
                </body>
                </html>
            """
            msg.set_content("Este mensaje requiere un cliente compatible con HTML.")
            msg.add_alternative(html_content, subtype="html")

            # Enviar email usando SMTP
            # Puerto 465 usa SSL directo, 587 usa STARTTLS
            if SMTP_PORT == 465:
                with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
                    server.login(SMTP_USER, SMTP_PASS)
                    server.send_message(msg)
            else:
                with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                    server.starttls()
                    server.login(SMTP_USER, SMTP_PASS)
                    server.send_message(msg)

            # Éxito
            self.show_success_modal = True
            self.sending = False

        except Exception as e:
            # Error
            self.error_message = str(e)
            self.show_success_modal = True
            self.sending = False


def navbar() -> rx.Component:
    """Barra de navegación fija"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                # Logo
                rx.link(
                    rx.heading("Javier Curto", size="8", color="#d19617"),
                    href="#inicio",
                    on_click=State.close_menu,
                ),
                rx.spacer(),
                # Menú Desktop
                rx.hstack(
                    rx.link("INICIO", href="#inicio", class_name="nav-link"),
                    rx.link("SOBRE MÍ", href="#sobremi", class_name="nav-link"),
                    rx.link("SKILLS", href="#skills", class_name="nav-link"),
                    rx.link("CURRICULUM", href="#curriculum", class_name="nav-link"),
                    rx.link("PORTFOLIO", href="#portfolio", class_name="nav-link"),
                    rx.link("CONTACTO", href="#contacto", class_name="nav-link"),
                    spacing="6",
                    class_name="desktop-menu",
                ),
                # Botón hamburguesa (mobile)
                rx.button(
                    rx.icon("menu", size=28),
                    on_click=State.toggle_menu,
                    variant="ghost",
                    class_name="mobile-menu-button",
                ),
                width="100%",
                align="center",
            ),
            # Menú Mobile (desplegable)
            rx.cond(
                State.show_mobile_menu,
                rx.vstack(
                    rx.link(
                        "INICIO",
                        href="#inicio",
                        on_click=State.close_menu,
                        class_name="mobile-nav-link",
                    ),
                    rx.link(
                        "SOBRE MÍ",
                        href="#sobremi",
                        on_click=State.close_menu,
                        class_name="mobile-nav-link",
                    ),
                    rx.link(
                        "SKILLS",
                        href="#skills",
                        on_click=State.close_menu,
                        class_name="mobile-nav-link",
                    ),
                    rx.link(
                        "CURRICULUM",
                        href="#curriculum",
                        on_click=State.close_menu,
                        class_name="mobile-nav-link",
                    ),
                    rx.link(
                        "PORTFOLIO",
                        href="#portfolio",
                        on_click=State.close_menu,
                        class_name="mobile-nav-link",
                    ),
                    rx.link(
                        "CONTACTO",
                        href="#contacto",
                        on_click=State.close_menu,
                        class_name="mobile-nav-link",
                    ),
                    width="100%",
                    spacing="2",
                    padding="1rem",
                    class_name="mobile-menu",
                ),
            ),
            width="100%",
            padding_y="1rem",
            padding_x="2rem",
            spacing="0",
        ),
        position="fixed",
        top="0",
        width="100%",
        background="rgba(30, 35, 38, 0.95)",
        backdrop_filter="blur(10px)",
        z_index="1000",
        box_shadow="0 2px 10px rgba(0,0,0,0.3)",
    )


def inicio() -> rx.Component:
    """Sección de inicio con presentación"""
    return rx.box(
        rx.vstack(
            rx.image(
                src="/img/hero2.jpg",
                alt="Javier Curto",
                width="200px",
                height="200px",
                border_radius="50%",
                border="5px solid #d19617",
                object_fit="cover",
            ),
            rx.heading("JAVIER CURTO", size="9", color="white", text_align="center"),
            rx.text(
                "Desarrollador Backend", size="6", color="#d19617", text_align="center"
            ),
            rx.text("Python", size="5", color="#e5c507", text_align="center"),
            rx.text("Java Spring", size="5", color="#e5c507", text_align="center"),
            rx.hstack(
                rx.link(
                    rx.icon("linkedin", size=32, color="white"),
                    href="https://www.linkedin.com/in/javier-curto-brull/",
                    is_external=True,
                ),
                rx.link(
                    rx.icon("twitter", size=32, color="white"),
                    href="https://x.com/JavierCurtoB",
                    is_external=True,
                ),
                rx.link(
                    rx.icon("github", size=32, color="white"),
                    href="https://github.com/CurtoBrull",
                    is_external=True,
                ),
                spacing="5",
            ),
            spacing="5",
            align="center",
            justify="center",
            min_height="100vh",
            padding_top="80px",
            padding_x="2rem",
            width="100%",
        ),
        id="inicio",
        background="linear-gradient(135deg, #1e2326 0%, #252a2e 100%)",
        width="100%",
    )


def sobre_mi() -> rx.Component:
    """Sección Sobre Mí"""
    return rx.box(
        rx.vstack(
            rx.heading(
                "SOBRE MÍ",
                size="8",
                color="#d19617",
                margin_bottom="2rem",
                text_align="start",
            ),
            rx.box(
                rx.vstack(
                    # Texto descriptivo
                    rx.vstack(
                        rx.text(
                            "Soy Técnico Superior en Desarrollo de Aplicaciones Web (CFGS), "
                            "previamente obtuve el título de Técnico en Sistemas Microinformáticos y Redes (CFGM).",
                            color="white",
                            line_height="1.8",
                        ),
                        rx.text(
                            "Actualmente trabajo como Desarrollador Backend en NTT Data desde febrero de 2023, "
                            "donde desarrollo aplicaciones con Java y Spring Framework, integrando bases de datos como DB2, "
                            "Oracle y MongoDB, y creando APIs REST robustas.",
                            color="white",
                            line_height="1.8",
                        ),
                        rx.text(
                            'Estoy realizando el ',
                            rx.link(
                                'Curso de Especialización de "Desarrollo de Aplicaciones en Lenguaje Python"',
                                href="https://www.todofp.es/que-estudiar/familias-profesionales/informatica-comunicaciones/ce-lenguaje-phyton.html",
                                color="#d19617",
                                text_decoration="underline",
                                is_external=True,
                            ),
                            ' y quiero enfocar '
                            "mi carrera profesional hacia este lenguaje, ampliando mis habilidades en desarrollo backend "
                            "y explorando nuevas oportunidades en el ecosistema Python.",
                            color="white",
                            line_height="1.8",
                        ),
                        spacing="4",
                        width="80%",
                        align="start",
                        max_width="1400px",
                        margin="0 auto",
                    ),
                    # Grid de Datos Personales e Intereses
                    rx.grid(
                        # Datos Personales
                        rx.vstack(
                            rx.heading(
                                "Datos Personales",
                                size="6",
                                color="#d19617",
                                margin_bottom="1rem",
                            ),
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("mail", color="#d19617"),
                                    rx.text(
                                        "curto.brull.javier@jcurtobr.eu", color="white"
                                    ),
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.icon("globe", color="#d19617"),
                                    rx.link(
                                        "https://jcurtobr.eu/",
                                        href="https://jcurtobr.eu/",
                                        color="white",
                                        is_external=True,
                                    ),
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.icon("map-pin", color="#d19617"),
                                    rx.text("Huércal de Almería", color="white"),
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.icon("briefcase", color="#d19617"),
                                    rx.text("Desarrollador Backend", color="white"),
                                    spacing="2",
                                ),
                                spacing="4",
                                align="start",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        # Intereses
                        rx.vstack(
                            rx.heading(
                                "Intereses y Hobbies",
                                size="6",
                                color="#d19617",
                                margin_bottom="1rem",
                            ),
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("cpu", color="#d19617", size=24),
                                    rx.text("Informática", color="white"),
                                    spacing="3",
                                ),
                                rx.hstack(
                                    rx.icon("gamepad-2", color="#d19617", size=24),
                                    rx.text("Juegos", color="white"),
                                    spacing="3",
                                ),
                                rx.hstack(
                                    rx.icon("music", color="#d19617", size=24),
                                    rx.text("Música", color="white"),
                                    spacing="3",
                                ),
                                rx.hstack(
                                    rx.icon("dumbbell", color="#d19617", size=24),
                                    rx.text("Deporte", color="white"),
                                    spacing="3",
                                ),
                                spacing="4",
                                align="start",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        columns="2",
                        spacing="8",
                        width="100%",
                        margin_top="2rem",
                    ),
                    spacing="6",
                    width="100%",
                ),
                max_width="1400px",
                margin="0 auto",
            ),
            spacing="5",
            padding_y="4rem",
            padding_x="2rem",
            width="100%",
            align="center",
        ),
        id="sobremi",
        background="#1e2326",
        width="100%",
    )


def skills() -> rx.Component:
    """Sección de habilidades técnicas y profesionales"""
    return rx.box(
        rx.vstack(
            rx.heading(
                "SKILLS",
                size="8",
                color="#d19617",
                text_align="center",
            ),
            rx.box(
                rx.vstack(
                    # Texto descriptivo
                    rx.vstack(
                        rx.text(
                            "",
                        ),
                        spacing="4",
                        width="80%",
                        align="start",
                        max_width="1400px",
                    ),
                    rx.grid(
                        # Technical Skills
                        rx.vstack(
                            rx.heading(
                                "Technical Skills",
                                size="6",
                                color="#d19617",
                                margin_bottom="1rem",
                            ),
                            rx.vstack(
                                rx.text("• Java", color="white"),
                                rx.text("• Python", color="white"),
                                rx.text(
                                    "• Spring Framework / Spring Boot", color="white"
                                ),
                                rx.text("• Git / Github", color="white"),
                                rx.text("• SQL, DB2, Oracle", color="white"),
                                rx.text("• Thymeleaf, PL/SQL", color="white"),
                                rx.text("• MongoDB", color="white"),
                                rx.text("• Postman", color="white"),
                                rx.text(
                                    "• HTML, CSS, JavaScript, PHP, jQuery",
                                    color="white",
                                ),
                                spacing="2",
                                align="start",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        # Professional Skills
                        rx.vstack(
                            rx.heading(
                                "Professional Skills",
                                size="6",
                                color="#d19617",
                                margin_bottom="1rem",
                            ),
                            rx.vstack(
                                rx.text("• Comunicación", color="white"),
                                rx.text("• Trabajo en equipo", color="white"),
                                rx.text("• Dedicación", color="white"),
                                rx.text("• Gestión del tiempo", color="white"),
                                rx.text("• Resolución de problemas", color="white"),
                                rx.text("• Adaptabilidad", color="white"),
                                rx.text("• Autoaprendizaje", color="white"),
                                rx.text("• Desarrollo ágil (SCRUM)", color="white"),
                                spacing="2",
                                align="start",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        columns="2",
                        spacing="8",
                        width="100%",
                    ),
                    max_width="1400px",
                    margin="0 auto",
                ),
                spacing="5",
                padding_y="2rem",
                padding_x="2rem",
                width="100%",
                align="center",
            ),
            spacing="5",
            padding_y="4rem",
            padding_x="2rem",
            width="100%",
            align="center",
        ),
        id="skills",
        background="#252a2e",
        width="100%",
    )


def curriculum() -> rx.Component:
    """Sección de educación y experiencia laboral"""
    return rx.box(
        rx.vstack(
            rx.heading(
                "CURRICULUM",
                size="8",
                color="#d19617",
                text_align="center",
            ),
            rx.box(
                rx.vstack(
                    # Texto descriptivo
                    rx.vstack(
                        rx.text(
                            "",
                        ),
                        spacing="4",
                        width="80%",
                        align="start",
                        max_width="1400px",
                    ),
                    rx.grid(
                        # Educación
                        rx.vstack(
                            rx.heading(
                                "Educación",
                                size="6",
                                color="#d19617",
                                margin_bottom="1.5rem",
                            ),
                            rx.vstack(
                                rx.vstack(
                                    rx.text(
                                        "2020 - Actual", color="#d19617", weight="bold"
                                    ),
                                    rx.heading(
                                        "CFGS Desarrollo de Aplicaciones Web",
                                        size="5",
                                        color="white",
                                    ),
                                    rx.text("IES La Puebla", color="white"),
                                    spacing="1",
                                    align="start",
                                ),
                                rx.vstack(
                                    rx.text(
                                        "2018 - 2020", color="#d19617", weight="bold"
                                    ),
                                    rx.heading(
                                        "CFGM Técnico de Sistemas Microinformáticos y Redes",
                                        size="5",
                                        color="white",
                                    ),
                                    rx.text("IES La Puebla", color="white"),
                                    spacing="1",
                                    align="start",
                                ),
                                spacing="5",
                                align="start",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        # Experiencia
                        rx.vstack(
                            rx.heading(
                                "Experiencia",
                                size="6",
                                color="#d19617",
                                margin_bottom="1.5rem",
                            ),
                            rx.vstack(
                                rx.vstack(
                                    rx.text(
                                        "Feb 2023 - Actualidad",
                                        color="#d19617",
                                        weight="bold",
                                    ),
                                    rx.heading(
                                        "Desarrollador Backend Spring",
                                        size="5",
                                        color="white",
                                    ),
                                    rx.text("NTT Data", color="white"),
                                    rx.text(
                                        "Java • Spring • Programación Funcional • API REST • DB2 • Oracle • "
                                        "Thymeleaf • PL/SQL • MongoDB • SQL • Postman",
                                        color="white",
                                        size="2",
                                    ),
                                    spacing="1",
                                    align="start",
                                ),
                                rx.vstack(
                                    rx.text(
                                        "Oct - Dic 2022", color="#d19617", weight="bold"
                                    ),
                                    rx.heading(
                                        "Prácticas Desarrollador Backend",
                                        size="5",
                                        color="white",
                                    ),
                                    rx.text("NTT Data", color="white"),
                                    spacing="1",
                                    align="start",
                                ),
                                rx.vstack(
                                    rx.text(
                                        "1998 - Feb 2023", color="#d19617", weight="bold"
                                    ),
                                    rx.heading(
                                        "Militar Profesional", size="5", color="white"
                                    ),
                                    rx.text("Ministerio de Defensa", color="white"),
                                    spacing="1",
                                    align="start",
                                ),
                                spacing="5",
                                align="start",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        columns="2",
                        spacing="8",
                        width="100%",
                    ),
                    max_width="1400px",
                    margin="0 auto",
                ),
                spacing="5",
                padding_y="2rem",
                padding_x="2rem",
                width="100%",
                align="center",
            ),
            # Currículum Vitae - Botón de descarga
            rx.vstack(
                rx.heading(
                    "Currículum Vitae",
                    size="6",
                    color="#d19617",
                    margin_bottom="1rem",
                ),
                rx.link(
                    rx.button(
                        "Ver y Descargar CV",
                        size="3",
                        color_scheme="orange",
                    ),
                    href="/cv/CV_Javier_Curto_Brull.pdf",
                    is_external=True,
                ),
                spacing="4",
                align="center",
                width="100%",
                margin_top="2rem",
            ),
            spacing="5",
            padding_y="4rem",
            padding_x="2rem",
            width="100%",
            align="center",
        ),
        id="curriculum",
        background="#1e2326",
        width="100%",
    )


def project_card(
    title: str,
    description: str,
    image: str,
    tech: str,
    github_url: str = "",
    demo_url: str = "",
) -> rx.Component:
    """Tarjeta de proyecto individual"""
    return rx.box(
        rx.vstack(
            rx.image(
                src=image,
                alt=title,
                width="100%",
                height="200px",
                object_fit="cover",
                border_radius="8px 8px 0 0",
            ),
            rx.vstack(
                rx.heading(title, size="5", color="white"),
                rx.text(description, color="white", size="2"),
                rx.text(tech, color="#d19617", size="1"),
                rx.hstack(
                    rx.cond(
                        github_url != "",
                        rx.link(
                            rx.button("Ver Código", size="2", variant="outline"),
                            href=github_url,
                            is_external=True,
                        ),
                    ),
                    rx.cond(
                        demo_url != "",
                        rx.link(
                            rx.button("Ver Demo", size="2", color_scheme="orange"),
                            href=demo_url,
                            is_external=True,
                        ),
                    ),
                    spacing="2",
                ),
                spacing="2",
                padding="1rem",
                align="start",
            ),
            spacing="0",
        ),
        background="#1e2326",
        border_radius="8px",
        overflow="hidden",
        box_shadow="0 4px 6px rgba(0,0,0,0.3)",
        transition="transform 0.3s ease",
        _hover={"transform": "translateY(-5px)"},
    )


def portfolio() -> rx.Component:
    """Sección de portfolio con proyectos"""
    return rx.box(
        rx.vstack(
            rx.heading("PORTFOLIO", size="8", color="#d19617", margin_bottom="2rem"),
            rx.grid(
                project_card(
                    "Web Personal ASTRO",
                    "Web para mostrar proyectos, habilidades y datos de contacto",
                    "/img/webAstroJCB.webp",
                    "Astro • Tailwind CSS",
                    "https://github.com/CurtoBrull/AstroJCB",
                ),
                project_card(
                    "API Spring JPA",
                    "CRUD básico para gestionar productos",
                    "/img/API_SPRING.webp",
                    "Spring Boot • JPA • MySQL",
                    "https://github.com/CurtoBrull/API_SPRING",
                ),
                project_card(
                    "OAuth2 con Spring Security",
                    "Autenticación y autorización de usuarios",
                    "/img/postmanPOSTCode.png",
                    "Spring Security • OAuth2 • Spring Boot",
                    "https://github.com/CurtoBrull/OAuth2-Spring-Security",
                ),
                project_card(
                    "GitHub User Activity App",
                    "Buscar información de usuarios de GitHub. Render tarda un poco en despertar la app.",
                    "/img/GitHubUserDetails.png",
                    "Spring Boot • GitHub API",
                    "https://github.com/CurtoBrull/GithubApiSpring",
                    "https://githubapispring.onrender.com/",
                ),
                project_card(
                    "Inventario del Congelador",
                    "App para controlar productos del congelador",
                    "/img/inventario-congelador.jpg",
                    "Next.js • React • Supabase",
                    "https://github.com/CurtoBrull/inventario-congelador",
                    "https://congelador-inventario.vercel.app/",
                ),
                project_card(
                    "NoPokeForYou",
                    "App fullstack troll con Pokémon + Gemini AI. Render tarda un poco en despertar la app.",
                    "/img/nopokeforyou.png",
                    "React • Spring Boot • Gemini AI",
                    "https://github.com/CurtoBrull/NoPokeForYou",
                    "https://nopokeforyou-front.onrender.com/",
                ),
                project_card(
                    "Generador de Ideas Gemini",
                    "Genera ideas creativas usando IA Gemini. Render tarda un poco en despertar la app.",
                    "/img/generador-ideas-gemini.png",
                    "Python • Gradio • Gemini AI",
                    "https://github.com/CurtoBrull/generador-ideas-gemini",
                    "https://generador-ideas-gemini.onrender.com/",
                ),
                project_card(
                    "Grocery Ticket AI",
                    "Procesa tickets de compra con OCR + Gemini",
                    "/img/groceryticketai.png",
                    "Tesseract.js • Gemini API • Supabase",
                    "https://github.com/CurtoBrull/grocery-ticket-ai",
                    "https://grocery-ticket-ai.vercel.app/",
                ),
                columns="3",
                spacing="5",
                width="100%",
            ),
            spacing="5",
            padding_y="4rem",
            padding_x="2rem",
            width="100%",
        ),
        id="portfolio",
        background="#252a2e",
        width="100%",
    )


def contacto() -> rx.Component:
    """Sección de contacto con formulario"""
    return rx.box(
        rx.vstack(
            rx.heading(
                "CONTACTO",
                size="8",
                color="#d19617",
                text_align="center",
            ),
            rx.box(
                rx.vstack(
                    # Texto descriptivo (hidden, for width control)
                    rx.vstack(
                        rx.text(""),
                        spacing="4",
                        width="80%",
                        align="start",
                        max_width="1400px",
                    ),
                    rx.grid(
                        # Formulario
                        rx.form(
                            rx.vstack(
                                # Campos visibles
                                rx.input(
                                    placeholder="Nombre *",
                                    name="name",
                                    required=True,
                                    size="3",
                                    height="3rem",
                                    width="80%",
                                ),
                                rx.input(
                                    placeholder="Teléfono",
                                    name="phone",
                                    size="3",
                                    height="3rem",
                                    width="80%",
                                ),
                                rx.input(
                                    placeholder="Email *",
                                    name="email",
                                    type="email",
                                    required=True,
                                    size="3",
                                    height="3rem",
                                    width="80%",
                                ),
                                rx.text_area(
                                    placeholder="Mensaje *",
                                    name="message",
                                    required=True,
                                    rows="8",
                                    min_height="150px",
                                    width="80%",
                                ),
                                rx.button(
                                    rx.cond(
                                        State.sending,
                                        rx.text("Enviando..."),
                                        rx.text("Enviar Mensaje"),
                                    ),
                                    type="submit",
                                    size="3",
                                    color_scheme="orange",
                                    width="80%",
                                    disabled=State.sending,
                                ),
                                spacing="4",
                                width="100%",
                                align="center",
                            ),
                            on_submit=State.handle_submit,
                        ),
                        # Modal de confirmación
                        rx.dialog.root(
                            rx.dialog.content(
                                rx.dialog.title(
                                    rx.cond(
                                        State.error_message != "",
                                        "Error al Enviar",
                                        "Mensaje Enviado",
                                    ),
                                    color=rx.cond(
                                        State.error_message != "",
                                        "#e74c3c",
                                        "#d19617",
                                    ),
                                ),
                                rx.dialog.description(
                                    rx.cond(
                                        State.error_message != "",
                                        State.error_message,
                                        "Tu mensaje ha sido enviado correctamente. Te responderé lo antes posible.",
                                    ),
                                    size="2",
                                    margin_bottom="1rem",
                                ),
                                rx.flex(
                                    rx.dialog.close(
                                        rx.button(
                                            "Cerrar",
                                            color_scheme="orange",
                                            on_click=State.close_modal,
                                        ),
                                    ),
                                    spacing="3",
                                    margin_top="1rem",
                                    justify="end",
                                ),
                                style={"max_width": 450},
                            ),
                            open=State.show_success_modal,
                        ),
                        # Información de contacto
                        rx.vstack(
                            rx.heading(
                                "Información de Contacto",
                                size="6",
                                color="#d19617",
                                margin_bottom="1rem",
                            ),
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("user", color="#d19617", size=24),
                                    rx.text("Javier Curto Brull", color="white"),
                                    spacing="3",
                                    align="center",
                                ),
                                rx.hstack(
                                    rx.icon("map-pin", color="#d19617", size=24),
                                    rx.text("Huércal de Almería", color="white"),
                                    spacing="3",
                                    align="center",
                                ),
                                rx.hstack(
                                    rx.icon("mail", color="#d19617", size=24),
                                    rx.text("curto.brull.javier@jcurtobr.eu", color="white"),
                                    spacing="3",
                                    align="center",
                                ),
                                rx.hstack(
                                    rx.icon("linkedin", color="#d19617", size=24),
                                    rx.link(
                                        "linkedin.com/in/javier-curto-brull/",
                                        href="https://www.linkedin.com/in/javier-curto-brull/",
                                        color="white",
                                        is_external=True,
                                    ),
                                    spacing="3",
                                    align="center",
                                ),
                                spacing="4",
                                align="start",
                            ),
                            spacing="4",
                            align="center",
                        ),
                        columns="2",
                        spacing="8",
                        width="100%",
                    ),
                    max_width="1400px",
                    margin="0 auto",
                ),
                spacing="5",
                padding_y="2rem",
                padding_x="2rem",
                width="100%",
                align="center",
            ),
            spacing="5",
            padding_y="4rem",
            padding_x="2rem",
            width="100%",
            align="center",
        ),
        id="contacto",
        background="#1e2326",
        width="100%",
    )


def footer() -> rx.Component:
    """Pie de página"""
    return rx.box(
        rx.vstack(
            rx.link(
                rx.button(
                    rx.icon("arrow-up", size=24),
                    variant="ghost",
                    color="white",
                ),
                href="#inicio",
            ),
            rx.hstack(
                rx.link(
                    rx.icon("linkedin", size=28, color="white"),
                    href="https://www.linkedin.com/in/javier-curto-brull/",
                    is_external=True,
                ),
                rx.link(
                    rx.icon("twitter", size=28, color="white"),
                    href="https://twitter.com/CurtoBrull",
                    is_external=True,
                ),
                rx.link(
                    rx.icon("github", size=28, color="white"),
                    href="https://github.com/CurtoBrull",
                    is_external=True,
                ),
                spacing="5",
            ),
            rx.text(
                f"© Javier Curto Brull - {datetime.now().year}",
                color="white",
                size="2",
            ),
            rx.text(
                "Desarrollado con Reflex",
                color="#d19617",
                size="1",
            ),
            rx.link(
                rx.image(
                    src="/img/r_logo.svg",
                    alt="Reflex Logo",
                    height="20px",
                ),
                href="https://reflex.dev",
                is_external=True,
            ),
            spacing="4",
            align="center",
            padding_y="2rem",
            padding_x="2rem",
            width="100%",
        ),
        background="#252a2e",
        border_top="1px solid rgba(209, 150, 23, 0.3)",
        width="100%",
    )


def index() -> rx.Component:
    """Página principal con todas las secciones"""
    return rx.box(
        navbar(),
        inicio(),
        sobre_mi(),
        skills(),
        curriculum(),
        portfolio(),
        contacto(),
        footer(),
        background="#1e2326",
    )


# Estilos personalizados
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Righteous&family=Work+Sans:wght@300;400;600;700&display=swap",
        "/custom.css",
    ],
    style={
        "font_family": "'Work Sans', sans-serif",
        "scroll_behavior": "smooth",
    },
)


app.add_page(
    index,
    title="Javier Curto | Desarrollador Backend Java Python",
    description="Portfolio personal de Javier Curto - Desarrollador Backend Java Python",
)
