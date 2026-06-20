"""Portfolio Personal de Javier Curto - Desarrollador Backend Java Spring"""

import reflex as rx
from rxconfig import config
from datetime import datetime


class State(rx.State):
    """The app state."""

    show_mobile_menu: bool = False

    def toggle_menu(self):
        """Toggle mobile menu visibility"""
        self.show_mobile_menu = not self.show_mobile_menu

    def close_menu(self):
        """Close mobile menu"""
        self.show_mobile_menu = False


class ThemeState(rx.State):
    """Estado del tema (claro/oscuro)."""
    is_dark: bool = True

    def toggle_theme(self):
        """Alterna entre tema claro y oscuro."""
        self.is_dark = not self.is_dark


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
                # Botón toggle tema claro/oscuro (JS puro - funciona en static export)
                rx.html(
                    """
                    <button onclick="(function(){var n=!document.documentElement.classList.contains('light-theme');document.documentElement.classList.toggle('light-theme',n);localStorage.setItem('theme',n?'light':'dark');var s=document.getElementById('theme-icon-sun'),m=document.getElementById('theme-icon-moon');if(s)s.style.display=n?'inline':'none';if(m)m.style.display=n?'none':'inline';})()" class="theme-toggle" aria-label="Toggle theme" style="background:none;border:none;cursor:pointer;padding:0.5rem;color:#d19617;">
                        <span id="theme-icon-sun" style="display:none;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                        </span>
                        <span id="theme-icon-moon" style="display:inline;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
                        </span>
                    </button>
                    """
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
        class_name="bg-navbar-blur",
        z_index="1000",
        box_shadow="var(--shadow-sm)",
    )


def social_icon(icon_name: str, href: str) -> rx.Component:
    """Iconos SVG para redes sociales"""
    icons = {
        "linkedin": rx.html(
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="white"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>',
            class_name="social-icon",
        ),
        "twitter": rx.html(
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="white"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>',
            class_name="social-icon",
        ),
        "github": rx.html(
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="white"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>',
            class_name="social-icon",
        ),
    }
    return rx.link(icons.get(icon_name, ""), href=href, is_external=True)


