# Portfolio Personal - Reflex Python

Portfolio personal desarrollado con **Reflex 0.9.x** (framework Python para web) y desplegado como **sitio estático** en Hostinger.

## Características

- Secciones: Inicio, Sobre Mí, Stats, Skills, Curriculum, Portfolio y Contacto
- Modo claro/oscuro con persistencia en localStorage
- Contadores animados (IntersectionObserver + requestAnimationFrame)
- Timeline visual para CV
- Iconos de tecnologías via Devicons
- Formulario de contacto con FormSubmit
- Responsive con menú hamburguesa para móvil
- Animaciones scroll-reveal y progreso de scroll

## Requisitos

- Python 3.10 o superior
- Node.js 18 o superior (Reflex lo gestiona automáticamente)

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/CurtoBrull/JCB-Reflex.git
cd JCB-Reflex

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Desarrollo local

```bash
source venv/bin/activate
reflex run
```

- Frontend: <http://localhost:3000/>
- Backend: <http://0.0.0.0:8000>

## Despliegue en Hostinger

El sitio se exporta como HTML/CSS/JS estático y se sube al hosting compartido.

### 1. Generar el build estático

```bash
reflex export --frontend-only --no-zip
```

Los archivos se generan en `.web/build/client/`.

### 2. Subir a Hostinger

**Opción A — File Manager (panel Hostinger):**

1. Accede a [hpanel.hostinger.com](https://hpanel.hostinger.com)
2. Ve a **Files → File Manager → public_html/**
3. Elimina el contenido anterior de `public_html/`
4. Sube **todo el contenido** de `.web/build/client/`
5. Sube el archivo `.htaccess` de la raíz del proyecto a `public_html/`

**Opción B — FTP/SFTP:**

```bash
# Con lftp (Linux/Mac/WSL)
lftp -u usuario,contraseña ftp.jcurtobr.eu
mirror --reverse --delete .web/build/client/ /public_html/
put .htaccess -o /public_html/.htaccess
quit
```

### Notas de despliegue

- El `.htaccess` configura la reescritura de rutas SPA y sirve ficheros `.gz` precomprimidos
- Sin backend activo: el State de Reflex y WebSocket no funcionan (diseño intencionado)
- El formulario de contacto funciona via [FormSubmit.co](https://formsubmit.co) sin servidor propio

## Estructura del proyecto

```text
JCB-Reflex/
├── JCB_Reflex/
│   └── JCB_Reflex.py       # Componentes y lógica de la app
├── assets/
│   ├── img/                # Imágenes (hero, proyectos)
│   ├── cv/                 # CV en PDF
│   ├── custom.css          # Estilos y tema claro/oscuro
│   ├── theme.js            # Inicialización del tema (localStorage)
│   ├── scroll-reveal.js    # Animaciones de entrada al hacer scroll
│   ├── scroll-progress.js  # Barra de progreso de scroll
│   ├── stats-counter.js    # Contadores animados
│   └── favicon.ico
├── .htaccess               # Configuración Apache para Hostinger
├── rxconfig.py             # Configuración de Reflex
└── requirements.txt        # Dependencias Python
```

## Tecnologías

- **Reflex 0.9.5** — Framework Python para web
- **Radix UI / Tailwind CSS V4** — Sistema de diseño y utilidades CSS
- **Devicons v2.16** — Iconos de tecnologías via CDN
- **Lucide Icons** — Iconos de interfaz via Reflex
- **Google Fonts** — Righteous y Work Sans
- **FormSubmit.co** — Formulario de contacto sin backend

## Autor

**Javier Curto Brull** — Desarrollador Backend Java · Python

- Web: <https://jcurtobr.eu/>
- LinkedIn: [javier-curto-brull](https://www.linkedin.com/in/javier-curto-brull/)
- GitHub: [@CurtoBrull](https://github.com/CurtoBrull)
- Email: <curto.brull.javier@jcurtobr.eu>
