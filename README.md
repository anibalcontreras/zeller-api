# Instrucciones para correr el código

Se usa pipenv para manejar las dependencias necesarias para ejecutar el proyecto. De esta forma, los comandos a ejecutar son los siguientes:

```
pipenv install
```

```
pipenv shell
```

```
python manage.py migrate

```

```
python manage.py runserver
```

Se tiene que tener liberado el puerto 8000.

Si se quiere manipular la base de datos para editar, crear o eliminar datos se puede acceder a la ruta /admin/ e ingresar con el usuario "admin" y contraseña "admin".

# Producción

La aplicación fue deployeada en render y la url es la siguiente:
https://zeller-api.onrender.com

# Link Documentación Endpoints

https://documenter.getpostman.com/view/39549389/2sAY518Kpn

# Comentarios

Dado que use python, me pareció mas correcto por convención usar snake_case, por lo que atributos como dueDate o sentAt se llaman due_date y sent_at respectivamente.

Debido a que use Django, que contiene un messages por default, todo lo que hace referencia a messages en el enunciado fue renombrado por conversations.

Por otro lado, para seguir principios SOLID, la creación de clientes, conversations y debts se hacen de forma separada (se puede revisar la documentación para mayor información). De esta forma hay tres endpoints posts:

- POST /clients/: Con esto se crea un cliente sin deudas y sin conversations
- POST /clients/<id>/conversations/: Se crea una conversación para el cliente con el id correspondiente
- POST /clients/<id>/debts/: Se crea una deuda para el cliente con el id correspondiente

Los body son los mismos que se sugieren en el enunciado.

También el endpoint GET /clients-to-do-follow-up fue cambiado por GET /clients/to-do-follow-up/
Además, se agregó el endpoint GET /GET /clients/has-active-debts/ para ver los clientes que tienen deudas activas (y así saber que id usar para obtener la respuesta del asistente donde menciona que no tiene acceso a financiamiento).

# Explicación modelo utilizado

Se escogió el modelo GPT-4o mini dado que es un modelo económico en términos de token. La respuesta que da el asistente de una automotora no requiere un razonamiento muy elaborado, por lo que me pareció la mejor opción.

# Explicación de como se generó el prompt

A grandes rasgos, lo que se hizo es tener un archivo branches.json, que tiene solo una automotora (Kaufmann) que tiene 3 branches y cada branch tiene autos de la marca Mercedes Benz y distintos modelos. Con esto se tienen los autos disponibles en la automotora. Luego, con el id de la URL se obtiene el nombre del cliente, para así saludarlo por su nombre y sea un tono mas cercano. Además, se tiene un método que permite determinar si el cliente tiene morosidad (Es decir, si a la fecha que se hace la request, tiene deudas con due_date menores a la fecha actual). Con esto se hicieron dos tipos de prompts, el primero es para clientes sin morosidad, que se le insiste al asistente que el cliente tiene posibilidad de financiamiento debido a que es un cliente responsable. Por otro lado, si el cliente es moroso, se le recuerda que tienes deudas por lo que no puede acceder al financiamiento. De todas formas, se le comunica de forma amable que si no sabía de la situación, que no dude comunicarse para ayudarlo a saldar sus deudas y así obtener un financiamiento para comprar su nuevo auto. A los dos tipos de clientes se les menciona los autos que están disponibles en las distintas sucursales de Kaufmann. No le incluí un nombre al asistente virtual, ya que me daba la impresión de que quedaba mas robotizado que sin nombre.

# Ejemplos

A la pregunta de ¿Que autos tienen disponibles?, el asistente responde:

- Para el caso de un cliente moroso

```
{
    "text": "Hola, Juan. Actualmente tenemos los siguientes autos disponibles en nuestras sucursales:\n\n**Sucursal Sur:**\n- Mercedes Benz Clase A (nuevo)\n- Mercedes Benz GLC Coupe AMG (nuevo)\n\n**Sucursal Central:**\n- Mercedes Benz Clase G (nuevo)\n\n**Sucursal Norte:**\n- Mercedes Benz EQS (nuevo)\n\nTe recuerdo que, debido a tu situación actual, puedes explorar el catálogo completo de autos, pero no tendrás acceso a opciones de financiamiento hasta que regularices tus pagos. Una vez que estés al día, podrás ser considerado para financiamiento en el auto que más te guste.\n\nSi necesitas más información sobre cómo regularizar tus pagos, no dudes en contactarme al +56 9 1234 5678. ¡Estoy aquí para ayudarte!"
}
```

- Para el caso de un cliente sin morosidad

```
{
    "text": "Hola, Pedro Bustamante. ¡Gracias por ponerte en contacto con Kaufmann! Actualmente, contamos con los siguientes modelos disponibles en nuestras sucursales:\n\n- **Sucursal Sur**: \n  - Mercedes Benz Clase A (nuevo)\n  - Mercedes Benz GLC Coupe AMG (nuevo)\n\n- **Sucursal Central**: \n  - Mercedes Benz Clase G (nuevo)\n\n- **Sucursal Norte**: \n  - Mercedes Benz EQS (nuevo)\n\nAdemás, quiero compartirte una excelente noticia: debido a tu historial financiero positivo, tienes opciones de financiamiento disponibles para adquirir el auto que prefieras. Esta es una ventaja especial para ti, por tu buen comportamiento financiero. Si necesitas más información o deseas agendar una visita, ¡estaré encantado de ayudarte!"
}
```

# Mejoras o Extensiones que se podrían hacer

Es peculiar que uno tenga que hacer un GET para tener una respuesta de un asistente virtual. El modelo debería estar entrenado de antes con RAG para tener las capacidades de un modelo de AI generativa, pero además tener la información propia de la automotora, como lo son los modelos que tienen en sus sucursales, así se tienen todos los beneficios del modelo estándar de GenAI para responder de forma natural, pero se ciñe a la información propia de la automora para dar a los clientes la respuesta mas acertada acorde a la realidad. Además, con un entrenamiento previo se puede evitar sobrecargar en cantidad de tokens cada vez que se hace una request, puesto que actualmente cada vez que se hace una request se leen todas las marcas y modelos actuales, haciendolo ineficiente y costoso.

Por otro lado, la idea es que la API permita que la interacción sea tipo chatbot. Actualmente la implementación no es así, se supone que el cliente siempre quiere saber los autos que tienen disponibles. Además, probablemente un cliente solo quiera saber la disponibilidad en una sucursal específica y no saber todos los autos que tienen disponible la automora.

Una mejora que se puede implementar es agregar a Client mas atributos, tales como edad, sexo, comuna, trabajo, entre otros, para así hacerle recomendaciones mas específicas respecto a los autos que les pueda interesar. Por ejemplo, si se tiene a un hombre de 35 años que vive en Temuco y trabaja en el sector de agricultura, se le podría poner mas énfasis en recomendarle la pickup clase X, dado que es probable que le pueda interesar mas que un clase S.
