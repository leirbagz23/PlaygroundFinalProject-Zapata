# PlaygroundFinalProject-Zapata
## Playground Final Project Gabriel Zapata
## Curso de Python CoderHouse Comisión 56045
El proyecto final consiste en la elaboración de un sitio web utilizando el framework Django.
Mi sitio web consise en un tracker o regisrador de lecturas, el cuál permite almacenar 4 tipos diferentes de  lecturas:
* Libros abandonados
* Libros leidos
* Libros en lectura actual
* Libros por leer
Paso a realizar una descripción de las distintas páginas que componen el sitio web y como navegar entre ellas:
Una vez puesto en marcha el servidor, la página central es **/home/**
![Página /home/ 1/](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/d4cd2095-32e4-40df-ae2f-f2aa7c8cf212)
Utilizando los enlaces ubicados en la parte superior (los cuales son comunes a todas las vistas) se puede acceder a las siguientes páginas:
**Página /aboutme**: En esta página se puede consultar una breve reseña acerca del autor del sitio web (AKA yo)
![Página /aboutme](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/88dff2ff-41ee-4304-b789-ff2badf9d36c)
Para poder acceder al resto de las páginas (además de poder visualizar un resumen de los registros de lecturas en la página **/home/**) es necesario registrarse, para lo cuál se debe dirigir a la página **/login/** a través del enlace **Iniciar Sesión**
![Página /home/ 2](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/4fd680c9-c68c-4e25-8ca4-df403cbff08b)
![Página /login/](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/466cdf38-8695-4a3c-aca5-431d2199a251)
En dicha página, a  través del enlace **Registrarse** se accede a la página **/registro/**, dónde se puede hacer el registro al sitio web, permitiendo acceder a todas las funcionalidades.
![Página /registro/](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/8500bd22-a2f9-4033-a85a-824ff9be7091)
Una vez registrado en el sitio, basta con acceder de nuevo a la página **/login** para asi iniciar sesión y poder navegar completamente en el sitio (Si se intente acceder a una página restringida sin estar logueado, la misma redirigirá a esta página también)
Al estar logueado en el sitio, en la página **/home/** se puede observar un resumen de los elementos registrados en las diferentes BBDD.
![Página /home/ 3](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/2cc5b1cc-7b06-406b-bcf7-2add24c9f65e)
A través de los enlaces **Abandonados**, **Leidos**, **Leyendo** y **Por Leer** se puede acceder a las páginas **/abandonados/**, **/leidos/**, **/leyendo/** y **/porleer/** respectivamente, las cuáles cuentan con las siguientes funcionalidades:
* Registro de una lectura a la BBDD asociada a la página a través de un formulario dónde se ingresan los datos del libro: **Titulo**, **Autor** Y **Año de Publicación**
![Registro de lectura](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/ab2d574f-3d7b-4c76-af34-fab9d7002d5f)
* Visualización, edición y borrado de los diferentes registros de la BBDD asociada a la página
![Visualización, edición y borrado de registros](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/bb351585-2577-4d7f-b999-4ebd62624d95)
En el enlace **Búsqueda** se accede a la página **/busqueda/** la cuál contiene un formulario que permite realizar búsquedas en las diferentes BBDD utilizando **Titulo**, **Autor** o **Año de Publicación** cómo parámetros de entrada.
![Búsqueda en las BBDD](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/942ecf93-a510-45f2-9a09-e6418ae278ec)
![Resultados de la búsqueda](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/cce13790-5629-4e71-8743-dbee8d4d0b9f)
Finalmente, el enlace **Cerrar Sesión** (Que se habilita cuándo el usuario está logueado en el sitio) permite hacer el respectivo deslogueo.
![Cierre de sesión](https://github.com/leirbagz23/PlaygroundFinalProject-Zapata/assets/148101637/f2ee3ee1-7ab5-484e-8470-954fd9bc2819)







 




  
