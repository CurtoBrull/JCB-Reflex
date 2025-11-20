"""Portfolio Personal de Javier Curto - Desarrollador Backend Java Spring"""

import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""
    show_mobile_menu: bool = False

    def toggle_menu(self):
        """Toggle mobile menu visibility"""
        self.show_mobile_menu = not self.show_mobile_menu

    def close_menu(self):
        """Close mobile menu"""
        self.show_mobile_menu = False


def navbar() -> rx.Component:
    """Barra de navegación fija"""
    return rx.box(
        rx.container(
            rx.hstack(
                # Logo
                rx.link(
                    rx.heading("JCB", size="8", color="#d19617"),
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
                    rx.link("INICIO", href="#inicio", on_click=State.close_menu, class_name="mobile-nav-link"),
                    rx.link("SOBRE MÍ", href="#sobremi", on_click=State.close_menu, class_name="mobile-nav-link"),
                    rx.link("SKILLS", href="#skills", on_click=State.close_menu, class_name="mobile-nav-link"),
                    rx.link("CURRICULUM", href="#curriculum", on_click=State.close_menu, class_name="mobile-nav-link"),
                    rx.link("PORTFOLIO", href="#portfolio", on_click=State.close_menu, class_name="mobile-nav-link"),
                    rx.link("CONTACTO", href="#contacto", on_click=State.close_menu, class_name="mobile-nav-link"),
                    width="100%",
                    spacing="2",
                    padding="1rem",
                    class_name="mobile-menu",
                ),
            ),
            size="4",
        ),
        position="fixed",
        top="0",
        width="100%",
        background="rgba(30, 35, 38, 0.95)",
        backdrop_filter="blur(10px)",
        z_index="1000",
        padding="1rem 0",
        box_shadow="0 2px 10px rgba(0,0,0,0.3)",
    )


def inicio() -> rx.Component:
    """Sección de inicio con presentación"""
    return rx.box(
        rx.container(
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
                rx.text("Desarrollador Backend", size="6", color="#d19617", text_align="center"),
                rx.text("Java Spring", size="5", color="#e5c507", text_align="center"),
                rx.hstack(
                    rx.link(
                        rx.icon("linkedin", size=32, color="white"),
                        href="https://www.linkedin.com/in/javier-curto-brull/",
                        is_external=True,
                    ),
                    rx.link(
                        rx.icon("twitter", size=32, color="white"),
                        href="https://twitter.com/CurtoBrull",
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
            ),
            size="4",
        ),
        id="inicio",
        background="linear-gradient(135deg, #1e2326 0%, #252a2e 100%)",
    )


def sobre_mi() -> rx.Component:
    """Sección Sobre Mí"""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading("SOBRE MÍ", size="8", color="#d19617", margin_bottom="2rem"),
                rx.grid(
                    # Columna izquierda - Texto
                    rx.vstack(
                        rx.text(
                            "Soy Técnico Superior en Desarrollo de Aplicaciones Web (CFGS) graduado en IES La Puebla. "
                            "Previamente obtuve el título de Técnico de Sistemas Microinformáticos y Redes (CFGM).",
                            color="white",
                            line_height="1.8",
                        ),
                        rx.text(
                            "Actualmente trabajo como Desarrollador Backend en NTT Data desde febrero de 2023, "
                            "donde desarrollo aplicaciones con Java Spring Framework, trabajando con bases de datos DB2, "
                            "Oracle y MongoDB, y creando APIs REST.",
                            color="white",
                            line_height="1.8",
                        ),
                        rx.heading("Datos Personales", size="6", color="#d19617", margin_top="1.5rem"),
                        rx.vstack(
                            rx.hstack(
                                rx.icon("mail", color="#d19617"),
                                rx.text("curto.brull.javier@jcurtobr.eu", color="white"),
                                spacing="2",
                            ),
                            rx.hstack(
                                rx.icon("globe", color="#d19617"),
                                rx.link("https://jcurtobr.eu/", href="https://jcurtobr.eu/", color="white", is_external=True),
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
                            spacing="3",
                            align="start",
                        ),
                        spacing="4",
                        align="start",
                    ),
                    # Columna derecha - Intereses
                    rx.vstack(
                        rx.heading("Intereses", size="6", color="#d19617"),
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
                        rx.link(
                            rx.button(
                                "Ver y Descargar CV",
                                size="3",
                                color_scheme="orange",
                            ),
                            href="/cv/CV_Javier_Curto_Brull.pdf",
                            is_external=True,
                            margin_top="2rem",
                        ),
                        spacing="4",
                        align="start",
                    ),
                    columns="2",
                    spacing="6",
                    width="100%",
                ),
                spacing="5",
                padding="4rem 0",
            ),
            size="4",
        ),
        id="sobremi",
        background="#1e2326",
    )


