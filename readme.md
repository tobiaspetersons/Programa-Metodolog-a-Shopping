# TRABAJO FINAL METODOLOGÍA DE LA PROGRAMACIÓN

## El sistema que estamos desarrollando está pensado para los shoppings de la ciudad de Rosario

Se utilizará para poder dar de alta, dar de baja y modificar locales, entre otras funciones detalladas posteriormente, y para esto será utilizado por el administrador del shopping y los dueños de los locales. Ademas, lo podran utilizar los clientes de dichos locales para poder buscar descuentos, y aplicarlos a sus compras.

El sistema tendrá 3 niveles de usuarios distintos: administrador, dueños de locales y clientes. Para ingresar a cada uno, se debera especificar usuario y contraseña del mismo en el login.

- __El administrador__ es quien gestionaria las ofertas de todos los locales del shopping de acuerdo a la politica comercial del mismo, aprobando o desaprobando dichos descuentos propuestos por los locales. El administrador tambien podra dar de alta/baja a los locales y tambien crear las cuentas de los dueños de locales para que accedan al sistema. Por ultimo, el administrador podra ver la utilizacion de los descuentos en los locales del shopping por medio de reportes brindados por el sistema. Al momento de hacer el sistema, ya va a estar creado el usuario y contraseña del administrador.

- __Los dueños de locales__ podran ingresar al sistema las promociones de sus locales, para que luego el administrador las apruebe o desapruebe, segun la politica comercial del shopping. Ademas, los dueños de locales, por medio del programa, aceptaran las solicitudes generadas por un clientes, o rechazarlas. Cada promocion va a tener categorias, como el rango de fecha que esta vigente, la categoria de cliente que puede acceder a la oferta, el dia de la semana que esta vigente la promocion y el texto que la describe.  Los dueños de locales, por último, podrán monitorear el uso de sus promociones por parte de los clientes mediante un reporte brindado por el sistema.

- __Los clientes__, para acceder al sistema, primero se deberan registrar con un mail y una contraseña a su gusto. Dentro del sisrema, podran consultar los descuentos vigentes en cada local, y al momento de realizar la compra, deberá ingresar el codigo del local que quiere comprar, y elegir la promocion que quiere aplicar (el sistema mostrará al cliente sólo las promociones que estén vigentes).
Por ejemplo, si un cliente es categoría ‘Premium’, puede acceder a todas las promociones del shopping; si un cliente es ‘Medium’ podrá acceder a las promociones de su categoría y a las promociones para clientes ‘Iniciales’; y si un cliente es ‘Inicial’ solo podrá acceder a las promociones dirigidas a clientes iniciales.

El camino básico de nuestro sistema es:

1. El administrador crea las cuentas de los dueños de locales y crea los locales.
2. El dueño del local crea descuentos.
3. El administrador aprueba descuentos.
4. El cliente se registra en el sistema.
5. El cliente consulta descuentos en los locales del shopping.
6. El cliente ingresa el código de un local y elige un descuento de ese local.
7. El dueño del local acepta el descuento solicitado por el cliente.
8. El dueño del local monitorea el uso de sus descuentos por parte de los clientes.
9. El administrador monitorea el uso de los descuentos y en todo el shopping.

### EN RESUMEN

__Como administrador, se podrá:__

- Crear, editar y eliminar locales.
- Crear cuentas de dueños de locales.
- Aprobar o denegar una solicitud de descuento de un local.
- Ver reportes acerca de la utilización de los descuentos.

__Como dueño de local, se podrá:__

- Crear, editar y eliminar descuentos del local.
- Aceptar o rechazar una solicitud de descuento de un cliente.
- Ver la cantidad de clientes que usaron un descuento.

__Como cliente, se podrá:__

- Registrarse en el sistema para acceder a las ofertas del shopping.
- Buscar descuentos en los locales del shopping.
- Ingresar el nombre de un local y elegir un descuento disponible.

## MENU DE OPCIONES

El programa mostrará un menú con 3 opciones:

```python
1. Ingresar con usuario registrado
2. Registrarse como cliente
3. Salir
```

Si el operador elige la opción 3, abandonan el programa.

Si el operador elige la opción 2, el programa deberá permitir crear un usuario de tipo ‘Cliente’ que no exista actualmente. Para ello deberán ingresar un mail (no debe existir otro usuario igual), clave.

Luego de crear exitosamente el cliente, se vuelve al menú anterior de 3 opciones para que el cliente recién creado pueda ingresar con su usuario y contraseña respectiva.

Si el operador elige la opción 1, se le solicitará su usuario y contraseña.
Deben verificar que existan el usuario y su clave guardado en el sistema, y de acuerdo al tipo de usuario que está ingresando, presentar el menú correspondiente.

Segun el tipo de usuario que ingrese, se mostrara alguno de los siguientes menús:

MENU DE ADMINISTRADOR:

```python
1. Gestión de Locales
    a) Crear Locales
    b) Modificar Local
    c) Eliminar Local
    d) Volver
2. Crear cuentas de dueños de locales
3. Aprobar / Denegar solicitud de descuento
4. Reporte de utilización de descuentos
0. Salir
```

MENU PARA DUEÑO DE LOCAL:

```pyhton
1. Gestión de Descuentos
    a) Crear descuento para mi local
    b) Modificar descuento de mi local
    c) Eliminar descuento de mi local
    d) Volver
2. Aceptar / Rechazar pedido de descuento
3. Reporte de uso de descuentos
0. Salir
```

MENU PARA CLIENTE

```python
1. Buscar/solicitar descuentos
0. Salir
```

instalar dateutil.
