
🎬 CINE BROTHERS - Catálogo de Directores y Películas

Cine Brothers es una plataforma administrativa para la gestión de contenido cinematográfico. Permite administrar un catálogo completo de directores y sus filmografías con una interfaz moderna basada en una estética de "Cine Premium" (Dorado, Negro y Neón).

Características Principales

👤 Gestión de Directores

CRUD Completo: Creación, lectura, actualización y eliminación de directores.

Perfiles Detallados: Vista individual con biografía y datos de nacionalidad.

Galería de Imágenes: Soporte para carga de fotografías de perfil mediante multipart/form-data.

Filmografía Dinámica: Visualización automática de las películas asociadas a cada director con efectos de iluminación Cian Neón.

🎥 Gestión de Películas

Catálogo General: Listado de todas las obras registradas.

Vinculación: Relación directa entre películas y sus respectivos directores.

🎨 Interfaz de Usuario (UI/UX)
Diseño Dark Mode: Estética basada en salas de cine de lujo.

Efectos Visuales:

Tarjetas con Zoom Progresivo al hacer hover.

Iluminación cian neón en elementos interactivos.

Bordes dorados para resaltar la identidad de marca.

🚀 Tecnologías Utilizadas

Frontend

React.js: Biblioteca principal para la interfaz.

Material UI (MUI): Sistema de componentes y estilizado.

Axios: Cliente HTTP para la comunicación con la API.

Backend

Django & Django REST Framework: API robusta y escalable.

Pillow: Procesamiento de imágenes para los posters y perfiles.

CORS Headers: Configuración para permitir el flujo de datos entre servidores.

🛠️ Instalación y Configuración
1. Clonar el repositorio
Bash
git clone https://github.com/MarlonArpi/Examen-Final.-Aplicaci-n-web-full-stack---Mateo-Marlon.git
cd DESARROLLO DE APLICACIONES WEB

3. Configurar el Backend (Django)
Bash
cd proyecto_cine-back
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

4. Configurar el Frontend (React)
Bash
cd proyecto_cine-front
npm install
npm run dev

📸 Vista Previa de la Interfaz
Directores: Lista con avatares circulares y bordes dorados. Detalles: Vista extendida con biografía y filmografía con efecto hover cian.

👨‍💻 Autor
Desarrollado con ❤️ por el equipo de Cine Brothers. (Mateo y Marlon)