def skills() -> rx.Component:
    """Sección de habilidades técnicas y profesionales"""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading("SKILLS", size="8", color="#d19617", margin_bottom="2rem"),
                rx.grid(
                    # Technical Skills
                    rx.vstack(
                        rx.heading("Technical Skills", size="6", color="#d19617", margin_bottom="1rem"),
                        rx.vstack(
                            rx.text("• Java (lenguaje principal)", color="white"),
                            rx.text("• Spring Framework / Spring Boot", color="white"),
                            rx.text("• Git / Github", color="white"),
                            rx.text("• SQL, DB2, Oracle", color="white"),
                            rx.text("• Thymeleaf, PL/SQL", color="white"),
                            rx.text("• MongoDB", color="white"),
                            rx.text("• Postman", color="white"),
                            rx.text("• HTML, CSS, JavaScript, PHP, jQuery", color="white"),
                            spacing="2",
                            align="start",
                        ),
                        spacing="4",
                        align="start",
                    ),
                    # Professional Skills
                    rx.vstack(
                        rx.heading("Professional Skills", size="6", color="#d19617", margin_bottom="1rem"),
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
                        align="start",
                    ),
                    columns="2",
                    spacing="6",
                    width="100%",
                ),
                spacing="5",
                padding="4rem 0",
            ),
            size="4",
        ),
        id="skills",
        background="#252a2e",
    )


def curriculum() -> rx.Component:
    """Sección de educación y experiencia laboral"""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading("CURRICULUM", size="8", color="#d19617", margin_bottom="2rem"),
                rx.grid(
                    # Educación
                    rx.vstack(
                        rx.heading("Educación", size="6", color="#d19617", margin_bottom="1.5rem"),
                        rx.vstack(
                            rx.vstack(
                                rx.text("2020 - Actual", color="#d19617", weight="bold"),
                                rx.heading("CFGS Desarrollo de Aplicaciones Web", size="5", color="white"),
                                rx.text("IES La Puebla", color="white"),
                                spacing="1",
                                align="start",
                            ),
                            rx.vstack(
                                rx.text("2018 - 2020", color="#d19617", weight="bold"),
                                rx.heading("CFGM Técnico de Sistemas Microinformáticos y Redes", size="5", color="white"),
                                rx.text("IES La Puebla", color="white"),
                                spacing="1",
                                align="start",
                            ),
                            spacing="5",
                            align="start",
                        ),
                        spacing="4",
                        align="start",
                    ),
                    # Experiencia
                    rx.vstack(
                        rx.heading("Experiencia", size="6", color="#d19617", margin_bottom="1.5rem"),
                        rx.vstack(
                            rx.vstack(
                                rx.text("Feb 2023 - Actualidad", color="#d19617", weight="bold"),
                                rx.heading("Desarrollador Backend Spring", size="5", color="white"),
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
                                rx.text("Oct - Dic 2022", color="#d19617", weight="bold"),
                                rx.heading("Prácticas Desarrollador Backend", size="5", color="white"),
                                rx.text("NTT Data", color="white"),
                                spacing="1",
                                align="start",
                            ),
                            rx.vstack(
                                rx.text("1998 - Feb 2023", color="#d19617", weight="bold"),
                                rx.heading("Militar Profesional", size="5", color="white"),
                                rx.text("Ministerio de Defensa", color="white"),
                                spacing="1",
                                align="start",
                            ),
                            spacing="5",
                            align="start",
                        ),
                        spacing="4",
                        align="start",
                    ),
                    columns="2",
                    spacing="6",
                    width="100%",
                ),
                spacing="5",
                padding="4rem 0",
            ),
            size="4",
        ),
        id="curriculum",
        background="#1e2326",
    )