def inicio() -> rx.Component:
    """Sección de inicio con presentación"""
    return rx.box(
        rx.vstack(
            rx.box(
                rx.box(class_name="hero-ping"),
                rx.box(class_name="hero-ping hero-ping-2"),
                rx.box(class_name="hero-ping hero-ping-3"),
                rx.image(
                    src="/img/hero2.jpg",
                    alt="Javier Curto",
                    class_name="hero-img",
                ),
                class_name="hero-image-wrapper",
            ),
            rx.heading(
                "JAVIER CURTO",
                size="9",
                color="white",
                text_align="center",
                class_name="hero-name fade-in-up",
            ),
            rx.text(
                "Desarrollador Backend",
                size="6",
                color="#d19617",
                text_align="center",
                class_name="fade-in-up delay-1",
            ),
            # Subtítulos adicionales
            rx.vstack(
                rx.text("Python", size="5", color="#e5c507", text_align="center"),
                rx.text("Java Spring", size="5", color="#e5c507", text_align="center"),
                spacing="2",
                align="center",
                class_name="fade-in-up delay-2",
            ),
            # Iconos de redes sociales con SVGs
            rx.hstack(
                social_icon("linkedin", "https://www.linkedin.com/in/javier-curto-brull/"),
                social_icon("twitter", "https://x.com/JavierCurtoB"),
                social_icon("github", "https://github.com/CurtoBrull"),
                spacing="5",
                class_name="fade-in-up delay-3",
            ),
            # CTA con animación de pulso
            rx.link(
                rx.button(
                    "Ver Proyectos →",
                    size="3",
                    color_scheme="orange",
                    class_name="cta-button pulse-animation",
                ),
                href="#portfolio",
                class_name="fade-in-up delay-4",
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
        class_name="hero-bg-animation",
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
                class_name="scroll-reveal",
            ),
            rx.box(
                rx.vstack(
                    # Texto descriptivo
                    rx.vstack(
                        rx.text(
                            "Soy Técnico Superior en Desarrollo de Aplicaciones Web (CFGS) y ",
                            "Especialista en Desarrollo de Aplicaciones en Lenguaje Python (Curso Especialización FP) "
                            "previamente obtuve el título de Técnico en Sistemas Microinformáticos y Redes (CFGM).",
                            color="white",
                            line_height="1.8",
                        ),
                        rx.text(
                            "Actualmente trabajo como Desarrollador Backend en NTT Data desde febrero de 2023, "
                            "donde desarrollo aplicaciones con Java y Spring Framework, integrando bases de datos como DB2, "
                            "Postgress y MongoDB, y creando APIs REST robustas.",
                            color="white",
                            line_height="1.8",
                        ),
                        rx.text(
                            'He realizado el ',
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
                class_name="scroll-reveal sr-delay-1",
            ),
            spacing="5",
            padding_y="4rem",
            padding_x="2rem",
            width="100%",
            align="center",
        ),
        id="sobremi",
        class_name="section-primary",
        width="100%",
    )


def stat_item(target: str, suffix: str, label: str, icon: str) -> rx.Component:
    """Tarjeta de estadística individual con contador animado.
    target puede ser un número ('8') o 'auto:YYYY-MM' para calcular años desde esa fecha."""
    return rx.vstack(
        rx.icon(icon, size=36, color="#d19617"),
        rx.html(
            f'<p class="stat-number" data-target="{target}" data-suffix="{suffix}">0{suffix}</p>'
        ),
        rx.text(label, size="3", color="#aaa", text_align="center", weight="medium"),
        spacing="3",
        align="center",
        class_name="stat-item scroll-reveal",
        padding="1.5rem",
        width="100%",
    )


def stats() -> rx.Component:
    """Sección de estadísticas con contadores animados"""
    return rx.box(
        rx.grid(
            stat_item("auto:2022-10", "+", "Años de experiencia", "briefcase"),
            stat_item("8", "", "Proyectos en portfolio", "rocket"),
            stat_item("15", "+", "Tecnologías", "cpu"),
            stat_item("1001", "+", "Cafés tomados ☕", "coffee"),
            columns="4",
            spacing="5",
            width="100%",
            max_width="1200px",
            margin="0 auto",
            class_name="stats-grid",
        ),
        id="stats",
        class_name="stats-grid section-secondary",
        width="100%",
        padding_y="3rem",
        padding_x="2rem",
    )


def skill_icon_card(name: str, devicon: str = "", abbrev: str = "", white: bool = False) -> rx.Component:
    """Tarjeta de icono de tecnología para la sección Skills"""
    if devicon:
        extra = ' devicon-white' if white else ''
        icon_el = rx.html(
            f'<i class="{devicon}{extra}" style="font-size:2.2rem;line-height:1;"></i>'
        )
    else:
        icon_el = rx.box(
            rx.text(abbrev or name[:3].upper(), size="2", weight="bold", color="#d19617"),
            display="flex",
            align_items="center",
            justify_content="center",
            width="36px",
            height="36px",
            border="1.5px solid rgba(209,150,23,0.4)",
            border_radius="6px",
            flex_shrink="0",
        )
    return rx.vstack(
        icon_el,
        rx.text(name, size="1", color="#bbb", text_align="center"),
        spacing="2",
        align="center",
        justify="center",
        class_name="skill-icon-card",
        width="76px",
        min_height="86px",
        padding="0.6rem 0.4rem",
        border="1px solid rgba(255,255,255,0.06)",
        background="rgba(255,255,255,0.02)",
        border_radius="10px",
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
                class_name="scroll-reveal",
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
                            rx.flex(
                                skill_icon_card("Java", "devicon-java-plain colored"),
                                skill_icon_card("Python", "devicon-python-plain colored"),
                                skill_icon_card("Spring", "devicon-spring-plain colored"),
                                skill_icon_card("Git", "devicon-git-plain colored"),
                                skill_icon_card("GitHub", "devicon-github-original", white=True),
                                skill_icon_card("PostgreSQL", "devicon-postgresql-plain colored"),
                                skill_icon_card("MongoDB", "devicon-mongodb-plain colored"),
                                skill_icon_card("Oracle", "devicon-oracle-original colored"),
                                skill_icon_card("Postman", "devicon-postman-plain colored"),
                                skill_icon_card("HTML5", "devicon-html5-plain colored"),
                                skill_icon_card("CSS3", "devicon-css3-plain colored"),
                                skill_icon_card("JavaScript", "devicon-javascript-plain colored"),
                                skill_icon_card("PHP", "devicon-php-plain colored"),
                                skill_icon_card("jQuery", "devicon-jquery-plain colored"),
                                skill_icon_card("SQL", abbrev="SQL"),
                                skill_icon_card("DB2", abbrev="DB2"),
                                wrap="wrap",
                                gap="3",
                                width="100%",
                            ),
                            spacing="4",
                            align="start",
                            width="100%",
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
                class_name="scroll-reveal sr-delay-1",
            ),
            spacing="5",
            padding_y="4rem",
            padding_x="2rem",
            width="100%",
            align="center",
        ),
        id="skills",
        class_name="section-secondary",
        width="100%",
    )


def timeline_entry(
    date: str,
    title: str,
    org: str,
    desc: str = "",
    extra_classes: str = "",
) -> rx.Component:
    """Entrada individual del timeline del CV"""
    content: list = [
        rx.badge(date, color_scheme="plum", variant="surface", size="3", radius="small"),
        rx.heading(title, size="5", color="white"),
        rx.text(org, color="#ccc", size="3", weight="medium"),
    ]
    if desc:
        content.append(
            rx.text(
                desc,
                color="#666",
                size="1",
                style={"lineHeight": "1.6"},
            )
        )
    return rx.box(
        *content,
        class_name=f"timeline-entry scroll-reveal {extra_classes}".strip(),
        display="flex",
        flex_direction="column",
        gap="0.35rem",
    )


def curriculum() -> rx.Component:
    """Sección de educación y experiencia laboral con timeline visual"""
    return rx.box(
        rx.vstack(
            rx.heading(
                "CURRICULUM",
                size="8",
                color="#d19617",
                text_align="center",
                class_name="scroll-reveal",
            ),
            rx.grid(
                # ── Columna Educación ──────────────────────────────
                rx.vstack(
                    rx.hstack(
                        rx.icon("graduation-cap", size=20, color="#d19617"),
                        rx.heading("Educación", size="5", color="#d19617"),
                        spacing="2",
                        align="center",
                        margin_bottom="1.5rem",
                    ),
                    rx.box(
                        timeline_entry(
                            "2025 — 2026",
                            "C.E. Desarrollo de Aplicaciones en Lenguaje Python",
                            "IES Al-Ándalus",
                        ),
                        timeline_entry(
                            "2020 — 2022",
                            "CFGS Desarrollo de Aplicaciones Web",
                            "IES La Puebla",
                            extra_classes="sr-delay-1",
                        ),
                        timeline_entry(
                            "2018 — 2020",
                            "CFGM Técnico en Sistemas Microinformáticos",
                            "IES La Puebla",
                            extra_classes="sr-delay-2",
                        ),
                        class_name="timeline",
                        width="100%",
                    ),
                    spacing="0",
                    align="start",
                    width="100%",
                ),
                # ── Columna Experiencia ────────────────────────────
                rx.vstack(
                    rx.hstack(
                        rx.icon("briefcase", size=20, color="#d19617"),
                        rx.heading("Experiencia", size="5", color="#d19617"),
                        spacing="2",
                        align="center",
                        margin_bottom="1.5rem",
                    ),
                    rx.box(
                        timeline_entry(
                            "Feb 2023 — Actualidad",
                            "Desarrollador Backend Spring",
                            "NTT Data",
                            "Java · Spring · API REST · DB2 · Oracle · PostgreSQL · PL/SQL · MongoDB · Postman",
                        ),
                        timeline_entry(
                            "Oct — Dic 2022",
                            "Prácticas Desarrollador Backend",
                            "NTT Data",
                            extra_classes="sr-delay-1",
                        ),
                        timeline_entry(
                            "1998 — Feb 2023",
                            "Militar Profesional",
                            "Ministerio de Defensa",
                            extra_classes="sr-delay-2",
                        ),
                        class_name="timeline",
                        width="100%",
                    ),
                    spacing="0",
                    align="start",
                    width="100%",
                ),
                columns="2",
                spacing="8",
                width="100%",
                max_width="1100px",
                class_name="timeline-cols",
            ),
            # Botón descarga CV
            rx.link(
                rx.button(
                    rx.icon("download", size=16),
                    "Descargar CV",
                    size="3",
                    color="white",
                    variant="soft",
                    gap="0.5rem",
                    class_name="cv-btn",
                ),
                href="/cv/CV_Javier_Curto_Brull.pdf",
                is_external=True,
                class_name="scroll-reveal sr-delay-1",
            ),
            spacing="8",
            padding_y="4rem",
            padding_x="2rem",
            width="100%",
            align="center",
        ),
        id="curriculum",
        class_name="section-primary",
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
            # Imagen con badge "Live Demo" superpuesto
            rx.box(
                rx.image(
                    src=image,
                    alt=title,
                    width="100%",
                    height="200px",
                    object_fit="cover",
                ),
                *([rx.box(
                    rx.badge("● Live", color_scheme="green", variant="solid", size="1"),
                    position="absolute",
                    top="0.5rem",
                    right="0.5rem",
                    z_index="2",
                )] if demo_url else []),
                position="relative",
                width="100%",
                overflow="hidden",
                flex_shrink="0",
            ),
            # Contenido — flex=1 para ocupar el espacio restante, justify=between para botones al fondo
            rx.vstack(
                rx.heading(title, size="5", color="white"),
                rx.text(description, color="white", size="2", line_height="1.5"),
                rx.box(
                    rx.text(tech, color="#d19617", size="1"),
                    class_name="tech-badge",
                ),
                rx.hstack(
                    rx.spacer(),
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
                    align="center",
                    width="100%",
                ),
                spacing="2",
                padding="1rem",
                align="start",
                width="100%",
                flex="1",
                justify="between",
            ),
            spacing="0",
            width="100%",
            height="100%",
        ),
        class_name="bg-card project-card",
        border_radius="8px",
        overflow="hidden",
        box_shadow="0 4px 6px rgba(0,0,0,0.3)",
        transition="transform 0.3s ease, box-shadow 0.3s ease",
        _hover={"transform": "translateY(-6px)", "box_shadow": "0 12px 30px rgba(209, 150, 23, 0.22)"},
        width="100%",
        height="100%",
    )


