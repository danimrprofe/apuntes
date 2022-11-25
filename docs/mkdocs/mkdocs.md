# Mkdocs

MkDocs es un generador de documentación rápido, simple y delicioso escrito en Python.

Si alguna vez te has frustrado con el tedioso proceso de escribir y mantener la documentación, entonces MkDocs es la herramienta que necesitas.

Aquí hay una breve descripción de lo que MkDocs puede hacer:

- Generar un sitio web hermoso a partir de su documentación
- Escriba su documentación en Markdown, un lenguaje de marcado simple y fácil de usar
- Generar automáticamente una tabla de contenidos
- Implemente su documentación en GitHub Pages, Amazon S3 o cualquier otro servidor web

Ahora comencemos con MkDocs!

### Instalación

MkDocs se puede instalar con pip:

```
pip install mkdocs
```

### Guía de inicio rápido

Una vez que MkDocs esté instalado, podrá usar el comando `mkdocs` para crear un nuevo proyecto:

```
mkdocs new my-project
```

Esto creará un nuevo directorio llamado `my-project` con la siguiente estructura:

```
my-project/
    docs/
        index.md
    mkdocs.yml
```

A continuación, puede previsualizar su nuevo proyecto con el comando `serve`:

```
mkdocs serve
```

Abra http://127.0.0.1:8000 en su navegador y debería ver la página de inicio.

Ahora editemos el archivo `docs/index.md` y agreguemos el siguiente contenido:

```markdown
# Mi proyecto

¡Bienvenido a mi proyecto!
```

Guarde el archivo y actualice la página en su navegador y debería ver el contenido actualizado:

![Página de inicio actualizada](https://raw.githubusercontent.com/mkdocs/mkdocs/master/docs/images/mkdocs-updated-home-page.png)

### Implementando su documentación

Una vez que esté satisfecho con su documentación, puede usar el comando `mkdocs build` para generar un sitio estático:

```
mkdocs build
```

Esto creará un directorio `site` con todos los archivos necesarios para alojar su sitio web.

Si desea implementar su sitio en GitHub Pages, puede usar el comando `gh-deploy`:

```
mkdocs gh-deploy
```

Para obtener más información sobre la implementación de su documentación, consulte la sección [Implementando su documentación](http://www.mkdocs.org/user-guide/deploying-your-docs/) de la documentación de MkDocs.