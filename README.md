# Primera Entrega

### Fernando Luna y Fernando Gomez

## Requisitos:
1. Herencia de templates
2. Por lo menos 3 clases en models.
3. Un formulario para insertar datos en todas las clases de tu models.
4. Un formulario para buscar algo en la BD.
5. Readme que indique el orden en el que se prueben las cosas y/o donde están las funcionalidades.

## Recorrido:

### Herencia de Templates
En la carpeta _"/templates/"_ se encuentra el archivo _baseTemplate.html_ el cual define la estructura y el estilo del sitio. El mismo contiene la barra de navegación con los enlaces necesarios para navegar por la web, y además un footer. Los subsiguientes archivos HTML heredan estos elementos del template base para mantener la estética y facilitar la navegación.

### Clases en Models y Formularios
El archivo _"models.py"_ contiene 3 clases utilizadas en esta web. <br>
- Posts  <br>
- Users  <br>
- Reviews  <br>
Cada una contiene su respectivo formulario para crear objetos nuevos.
#### Posts
La clase Posts puede visualizarse ingresando al item **PERFIL** en la barra de navegación. En esta vista se encuentra la simulación del perfil de un usuario, y a su derecha se encuentran todos los posteos encontrados en la DB, y por encima de ellos se encuentra el botón **Nuevo Post**, clickeando en él se accede a un formulario que solicita un Título, un Subtítulo, y un Contenido para el post. Si se regresa al **PERFIL**, este se encontrará actualizado con el post nuevo creado recientemente.

#### Users
La clase Users puede visualizarse ingresando al item **USUARIOS** en la barra de navegación. En esta vista se encuentra la lista completa de usuarios separados en tarjetas que contienen el nombre, una breve descripción, una fecha genérica de creación de cuenta y un botón para dirigirse al perfil. Para crear un nuevo objeto Usuario se debe clickear en el botón de **LOGIN** en la barra de navegación y luego en el modal seleccionar la opción de **Registrarse** en la zona inferior del mismo, esto te redirigirá a un formulario de creación de usuarios. Al completar los campos y clickear en **Registrarse**, si se regresa al apartado **USUARIOS** se podrá visualizar la lista actualizada de usuarios incluyendo el recientemente creado.

#### Reviews
La clase Reviews puede visualizarse ingresando al item **REVIEWS** en la barra de navegación. En esta vista se encuentra la lista completa de reviews ingresadas por los usuarios. Para crear un nuevo objeto Review se debe ingresar al botón **Deja tu Opinión** ubicada en la zona superior de la vista, esta te redirigirá a un formulario en el cual puedes ingresar tu nombre, un puntaje en estrellas limitado entre 1 y 5, y una review personalizada. Al clickear en **Enviar**, tu review quedará guardada y podrás visualizarla regresando al item **REVIEWS**.

### Búsqueda en la BD

La barra de navegación, en su lado derecho, contiene un pequeño formulario de búsqueda el cual busca en la DB los posteos que contengan la palabra o frase indicada. Los resultados se mostraran en una nueva vista.

<br>
<br>
<br>

Gracias por leer, espero que te haya gustado el progreso de la web. Los comentarios y sugerencias son más que bienvenidos!