def portfolio() -> rx.Component:
    """Sección de portfolio con proyectos"""
    return rx.box(
        rx.vstack(
            rx.heading("PORTFOLIO", size="8", color="#d19617", margin_bottom="2rem", class_name="scroll-reveal"),
            rx.grid(
                rx.box(project_card(
                    "Web Personal ASTRO",
                    "Web para mostrar proyectos, habilidades y datos de contacto",
                    "/img/webAstroJCB.webp",
                    "Astro • Tailwind CSS",
                    "https://github.com/CurtoBrull/AstroJCB",
                ), class_name="scroll-reveal sr-delay-1"),
                rx.box(project_card(
                    "API Spring JPA",
                    "CRUD básico para gestionar productos",
                    "/img/API_SPRING.webp",
                    "Spring Boot • JPA • MySQL",
                    "https://github.com/CurtoBrull/API_SPRING",
                ), class_name="scroll-reveal sr-delay-2"),
                rx.box(project_card(
                    "OAuth2 con Spring Security",
                    "Autenticación y autorización de usuarios",
                    "/img/postmanPOSTCode.png",
                    "Spring Security • OAuth2 • Spring Boot",
                    "https://github.com/CurtoBrull/OAuth2-Spring-Security",
                ), class_name="scroll-reveal sr-delay-3"),
                rx.box(project_card(
                    "GitHub User Activity App",
                    "Buscar información de usuarios de GitHub. Render tarda un poco en despertar la app.",
                    "/img/GitHubUserDetails.png",
                    "Spring Boot • GitHub API",
                    "https://github.com/CurtoBrull/GithubApiSpring",
                    "https://githubapispring.onrender.com/",
                ), class_name="scroll-reveal sr-delay-1"),
                rx.box(project_card(
                    "Inventario del Congelador",
                    "App para controlar productos del congelador",
                    "/img/inventario-congelador.jpg",
                    "Next.js • React • Supabase",
                    "https://github.com/CurtoBrull/inventario-congelador",
                    "https://congelador-inventario.vercel.app/",
                ), class_name="scroll-reveal sr-delay-2"),
                rx.box(project_card(
                    "NoPokeForYou",
                    "App fullstack troll con Pokémon + Gemini AI. Render tarda un poco en despertar la app.",
                    "/img/nopokeforyou.png",
                    "React • Spring Boot • Gemini AI",
                    "https://github.com/CurtoBrull/NoPokeForYou",
                    "https://nopokeforyou-front.onrender.com/",
                ), class_name="scroll-reveal sr-delay-3"),
                rx.box(project_card(
                    "Generador de Ideas Gemini",
                    "Genera ideas creativas usando IA Gemini. Render tarda un poco en despertar la app.",
                    "/img/generador-ideas-gemini.png",
                    "Python • Gradio • Gemini AI",
                    "https://github.com/CurtoBrull/generador-ideas-gemini",
                    "https://generador-ideas-gemini.onrender.com/",
                ), class_name="scroll-reveal sr-delay-1"),
                rx.box(project_card(
                    "Grocery Ticket AI",
                    "Procesa tickets de compra con OCR + Gemini",
                    "/img/groceryticketai.png",
                    "Tesseract.js • Gemini API • Supabase",
                    "https://github.com/CurtoBrull/grocery-ticket-ai",
                    "https://grocery-ticket-ai.vercel.app/",
                ), class_name="scroll-reveal sr-delay-2"),
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
        class_name="section-secondary",
        width="100%",
    )


def contacto() -> rx.Component:
    """Sección de contacto con formulario usando FormSubmit"""
    return rx.box(
        rx.vstack(
            rx.heading(
                "CONTACTO",
                size="8",
                color="#d19617",
                text_align="center",
                class_name="scroll-reveal",
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
                        # Formulario con FormSubmit
                        rx.html(
                            """
                            <form action="https://formsubmit.co/curto.brull.javier@jcurtobr.eu" method="POST" style="width: 100%; display: flex; flex-direction: column; align-items: center; gap: 1rem;">
                                <!-- Campos ocultos de configuración FormSubmit -->
                                <input type="hidden" name="_subject" value="Nuevo mensaje desde Portfolio Web">
                                <input type="hidden" name="_captcha" value="false">
                                <input type="hidden" name="_template" value="table">
                                <input type="text" name="_honey" style="display:none">
                                
                                <!-- Campos visibles -->
                                <input type="text" name="name" placeholder="Nombre *" required 
                                    style="width: 80%; height: 3rem; padding: 0.75rem; border-radius: 0.375rem; border: 1px solid #374151; background: #1f2937; color: white; font-size: 1rem;">
                                
                                <input type="tel" name="phone" placeholder="Teléfono"
                                    style="width: 80%; height: 3rem; padding: 0.75rem; border-radius: 0.375rem; border: 1px solid #374151; background: #1f2937; color: white; font-size: 1rem;">
                                
                                <input type="email" name="email" placeholder="Email *" required
                                    style="width: 80%; height: 3rem; padding: 0.75rem; border-radius: 0.375rem; border: 1px solid #374151; background: #1f2937; color: white; font-size: 1rem;">
                                
                                <textarea name="message" placeholder="Mensaje *" required rows="8"
                                    style="width: 80%; min-height: 150px; padding: 0.75rem; border-radius: 0.375rem; border: 1px solid #374151; background: #1f2937; color: white; font-size: 1rem; resize: vertical;"></textarea>
                                
                                <button type="submit"
                                    style="width: 80%; height: 3rem; background: #d19617; color: white; border: none; border-radius: 0.375rem; font-size: 1rem; font-weight: 600; cursor: pointer; transition: background 0.3s;">
                                    Enviar Mensaje
                                </button>
                            </form>
                            """
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
                                    rx.html(
                                        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#d19617"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>',
                                    ),
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
                class_name="scroll-reveal sr-delay-1",
            ),
            spacing="5",
            padding_y="4rem",
            padding_x="2rem",
            width="100%",
            align="center",
        ),
        id="contacto",
        class_name="section-primary",
        width="100%",
    )


def footer_social_icon(icon_name: str, href: str) -> rx.Component:
    """Iconos SVG para redes sociales en footer"""
    icons = {
        "linkedin": rx.html(
            '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="white"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>',
            class_name="social-icon",
        ),
        "twitter": rx.html(
            '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="white"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>',
            class_name="social-icon",
        ),
        "github": rx.html(
            '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="white"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>',
            class_name="social-icon",
        ),
    }
    return rx.link(icons.get(icon_name, ""), href=href, is_external=True)


def footer() -> rx.Component:
    """Pie de página"""
    return rx.box(
        rx.vstack(
            rx.link(
                rx.button(
                    rx.icon("arrow-up", size=24, class_name="footer-up-icon"),
                    variant="ghost",
                    color="white",
                ),
                href="#inicio",
            ),
            rx.hstack(
                footer_social_icon("linkedin", "https://www.linkedin.com/in/javier-curto-brull/"),
                footer_social_icon("twitter", "https://twitter.com/CurtoBrull"),
                footer_social_icon("github", "https://github.com/CurtoBrull"),
                spacing="5",
            ),
            rx.text(
                f"© Javier Curto Brull - {datetime.now().year}",
                color="white",
                size="2",
            ),
            spacing="4",
            align="center",
            padding_y="2rem",
            padding_x="2rem",
            width="100%",
        ),
        class_name="section-primary",
        width="100%",
    )


def index() -> rx.Component:
    """Página principal con todas las secciones"""
    return rx.box(
        rx.script(src="/theme.js"),
        rx.script(src="/scroll-reveal.js"),
        rx.script(src="/scroll-progress.js"),
        rx.script(src="/stats-counter.js"),
        navbar(),
        inicio(),
        sobre_mi(),
        stats(),
        skills(),
        curriculum(),
        portfolio(),
        contacto(),
        footer(),
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
