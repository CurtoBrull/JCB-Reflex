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
    pip install -r requirements.txt
    ```

4. **Configurar variables de entorno**:

    Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

    ```env
    # Configuración SMTP para envío de correos
    SMTP_HOST=tu-servidor-smtp.com
    SMTP_PORT=465
    SMTP_USER=tu-email@dominio.com
    SMTP_PASS=tu-contraseña
    ```

**Ejemplo para Gmail:**

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tu-email@gmail.com
SMTP_PASS=tu-app-password
```

**Ejemplo para servidor propio:**

```env
SMTP_HOST=jcurtobr.eu
SMTP_PORT=465
SMTP_USER=curto.brull.javier@jcurtobr.eu
SMTP_PASS=tu-contraseña
```

> **Nota:**
>
> - Puerto **465** usa SSL directo
> - Puerto **587** usa STARTTLS
> - Para Gmail necesitas crear una [contraseña de aplicación](https://support.google.com/accounts/answer/185833)

## 🚀 Ejecución

Para ejecutar el proyecto en modo desarrollo:

```bash
# Asegúrate de estar en el directorio del proyecto y con el entorno virtual activado
source venv/bin/activate
reflex run
```

El proyecto estará disponible en:

- **Frontend**: <http://localhost:3000/>
- **Backend**: <http://0.0.0.0:8000>

## 📁 Estructura del Proyecto

```text
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

### Despliegue en Namecheap (Hosting Compartido)

Dado que Reflex requiere un servidor ASGI/WebSocket que no está disponible en hosting compartido tradicional, se despliega como **sitio estático** con FormSubmit para el formulario de contacto.

#### Pasos para desplegar

1. **Compilar versión estática** (solo frontend):

    ```bash
    reflex export --frontend-only
    ```

    Esto genera los archivos estáticos en `.web/build/client/`

2. **Crear paquete de deployment**:

    ```bash
    cd .web/build/client
    tar -czf ~/portfolio-deploy.tar.gz .
    ```

3. **Subir a Namecheap vía cPanel**:

   - Accede a tu cPanel de Namecheap
   - Ve a **File Manager**
   - Navega a `/public_html/`
   - **Elimina todo el contenido** existente en `public_html`
   - Sube el archivo `portfolio-deploy.tar.gz`
   - Selecciona el archivo y haz clic en **Extract**
   - Elimina el archivo `.tar.gz` después de extraer

4. **Configurar FormSubmit**:

   - La primera vez que alguien envíe el formulario, recibirás un email de confirmación de FormSubmit
   - Haz clic en el enlace de activación para validar tu email
   - Después de esto, los mensajes llegarán directamente a tu correo

#### Notas importantes

- ✅ **No requiere backend** - Todo el sitio es HTML/CSS/JS estático
- ✅ **FormSubmit gratuito** - Maneja el envío de formularios sin servidor
- ✅ **CSS personalizado** - Oculta elementos de estado de Reflex (WebSocket, modales)
- ⚠️ **Sin funcionalidad del backend** - El State de Reflex no funciona en estático
- ⚠️ **Archivos estáticos solamente** - Los cambios requieren recompilar y resubir

#### Alternativas para deployment con backend completo

Si necesitas las funcionalidades completas de Reflex (State, WebSocket, backend):

- **Render.com** - $7/mes, soporte Python completo
- **Railway.app** - $5/mes, deploy automático desde GitHub
- **DigitalOcean App Platform** - Desde $6/mes
- **VPS propio** - Control total, desde $5/mes (DigitalOcean, Linode, Vultr)

Para deployment en producción:

```bash
reflex export
```

Esto generará una versión optimizada completa (no solo frontend).

## 👨‍💻 Autor

### **Javier Curto Brull**

- Desarrollador Backend Java Spring
- Email: <curto.brull.javier@jcurtobr.eu>
- Website: <https://jcurtobr.eu/>
- LinkedIn: [javier-curto-brull](https://www.linkedin.com/in/javier-curto-brull/)
- GitHub: [@CurtoBrull](https://github.com/CurtoBrull)

## 📄 Licencia

Este proyecto es personal y está disponible para referencia educativa.

---

### **Desarrollado con ❤️ usando Reflex Python**
