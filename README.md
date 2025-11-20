# Portfolio Personal - Reflex Python

Este es mi portfolio personal desarrollado con **Reflex**, un framework Python moderno para crear aplicaciones web fullstack.

## 🚀 Características

- **Portfolio completo** con todas las secciones: Inicio, Sobre Mí, Skills, Curriculum, Portfolio y Contacto
- **Diseño responsive** que se adapta a cualquier dispositivo
- **Navegación suave** entre secciones
- **Menú móvil** hamburguesa para pantallas pequeñas
- **8 proyectos destacados** con enlaces a GitHub y demos en vivo
- **Formulario de contacto** integrado con FormSubmit
- **Estilos personalizados** con colores corporativos (#d19617)

## 📋 Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)

## 🛠️ Instalación

1. **Clonar el repositorio** (o navegar al directorio del proyecto):
```bash
cd ~/workspace/JCB-Reflex
```

2. **Crear y activar el entorno virtual**:
```bash
python3.12 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**:
```bash
pip install reflex
```

## 🚀 Ejecución

Para ejecutar el proyecto en modo desarrollo:

```bash
# Asegúrate de estar en el directorio del proyecto y con el entorno virtual activado
source venv/bin/activate
reflex run
```

El proyecto estará disponible en:
- **Frontend**: http://localhost:3000/
- **Backend**: http://0.0.0.0:8000

## 📁 Estructura del Proyecto

```
JCB-Reflex/
├── JCB_Reflex/
│   ├── JCB_Reflex.py      # Archivo principal con todos los componentes
│   └── __init__.py
├── assets/
│   ├── img/               # Imágenes del portfolio
│   ├── cv/                # CV en PDF
│   ├── custom.css         # Estilos personalizados
│   └── favicon.ico
├── rxconfig.py            # Configuración de Reflex
├── requirements.txt       # Dependencias Python
└── venv/                  # Entorno virtual
```

## 🎨 Tecnologías Utilizadas

- **Reflex 0.8.20** - Framework Python para aplicaciones web
- **Tailwind CSS V4** - Framework CSS (configurado via plugin)
- **Google Fonts** - Righteous y Work Sans
- **Lucide Icons** - Iconos via Reflex
- **FormSubmit.co** - Servicio de formularios

## 📝 Secciones del Portfolio

1. **Inicio** - Presentación con foto de perfil y redes sociales
2. **Sobre Mí** - Información personal, formación y experiencia
3. **Skills** - Habilidades técnicas y profesionales
4. **Curriculum** - Educación y experiencia laboral detallada
5. **Portfolio** - Galería de 8 proyectos con enlaces
6. **Contacto** - Formulario de contacto e información

## 🔧 Personalización

Para personalizar el contenido:

1. Edita el archivo `JCB_Reflex/JCB_Reflex.py`
2. Actualiza las imágenes en `assets/img/`
3. Modifica los estilos en `assets/custom.css`
4. Cambia la configuración en `rxconfig.py`

## 📱 Responsive Design

El diseño es completamente responsive con breakpoints en:
- **Desktop**: > 1024px - Grid de 3 columnas para proyectos
- **Tablet**: 768px - 1024px - Grid de 2 columnas
- **Mobile**: < 768px - Grid de 1 columna, menú hamburguesa

## 🌐 Deploy

Para construir y desplegar en producción:

```bash
reflex export
```

Esto generará una versión optimizada en el directorio `.web/_static/`.

## 👨‍💻 Autor

**Javier Curto Brull**
- Desarrollador Backend Java Spring
- Email: curto.brull.javier@jcurtobr.eu
- Website: https://jcurtobr.eu/
- LinkedIn: [javier-curto-brull](https://www.linkedin.com/in/javier-curto-brull/)
- GitHub: [@CurtoBrull](https://github.com/CurtoBrull)

## 📄 Licencia

Este proyecto es personal y está disponible para referencia educativa.

---

**Desarrollado con ❤️ usando Reflex Python**
