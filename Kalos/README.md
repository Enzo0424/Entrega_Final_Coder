# Kalos
Kalos es un proyecto creado como parte de la preentrega del curso de Python en Coder House. Este proyecto consiste en una interfaz web que permite al personal administrativo de una empresa crear, visualizar y modificar bases de datos de la empresa. Está construido utilizando Bootstrap como base.

## Comisión

47770

## Instalación

Sigue estos pasos para instalar y ejecutar Kalos en tu entorno local:

1. Clona este repositorio:
git clone https://github.com/Enzo0424/PreEntregaTercera_ELocatelli.git

markdown
Copy code

2. Asegúrate de cumplir con los requisitos de software necesarios.

3. Realiza las migraciones de la base de datos:
python manage.py migrate

markdown
Copy code

## Uso

1. Inicia el servidor con el siguiente comando:
python manage.py runserver


2. Abre tu navegador web y accede a la siguiente URL:
http://127.0.0.1:8000/AppKalos/

3. Navega por las secciones en la barra de navegación:

- **Inicio**: Información sobre el proyecto y quienes somos.

- **Pacientes**:
  - Cargar Paciente
  - Buscar Paciente por DNI

- **Profesionales**:
  - Buscar Profesional por profesión
  - Cargar Profesional nuevo

- **Cuenta**:
  - Si no estás loggeado:
    - Crear Cuenta
    - Iniciar Sesión
  - Si estás loggeado:
    - Ver Perfil
      - Editar Perfil
      - Cambiar la contraseña
    - Cerrar Sesión

- **Acerca de mi**:
  - Conocer al autor del proyecto

- **Ir Arriba**:
  - Scroller hacia arriba de la pagina

## Contribución

Por el momento, no se aceptan contribuciones al proyecto.

## Autor

- Enzo Locatelli

## Estado del Proyecto

Proyecto en desarrollo activo.

## Requisitos

- Python 3.11.6
- Django 4.2.5
- Db.sqlite3

## Contacto

Para preguntas o comentarios, puedes ponerte en contacto con Enzo Locatelli a través de correo electrónico: locatellienzor@gmail.com