def project_card(title: str, description: str, image: str, tech: str, github_url: str = "", demo_url: str = "") -> rx.Component:
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
        rx.container(
            rx.vstack(
                rx.heading("PORTFOLIO", size="8", color="#d19617", margin_bottom="2rem"),
                rx.grid(
                    project_card(
                        "Web Personal ASTRO",
                        "Web para mostrar proyectos, habilidades y datos de contacto",
                        "/img/webAstroJCB.webp",
                        "Astro • Tailwind CSS",
                        "https://github.com/CurtoBrull/AstroJCB",
                        "https://jcurtobr.eu/",
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
                        "Buscar información de usuarios de GitHub",
                        "/img/GitHubUserDetails.png",
                        "Spring Boot • GitHub API",
                        "https://github.com/CurtoBrull/GitHubUserActivity",
                        "https://githubuseractivity-5ys6.onrender.com/",
                    ),
                    project_card(
                        "Inventario del Congelador",
                        "App para controlar productos del congelador",
                        "/img/inventario-congelador.jpg",
                        "Next.js • React • Supabase",
                        "https://github.com/CurtoBrull/inventario-congelador",
                        "https://inventario-congelador.vercel.app/",
                    ),
                    project_card(
                        "NoPokeForYou",
                        "App fullstack troll con Pokémon + Gemini AI",
                        "/img/nopokeforyou.png",
                        "React • Spring Boot • Gemini AI",
                        "https://github.com/CurtoBrull/NoPokeForYou",
                        "https://nopokeforyou.onrender.com/",
                    ),
                    project_card(
                        "Generador de Ideas Gemini",
                        "Genera ideas creativas usando IA Gemini",
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
                padding="4rem 0",
            ),
            size="4",
        ),
        id="portfolio",
        background="#252a2e",
    )


def contacto() -> rx.Component:
    """Sección de contacto con formulario"""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading("CONTACTO", size="8", color="#d19617", margin_bottom="2rem"),
                rx.grid(
                    # Formulario
                    rx.form(
                        rx.vstack(
                            rx.input(
                                placeholder="Nombre *",
                                name="name",
                                required=True,
                                size="3",
                            ),
                            rx.input(
                                placeholder="Teléfono",
                                name="phone",
                                size="3",
                            ),
                            rx.input(
                                placeholder="Email *",
                                name="email",
                                type="email",
                                required=True,
                                size="3",
                            ),
                            rx.text_area(
                                placeholder="Mensaje *",
                                name="message",
                                required=True,
                                rows="6",
                            ),
                            rx.button(
                                "Enviar Mensaje",
                                type="submit",
                                size="3",
                                color_scheme="orange",
                                width="100%",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                        action="https://formsubmit.co/curto.brull.javier@jcurtobr.eu",
                        method="POST",
                    ),
                    # Información de contacto
                    rx.vstack(
                        rx.heading("Información de Contacto", size="6", color="#d19617", margin_bottom="1rem"),
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
                            spacing="4",
                            align="start",
                        ),
                        spacing="4",
                        align="start",
                    ),
                    columns="2",
                    spacing="6",
                    width="100%",
                ),
                spacing="5",
                padding="4rem 0",
            ),
            size="4",
        ),
        id="contacto",
        background="#1e2326",
    )


def footer() -> rx.Component:
    """Pie de página"""
    return rx.box(
        rx.container(
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
                    f"© Javier Curto Brull - 2024",
                    color="white",
                    size="2",
                ),
                rx.text(
                    "Desarrollado con Reflex",
                    color="#d19617",
                    size="1",
                ),
                spacing="4",
                align="center",
                padding="2rem 0",
            ),
            size="4",
        ),
        background="#252a2e",
        border_top="1px solid rgba(209, 150, 23, 0.3)",
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
    title="Javier Curto | Desarrollador Backend Java Spring",
    description="Portfolio personal de Javier Curto - Desarrollador Backend especializado en Java Spring",
)
