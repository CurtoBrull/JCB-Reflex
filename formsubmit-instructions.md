# Configuración de FormSubmit para el formulario de contacto

## Pasos para configurar FormSubmit:

### 1. Modificar el archivo `index.html` en el servidor

En el archivo `/home/jcurdyhg/public_html/index.html`, busca el formulario de contacto y modifica el `<form>` para que quede así:

```html
<form action="https://formsubmit.co/curto.brull.javier@jcurtobr.eu" method="POST">
    <!-- Campos ocultos de configuración de FormSubmit -->
    <input type="hidden" name="_subject" value="Nuevo mensaje desde Portfolio Web">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="_template" value="table">
    <input type="text" name="_honey" style="display:none">
    <input type="hidden" name="_next" value="https://jcurtobr.eu/gracias.html">
    
    <!-- Campos visibles del formulario -->
    <input type="text" name="name" placeholder="Nombre *" required>
    <input type="tel" name="phone" placeholder="Teléfono">
    <input type="email" name="email" placeholder="Email *" required>
    <textarea name="message" placeholder="Mensaje *" rows="8" required></textarea>
    <button type="submit">Enviar Mensaje</button>
</form>
```

### 2. Verificación inicial

La primera vez que alguien envíe el formulario:
1. FormSubmit enviará un email de verificación a `curto.brull.javier@jcurtobr.eu`
2. Click en el enlace de verificación
3. A partir de ahí, todos los mensajes llegarán directamente

### 3. Crear página de agradecimiento (opcional)

Crea `/home/jcurdyhg/public_html/gracias.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mensaje Enviado - Javier Curto</title>
    <style>
        body {
            font-family: 'Work Sans', sans-serif;
            background: linear-gradient(135deg, #1e2326 0%, #252a2e 100%);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }
        .container {
            text-align: center;
            max-width: 500px;
        }
        h1 { color: #d19617; margin-bottom: 20px; }
        p { line-height: 1.8; margin-bottom: 30px; }
        a {
            display: inline-block;
            background: #d19617;
            color: white;
            padding: 12px 30px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: 600;
        }
        a:hover { background: #e5c507; }
    </style>
</head>
<body>
    <div class="container">
        <h1>✓ Mensaje Enviado</h1>
        <p>Tu mensaje ha sido enviado correctamente. Te responderé lo antes posible.</p>
        <a href="/">Volver al inicio</a>
    </div>
</body>
</html>
```

## Ventajas de FormSubmit:

✓ Gratis  
✓ Sin backend necesario  
✓ Protección anti-spam integrada  
✓ Confirmación por email  
✓ Funciona en hosting estático  

## Documentación:

https://formsubmit.co/
