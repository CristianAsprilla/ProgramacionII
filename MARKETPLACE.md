# Publicar el curso en el JetBrains Marketplace

Guía paso a paso para subir el curso **Programación II — Currículo MEDUCA** al marketplace de JetBrains Academy.

> **Estado actual:** Curso listo y pusheado a GitHub (§ 1 ya hecho).
> **Pendiente:** Pasos § 2 en adelante, después de la aprobación como vendor.

---

## Tabla de contenidos

0. [Prerequisitos](#prerrequisitos)
1. [Subir el codigo a GitHub](#1-subir-el-codigo-a-github) ✅
2. [Convertirse en vendor de JetBrains](#2-convertirse-en-vendor-de-jetbrains)
3. [Crear el plugin descriptor](#3-crear-el-plugin-descriptor)
4. [Configurar Gradle wrapper](#4-configurar-gradle-wrapper)
5. [Compilar el .zip del plugin](#5-compilar-el-zip-del-plugin)
6. [Subir el plugin al marketplace](#6-subir-el-plugin-al-marketplace)
7. [Llenar metadata del marketplace](#7-llenar-metadata-del-marketplace)
8. [Revision y aprobacion](#8-revision-y-aprobacion)
9. [Despues de publicado](#9-despues-de-publicado)

---

## Prerequisitos

- Java 17 o superior (ya tienes el OpenJDK en `/usr/lib/jvm/default`).
- Conexion a internet.
- Repositorio del curso en GitHub (ya tienes `github.com/CristianAsprilla/ProgramacionII`).
- Una cuenta de JetBrains (con la misma dirección de email que usas en GitHub).
- El archivo LICENSE con copyright dual (ya está en el repo).

---

## 1. Subir el codigo a GitHub ✅

El codigo del curso debe estar en un repositorio publico de GitHub.
Eso ya está hecho en `github.com/CristianAsprilla/ProgramacionII`.

**Verificar:**

```bash
git remote -v
# Debe mostrar origin  https://github.com/CristianAsprilla/ProgramacionII.git (push)
```

**Los commits de Cristian Asprilla ya quedaron registrados.** § 1 completo.

---

## 2. Convertirse en vendor de JetBrains

Este paso se hace UNA sola vez por autor. Tiempo estimado: 1-3 dias habiles (revision manual de JetBrains).

### 2.1. Iniciar sesion

1. Ve a <https://plugins.jetbrains.com/vendor>
2. Inicia sesion con tu cuenta personal de JetBrains
3. Haz clic en **\"Apply for a vendor account\"** o **\"Become a vendor\"**

### 2.2. Llenar el formulario

| Campo | Valor recomendado |
|---|---|
| **Vendor name** | `Cristian Asprilla` |
| **Display name** (como aparece al publico) | `Programacion II — Curriculo MEDUCA` o `MEDUCA Educacion Panama` |
| **Vendor status** | **Non-trader** (porque distribuyes gratis) |
| **Email de contacto** | tu email personal |
| **Sitio web** | `https://github.com/CristianAsprilla/ProgramacionII` |
| **Pais** | Panama |
| **Descripcion del vendor** | "Profesor de Programacion II, Bachillerato Tecnico, MEDUCA Panama. Adaptacion del template de JetBrains Academy al curriculo oficial del Ministerio de Educacion de Panama." |

### 2.3. Aceptar terminos

- Acepta el JetBrains Plugins Marketplace Agreement.
- Acepta la politica de privacidad.
- Confirma el email.

### 2.4. Esperar aprobacion

JetBrains suele responder en 1-3 dias habiles. Mientras esperas, puedes continuar con los pasos siguientes.

---

## 3. Crear el plugin descriptor

El descriptor `plugin.xml` indica a IntelliJ que este ZIP es un plugin. En este caso, lo subes como curso marketplace.

### 3.1. Crear el archivo `src/main/resources/META-INF/plugin.xml`

Estructura de directorios esperada:

```
ProgramacionII/
├── src/
│   └── main/
│       └── resources/
│           └── META-INF/
│               └── plugin.xml
├── build.gradle.kts
├── gradle.properties
├── gradlew
├── gradlew.bat
├── course-info.yaml
├── lessons/, projects/ … (tu contenido del curso)
```

(El archivo `plugin.xml` debe quedar en `src/main/resources/META-INF/`. En el repo actual no existe; hay que crearlo.)

### 3.2. Contenido del `plugin.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<idea-plugin>
    <id>pa.meduca.programacion-ii</id>
    <name>Programacion II — Curriculo MEDUCA</name>
    <vendor email="[email]" url="https://github.com/CristianAsprilla/ProgramacionII">
        Cristian Asprilla
    </vendor>
    <description><![CDATA[
        Curso de Programacion II del Bachillerato Tecnico de Panama,
        alineado con el curriculo oficial del MEDUCA (Ministerio de Educacion de Panama),
        grado 11. Apto para cualquier colegio del pais.

        Cubre: variables y tipos, operadores, control de flujo, funciones y subrutinas,
        arreglos 1D/2D, listas dinamicas, pilas, diccionarios, y un modulo sobre uso
        responsable de asistentes de IA generativa.

        Basado en el template oficial de JetBrains Academy, con contenido adaptado
        al contexto educativo panameno (ITBMS, escala 1.0-5.0, vocabulario local).
    ]]></description>
    <change-notes><![CDATA[
        <h2>v1.0.0 — Version inicial</h2>
        <ul>
            <li>15 lecciones con 10+ practicos cada una</li>
            <li>3 proyectos guiados con integracion incremental</li>
            <li>21 quizzes de pruebas de escritorio balanceados</li>
            <li>Localizacion al espanol panameno (MEDUCA)</li>
        </ul>
    ]]></change-notes>
    <idea-version since-build="232.0" until-build="252.*"/>
    <depends>com.jetbrains.edu</depends>
</idea-plugin>
```

> **Nota:** Reemplaza `[email]` con tu direccion de email real.
> El `vendor` debe coincidir con el vendor que aprobaste en § 2.

### 3.3. Crear `gradle.properties`

```properties
pluginGroup=pa.meduca
pluginName=ProgramacionII
pluginVersion=1.0.0
pluginSandboxVersion=2026.6
pluginSinceBuild=232.0
pluginUntilBuild=252.*
```

---

## 4. Configurar Gradle wrapper

El gradle wrapper es un script que descarga gradle automaticamente. Te ahorra instalarlo manualmente.

### 4.1. Descargar el template de JetBrains Academy

```bash
cd /tmp
git clone --depth 1 https://github.com/JetBrains-Academy/marketplace-courses-example.git
ls marketplace-courses-example/
```

### 4.2. Copiar gradle wrapper a tu repo

```bash
cd /home/cristianasprilla/PycharmProjects/ProgramacionII
cp /tmp/marketplace-courses-example/gradlew .
cp /tmp/marketplace-courses-example/gradlew.bat .
cp -r /tmp/marketplace-courses-example/gradle/ .
chmod +x gradlew
git add gradlew gradlew.bat gradle/
git commit -m "Agregar gradle wrapper para build del plugin"
```

### 4.3. Crear `build.gradle.kts`

```kotlin
import org.jetbrains.changelog.markdownToHTML

plugins {
    id("java")
    id("org.jetbrains.intellij") version "1.17.2"
    id("org.jetbrains.changelog") version "1.3.1"
    id("org.jetbrains.edu") version "1.0.0" apply false
}

group = "pa.meduca"
version = "1.0.0"

repositories {
    mavenCentral()
}

intellij {
    version.set("2026.6")
    plugins.set(listOf("com.jetbrains.edu:2026.6"))
}

tasks {
    // Solo empaqueta el curso, no compila codigo Java
    buildSearchableOptions {
        enabled = false
    }
    jar {
        from("course-info.yaml")
    }
}

dependencies {
    intellij()
}
```

(El template oficial tiene un `build.gradle.kts` mucho mas completo; este es el minimo esencial.)

---

## 5. Compilar el .zip del plugin

Una vez tengas gradle wrapper configurado:

```bash
cd /home/cristianasprilla/PycharmProjects/ProgramacionII
./gradlew buildPlugin
```

Esto genera `build/distributions/ProgramacionII-1.0.0.zip`. Ese es el archivo que subes al marketplace.

**Si el build falla** por errores de tipo:

```bash
./gradlew --info buildPlugin 2>&1 | tail -50
```

y consulta el log. Las causas mas comunes son:
- Version de IntelliJ incorrecta en `intellij { version.set(...) }`
- Dependencias no disponibles (verifica que `mavenCentral()` esta agregado)
- plugin.xml con tags invalidos

---

## 6. Subir el plugin al marketplace

Con la cuenta de vendor aprobada (ver § 2):

1. Ve a <https://plugins.jetbrains.com/plugin/add>
2. Inicia sesion
3. Haz clic en **\"Upload plugin\"**
4. Selecciona `ProgramacionII-1.0.0.zip` que generaste en § 5
5. JetBrains valida el archivo (puede tardar 5-15 min)
6. Si pasa la validacion, te aparece una pantalla para llenar metadata

---

## 7. Llenar metadata del marketplace

| Campo | Valor |
|---|---|
| **Plugin name** | Programacion II — Curriculo MEDUCA |
| **Plugin ID** | `pa.meduca.programacion-ii` |
| **Category** | Education |
| **Tags** | panama, educacion, python, jetbrains-academy, meduca, bachillerato-tecnico |
| **License** | MIT (compatible con tu LICENSE) |
| **Description (corto)** | "Curso de Programacion II del Bachillerato Tecnico de Panama, alineado al curriculo del MEDUCA (Ministerio de Educacion)." |
| **Description (largo)** | texto completo en espanol con HTML basico |
| **Code source link** | <https://github.com/CristianAsprilla/ProgramacionII> |
| **Documentation link** | (opcional) el README se autodocumenta |
| **Logo** | imagen PNG 256x256 |
| **Feature graphic** | imagen PNG 480x320 |
| **Promo banner** | imagen PNG 1280x640 |
| **Version** | 1.0.0 |
| **Build** | 2026.6 (o la build de IntelliJ que targeteas) |

### 7.1. Imagenes requeridas

Crea tres imagenes:

- **Logo 256x256.png**: icono cuadrado, legible a 64x64
- **Feature 480x320.png**: portada del curso, incluye el titulo
- **Promo 1280x640.png**: banner promocional para marketplace

Herramientas gratuitas para crearlas:
- GIMP (<https://www.gimp.org/>)
- Inkscape (<https://inkscape.org/>)
- Canva (<https://www.canva.com/>)

Estilo sugerido: bandera o simbolos de Panama, libro de Python, IDE de JetBrains, etc.

---

## 8. Revision y aprobacion

JetBrains revisa los plugins educativos manualmente (no automatico).

- **Tiempo**: 3-7 dias habiles
- **Posibles rechazos**: contenido ofensivo, copyright sin acreditar, problemas tecnicos graves
- **Tras la aprobacion**: el plugin aparece en `plugins.jetbrains.com/plugin/pa.meduca.programacion-ii` y los usuarios pueden instalarlo desde PyCharm/IntelliJ

---

## 9. Despues de publicado

### 9.1. Verificar que el plugin es instalable

1. Abre PyCharm en otro computador
2. `Settings > Plugins > Marketplace > search "Programacion II MEDUCA"`
3. Debe aparecer listada
4. Haz clic en `Install`
5. Reinicia PyCharm
6. Crea un nuevo proyecto y elige el curso recien instalado
7. Verifica que cargan las 15 lecciones y los 3 proyectos guiados

### 9.2. Mantener versiones

Para publicar una nueva version (correcciones, nuevos ejemplos):

1. Edita el contenido en tu repo local
2. `git commit` con el mensaje descriptivo
3. `./gradlew buildPlugin` regenera el .zip
4. Ve a la pagina del plugin en el marketplace
5. Sube el nuevo .zip (incrementa `version` en `gradle.properties`)
6. JetBrains revisa y aprueba

### 9.3. Promocion del curso

Una vez publicado:

- Anade el badge al README: `[![JetBrains Plugin](https://img.shields.io/badge/JetBrains-Plugin-blue)](https://plugins.jetbrains.com/plugin/pa.meduca.programacion-ii)`
- Comparte el link en colegios de Panama
- Anade el link en tu LinkedIn como proyecto educativo
- Comenta a colegas docentes del MEDUCA

---

## Preguntas frecuentes

### ¿Que pasa si JetBrains rechaza la publicacion?

- Leen los logs y comentarios que envian
- Corrige lo solicitado
- Vuelve a subir
- Tipico: les toma 1-3 dias responder

### ¿Cuanto cuesta subir un plugin?

- **Gratis** para plugins libres sin monetizacion
- Si quieres cobrar por el plugin, JetBrains se queda un % segun su politica

### ¿Puedo actualizar el plugin despues de publicado?

- Si, las veces que quieras
- Cada actualizacion pasa por revision (mas rapida que la primera)

### ¿Que version de PyCharm/IntelliJ soporta?

- Lo que indique el campo `idea-version` en plugin.xml
- Recomendado: `since-build=\"232.0\"` (IntelliJ 2023.2 en adelante)

### ¿Mi curso aparece en el IDE en espanol o en ingles?

- El **contenido** del curso aparece en el idioma que escribiste (espanol)
- La **interfaz del plugin** (botones, menus) aparece en el idioma del IDE

---

## Soporte

Si te quedas atascado en algun paso:

- **Documentacion oficial**: <https://plugins.jetbrains.com/docs/marketplace/>
- **Foro de creadores de cursos**: <https://discuss.jetbrains.com/c/jetbrains-academy/52>
- **Email de soporte de JetBrains Academy**: <[email protected]>

---

**Ultima actualizacion**: Julio 2026
**Autor del curso**: Cristian Asprilla
**Basado en**: Template oficial de JetBrains Academy (MIT License)
