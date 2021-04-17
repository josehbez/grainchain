 uvicorn app:app --reload --port 8022


Su código debe incluirse debajo de este encabezado, puede crear tantas celdas como sea necesario, incluido el código y el marcado para explicar su enfoque y darnos su opinión.

Lea atentamente las siguientes instrucciones, su tarea es crear una nueva API desde cero para manejar la información interna del usuario:

1. Existe una aplicación adicional, denominada Zeta. Tiene una API que utilizará para obtener información y validación adicional del usuario. Consulte ZetaAPI.ipynb, este cuaderno contiene la información requerida en un ejemplo en ejecución.
2. Los puntos finales deben desarrollarse para crear, editar y eliminar información básica del usuario. Debe incluir ubicación, nombre, nombre de usuario y una estructura que contenga la información del usuario obtenida de la aplicación Zeta. Consulte MongoDB.ipynb, este cuaderno contiene la información requerida en un ejemplo en ejecución.
3. Utilice las celdas debajo de FastAPI Start and Endpoint Tests como guía, los extremos esperados y las respuestas ya están allí.
4. Se debe desarrollar un punto final para crear 100 usuarios falsos, todos los campos deben contener datos y cada usuario debe estar asignado a una ubicación aleatoria.
5. Se debe desarrollar un punto final para proporcionar un informe que contenga la cantidad de usuarios vinculados a cada ubicación disponible, también se debe devolver el recuento de documentos de usuario almacenados y el informe debe incluir al menos diez ubicaciones falsas.
6. Todas las pruebas del bloque Prueba de tareas deben aprobarse.
7. No se esperan usuarios anteriores al inicio, la colección MongoDB debe estar vacía. Siéntase libre de crear y usar la información como mejor le parezca para su prueba, solo tenga esto en cuenta para propósitos de entrega.


# a
# b
# Original
<ol>
    <li>An additional application exists, named <i>Zeta</i>. It has an <i>API</i> thay you will use to get additional user information and validation. See <i>ZetaAPI.ipynb</i>, this notebook contains the information required in a running example.</li>
    <li>Endpoints must be developed to create, edit, and delete basic user information. You must include location, name, username, and a structure contain user information obtained from the <i>Zeta</i> application. See <i>MongoDB.ipynb</i>, this notebook contains the information required in a running example.</li>
    <li><u>Use the cells under the <b>FastAPI Start and Endpoint Tests</b> as guidance</u>, the expected endpoints and responses are already there.</li>
    <li>An endpoint must be developed to create 100 fake users, all fields must contain data and each user must be assigned to a random location.</li>
    <li>An endpoint must be developed to provide a report containing the amount of users linked to each location available, the count of user documents stored must be returned as well and the report must include at least ten faked locations.</li>
    <li><u>All tests in the <b>Task Testing</b> block must pass</u>.</li>
    <li><u>No previous users are expected on start</u>, the <i>MongoDB</i> collection must be empty. Feel free to create and use information as you see fit for your test, just take this in consideration for delivery purposes.</li>
</ol>