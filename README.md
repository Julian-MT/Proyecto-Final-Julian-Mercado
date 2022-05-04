# Proyecto-Final-Julian-Mercado-Tawil
Proyecto final de web para empresa de agricultura de precision.

## Introduccion ##
Esta plataforma, esta pensada para acoplarse a una empresa real, en la que trabajo actualmente y que ofrece el servicio de 
relevamientos aereos mediante el vuelo de drones de imagenes en campos agricolamente productivos.

El funcionamiento basico de la empresa consiste en mantener reuniones con los distintos clientes, captar cual es el servicio 
que estan solicitando, realizar el relevamiento y compartir con ellos la informacion mediante un link a la plataforma en la cual
procesamos las imagenes aereas.

Esta ultima parte, suele realizarse via mail o Whatsapp, por lo que es comun que la informacion se pierda en la voragine del dia a dia. Es por esto, que pense en esta plataforma, para que cada lote quede registrado junto a su link de proyecto y en un futuro tambien pueda asociarse archivos pdf a los mismos, a modo de informes de relevamiento.

Creo que la aplicacion cumple con los requerimientos basicos para la misma, siendo robusta en cuanto a necesidad de LogIn y a los posibles errores por la manipulacion de base de datos.

## FUNCIONAMIENTO ##

La pagina cuenta con una vista de inicio, que al igual que las vistas de informacion, de login y de consultas es accesible a usuarios no logeados. 
En la vista de LogIn, contamos con la posibilidad de acceder a nuestra cuenta o de registrar nuevos usuarios. Una vez que accedemos, aparecen las funciones de hacer LogOut o de ver los lotes registrados. Para ver los lotes registrados o crear nuevos lotes, primero sera necesario asignar un cliente al nuevo usuario creado. En esa Vista que se enlistan los lotes, a cada uno se le asigna la opcion de ver en detalle, editar o eliminar. Ante cada accion que realiza el usuario, la plataforma redirigira a una vista que tendra una notificacion especifica.

## Robustecimiento ##

La app conto con algunos problemas iniciales que se fueron solucionando:

    -Asociar un cliente a un usuario funcionaba, pero recuperar la lista de lotes asociada a un usuario daba error. Esto se soluciono asegurando la recuperacion del id del cliente para la generacion de la lista en vez del id del usuario.

    -Cuando un usuario queria ver lotes registrados antes de asociar un cliente  a su cuenta, daba error. Se realizo una comprobacion de esto mediante un try, que ante el error redirige al usuario al registro de Cliente.

    -Mediante un try me asegure que cada usuario solo pueda tener un cliente asignado y se le notifique si es que intenta asignar uno nuevo.

    -Se intento que las consultas estuvieran disponibles para hacer en todas las vistas, poniendo un formulario en el footer del template padre. Sin embargo cada vez q se llenaba el formulario aparecia un error porque la url terminaba siendo distinta a la asignada para esa funcion. Esto se soluciono reemplazando el formulario por un boton que redirige al usuario a una vista especifica para realizar consultas.

## Consideraciones ##

Ante el intento de comunicarme con mis compañeros de grupo via Slack y no obtener respuesta, realice el trabajo de manera individual, maniobrando entre el trabajo y programacion.

Muchas Gracias!!!
