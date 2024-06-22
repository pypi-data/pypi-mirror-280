![Gravitad Logo](https://github.com/alexjszamora78/Gravitad/blob/main/resources/logo.jpg)

--------------------------------------------------------------------------------

**Gravitad es una librería de código abierto que fusiona la robustez de PyTorch con la precisión de los modelos ARIMA para la predicción de series temporales.  Su chatbot, entrenado con PyTorch, proporciona información personalizada, mientras que su módulo ARIMA ofrece predicciones precisas para diversos campos como finanzas, clima, tráfico, etc.**


### Tabla de Contenido

<!-- toc -->

- [Version](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#version-10)
- [Crear un Entorno Virtual](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#crear-un-entorno-virtual)
- [Instalar dependencias](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#instalar-dependencias-necesarias)
- [ChatBot](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#chatbot)
	- [Crear Archivo JSON](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#chatbot)
	- [Ejemplo de config.json](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#ejemplo-de-configjson)
	- [Ejecución](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#ejecuci%C3%B3n)
	- [Output](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#output)
	- [¿ Cuándo usar ChatBot como solución para proyectos ?](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#-cu%C3%A1ndo-usar-chatbot-como-soluci%C3%B3n-para-proyectos-)
	- [Ejemplo proyecto 038](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#ejemplo-de-uso-tomando-como-ejemplo-el-proyecto-038)
	- [Plantilla del JSON](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#plantilla-del-json)
	- [config.json con los datos proporciondos por Scrapping](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#ejemplo-del-configjson-con-los-datos-proporciondos-por-el-grupo-de-scrapping)
	- [Ejecución de la prueba 038](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#ejecuci%C3%B3n-de-la-prueba-038)
	- [Output](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#output-1)
- [Arima Time Predictor (ATP)](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#arima-time-predictor-atp)
	- [Componentes de ARIMA](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#arima-tiene-tres-componentes)
	- [Archivo CSV](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#archivo-csv)
	- [Ejecución](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#ejecuci%C3%B3n-1)
	- [Output](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#output-2)
	- [Parámetros Adicionles](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#par%C3%A1metros-adicionales)
	- [¿ Cuándo usar ArimaTP como solución para proyectos ?](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#-cu%C3%A1ndo-usar-arimatp-como-soluci%C3%B3n-para-proyectos-)
- [Información para Desarrolladores (DEV)](https://github.com/alexjszamora78/Gravitad?tab=readme-ov-file#informaci%C3%B3n-para-desarrolladores-dev)
<!-- tocstop -->

--------------------------------------------------------------------------------

## Versión 1.0

## Crear un entorno virtual

```bash
python -m venv env
source env/bin/active
```


## Instalar dependencias necesarias

```bash
pip install Gravitad
```

# ChatBot:

```python
#importamos la libreria Gravitad para uso del ChatBot
from Gravitad import ChatBot
````

## Crear archivo json
Se debe crear un archivo config.json con las preguntas y respuestas previamente formuladas para el aprendizaje del modelo
La estructura de este JSON debe seguir estas pautas

```json
[
    {
      "tag": "saludo",
      "patterns": [
        "Hola",
        "Buenos días",
        "¿Cómo estás?"
      ],
      "responses": [
        "¡Hola! ¿En qué puedo ayudarte hoy?",
        "¡Buenos días! ¿Cómo puedo asistirte?",
        "Estoy aquí para ayudarte. ¿En qué puedo colaborar contigo?"
      ]
    }
]
```

Los tag son el ID del tipo de interacción que se esta realizando.
Los patterns son los patrones de entra del input dele usuario.
Los responses son un conjunto de respuestas que el modelo puede usar para retonar

## **Ejemplo de config.json**

```json
[
    {
      "tag": "saludo",
      "patterns": [
        "Hola",
        "Buenos días",
        "¿Cómo estás?"
      ],
      "responses": [
        "¡Hola! ¿En qué puedo ayudarte hoy?",
        "¡Buenos días! ¿Cómo puedo asistirte?",
        "Estoy aquí para ayudarte. ¿En qué puedo colaborar contigo?"
      ]
    },
    {
      "tag": "despedida",
      "patterns": [
        "Adiós",
        "Hasta luego",
        "Nos vemos luego"
      ],
      "responses": [
        "¡Adiós! Que tengas un buen día.",
        "¡Hasta luego! No dudes en volver si necesitas ayuda.",
        "Nos vemos pronto. ¡Cuídate!"
      ]
    },
    {
      "tag": "ayuda",
      "patterns": [
        "Necesito ayuda",
        "Puedes ayudarme",
        "Quiero que me ayudes",
        "¿Podrías ayudarme?",
        "¿Podrías aconsejarme?",
        "¿Podrías darme un aconsejo?",
        "Dame un consejo"
      ],
      "responses": [
        "¡Claro! ¿Qué ocurre?",
        "¡Sí, por supuesto! ¿Pasa algo?",
        "¡Sí! ¿Te sientes mal?",
        "¡Sí! Cuentame por favor, estoy para ayudarte.",
        "¡Por supuesto! ¿En qué puedo ayudarte?",
        "¡Por supuesto! Cuentame tu situación, por favor.",
        "¡Por supuesto! Estoy para ayudarte, cuéntame sobre tu situación.",
        "¡Por supuesto! Dime como te sientes y qué podría ayudarte."
      ]
    },  
    {
      "tag": "definicion_burnout",
      "patterns": [
          "¿Qué es el burnout?",
          "¿Cómo puedo reconocer si estoy experimentando burnout?",
          "Señales de burnout"
      ],
      "responses": [
          "El burnout es un estado de agotamiento físico, emocional y mental causado por el estrés crónico en el trabajo.",
          "Algunas señales de burnout incluyen el agotamiento constante, la falta de motivación, la irritabilidad, el aislamiento social y la disminución del rendimiento laboral.",
          "Si te sientes abrumado, desmotivado y agotado física y emocionalmente, es posible que estés experimentando burnout. Es importante buscar apoyo y tomar medidas para cuidar tu bienestar."
      ]
    },
    {
      "tag": "ansiedad",
      "patterns": [
        "Siento que no puedo concentrarme en el trabajo.",
        "Estoy constantemente preocupado por mi desempeño laboral.",
        "Me cuesta trabajo relajarme después de un día de trabajo intenso."
      ],
      "responses": [
        "Prueba técnicas de respiración profunda para reducir la ansiedad.",
        "Haz pausas cortas durante el día para desconectar y relajarte.",
        "Habla con tu supervisor sobre cómo te sientes, podría ofrecerte apoyo adicional."
      ]
    },
    {
      "tag": "depresion",
      "patterns": [
        "Me siento mal",
        "No me siento del todo bien",
        "Siento que mi trabajo no tiene sentido o propósito.",
        "No tengo energía para enfrentar mis responsabilidades laborales.",
        "Me siento abrumado y sin esperanza en mi trabajo."
      ],
      "responses": [
        "Considera hablar con un terapeuta o consejero para obtener apoyo emocional.",
        "Busca actividades que disfrutes fuera del trabajo para mejorar tu estado de ánimo.",
        "Habla con recursos humanos sobre la posibilidad de ajustar tu carga de trabajo si te sientes abrumado."
      ]
    },
    {
      "tag": "estres",
      "patterns": [
        "Me siento constantemente tenso y nervioso en el trabajo.",
        "Tengo dificultades para conciliar el sueño debido al estrés laboral.",
        "Siento que tengo demasiadas tareas y plazos para cumplir."
      ],
      "responses": [
        "Haz ejercicio regularmente para liberar tensiones y reducir el estrés.",
        "Practica técnicas de manejo del tiempo para priorizar tareas y evitar la sobrecarga.",
        "Considera hablar con tu supervisor sobre la redistribución de tareas si te sientes abrumado."
      ]
    }
]
```

## **Ejecución**

```python
from Gravitad import ChatBot

response = ChatBot("config.json")
```

## **Output**

![Output](https://github.com/alexjszamora78/Gravitad/blob/main/resources/output.png)


## **¿ Cuándo usar ChatBot como solución para proyectos ?**

* **Servicio de atención al cliente 24/7:** Para responder preguntas frecuentes, resolver problemas básicos, guiar al usuario por el sitio web, recomendar productos, responder preguntas de envíos y devoluciones, etc.

* **Agendar Citas:** Puedes usarlo como alternativa para gestionar la agenda, programar citas y enviar recordatorios.

* **Captación de clientes potenciales:** Puede recopilar información y datos del usuario para clasificarlos.

* **Asistente virtual:** Para ayudar a los usuarios a crear listas de tareas, gestionar su tiempo, etc.

* **Educación y formación:** Para proporcionar respuestas rápidas a preguntas, explicación de conceptos y apoyo en el aprendizaje. Para enseñar a aprender idiomas, matemáticas, etc.

* **Juegos Interactivos:** Para crear o predecir experiencias de juego y usuario más inmersas y personalizadas.

* **Marketing y Publicidad:** Para segmentar la audiencia y ofrecer mensajes personalizados acordes a ella.

* **Investigación de mercado:** Para recopilar opiniones de los usuarios sobre productos o servicios. 

* **Reservas de viajes:** Para reservar vuelos, hoteles, coches y otros servicios turísticos. 

* **Asistencias de compras online:** Para encontrar productos, comparar precios y obtener recomendaciones personalizadas. 

* **Entretenimientos:** Para jugar juegos, contar historias, dar predicciones de gustos sobre las mejores o peores (mediante un filtro) películas y libros, etc.

* **Gestión de redes sociales:** Para responder a los mensajes, publicar contenido, analizar datos, etc.


## Ejemplo de uso tomando como ejemplo el proyecto 038.

El Objetivo general del [Proyecto 038](https://github.com/alexjszamora78/Gravitad/blob/main/resources/Documento038.docx) es Desarrollar una plataforma integral de **análisis predictivo** y experiencia de usuario en comercio electrónico que emplee técnicas avanzadas de recopilación y análisis de datos para **predecir** el comportamiento del usuario, ofrecer recomendaciones personalizadas y mejorar la interacción en el sitio web, optimizando así la navegación y la experiencia de compra para aumentar la satisfacción del cliente y potenciar el rendimiento del comercio electrónico.

* Se toma en cuenta que lo que se quiere es predecir, pronosticar y una de las posibles soluciones es la utilización del ChatBot

* Primeramente se tendría que crear la configuración (JSON) correspondiente pra entrenar al modelo de aprendizaje

## Plantilla del JSON
```json
[
    {
      "tag": ...,
      "patterns": [
        ...
      ],
      "responses": [
        ...
      ]
    }
]
```

* En el tag se debe poner una palabra clave para el uso que se está empleando, en este caso se pudiera usar la categoría del profucto o servicio

* El patterns son los gusto o preferencias del usuario que en la tabla de interés aparece como (userInterests) **Intereses del Usuario** 

* Los respondes son productos o servicios que está brindando la Empresa y que en la tabla de interés aprece como (comProducts) y (comServices) respectivamente

* Solo quedaría pasar esos valores proporciondos por el grupo de Scrapping para el config.json


## **Ejemplo del config.json con los datos proporciondos por el grupo de Scrapping**

```json
[
    {
	  "tag": "tecnologia",
	  "patterns": [
	    "teléfonos inteligentes",
	    "portátiles",
	    "auriculares inalámbricos",
	    "altavoces inteligentes",
	    "tabletas",
	    "smartwatches",
	    "cámaras digitales",
	    "impresoras",
	    "componentes de PC"
	  ],
	  "responses": [
	    "Teléfono inteligente de última generación con cámara de alta resolución y procesador potente",
	    "Portátil ultradelgado y ligero con pantalla de alta definición y gran autonomía",
	    "Auriculares inalámbricos con cancelación de ruido activa y sonido de alta fidelidad",
	    "Altavoces inteligentes con asistente de voz y conectividad Bluetooth",
	    "Tablet con pantalla táctil de gran tamaño y sistema operativo Android",
	    "Smartwatch con funciones de seguimiento de actividad física y notificaciones",
	    "Cámara digital réflex con objetivo intercambiable y resolución de alta calidad",
	    "Impresora multifunción con conectividad inalámbrica y capacidad de impresión a doble cara",
	    "Componentes de PC de alta gama, incluyendo tarjeta gráfica, procesador, memoria RAM y almacenamiento SSD"
	  ]
	},
	{
	  "tag": "moda",
	  "patterns": [
	    "ropa para hombre",
	    "ropa para mujer",
	    "zapatos",
	    "bolsos",
	    "accesorios",
	    "ropa deportiva",
	    "trajes",
	    "vestidos de fiesta",
	    "jeans"
	  ],
	  "responses": [
	    "Camisasde algodón con diseños modernos y tallas para todos",
	    "Pantalones vaqueros ajustados, rectos o acampanados con diferentes lavados",
	    "Vestidos de verano de algodón fresco y colores vibrantes",
	    "Zapatos de tacón alto para ocasiones especiales",
	    "Bolsos de mano para mujer de diferentes tamaños y materiales",
	    "Ropa deportiva de alta calidad para correr, entrenar o hacer ejercicio",
	    "Trajes de chaqueta y pantalón elegantes para ocasiones formales",
	    "Vestidos de fiesta largos o cortos con diseños únicos y elegantes",
	    "Jeans de diferentes estilos, colores y tallas para hombre y mujer"
	  ]
	},
	{
	  "tag": "hogar",
	  "patterns": [
	    "muebles",
	    "decoración",
	    "textiles para el hogar",
	    "electrodomésticos",
	    "iluminación",
	    "artículos de cocina",
	    "alfombras",
	    "cortinas",
	    "cojines"
	  ],
	  "responses": [
	    "Sofá de cuero con diseño moderno y confortable para tu salón",
	    "Mesa de comedor de madera maciza para 6 personas",
	    "Lámparas de techo con diseño elegante y funcional para tu habitación",
	    "Electrodomésticos de última generación como lavavajillas, lavadora y secadora",
	    "Textiles para el hogar como sábanas, toallas y cortinas de alta calidad",
	    "Artículos de cocina como ollas, sartenes y cubiertos de acero inoxidable",
	    "Alfombras de diferentes materiales y estilos para tu hogar",
	    "Cortinas opacas o translúcidas para controlar la entrada de luz",
	    "Cojines decorativos con diferentes estampados y tejidos para tu sofá"
	  ]
	},
	{
	  "tag": "belleza",
	  "patterns": [
	    "productos de belleza",
	    "cosméticos",
	    "maquillaje",
	    "cuidado de la piel",
	    "cuidado del cabello",
	    "perfumes",
	    "productos para hombres",
	    "productos para mujeres"
	  ],
	  "responses": [
	    "Cremas faciales hidratantes y antiedad para todos los tipos de piel",
	    "Productos de maquillaje de alta calidad como sombras de ojos, labiales y bases",
	    "Champús y acondicionadores para el cuidado del cabello",
	    "Perfumes para hombre y mujer con aromas únicos y duraderos",
	    "Productos para el cuidado personal como desodorantes, jabones y cremas para manos",
	    "Productos de afeitado para hombres como espuma de afeitar y bálsamos después del afeitado"
	  ]
	},
	{
	  "tag": "libros",
	  "patterns": [
	    "libros de ficción",
	    "libros de no ficción",
	    "libros de texto",
	    "biografías",
	    "novelas",
	    "cuentos",
	    "poesía",
	    "libros infantiles",
	    "libros de cocina",
	    "libros de viajes"
	  ],
	  "responses": [
	    "Novela de misterio y suspense con giros inesperados",
	    "Biografía de un personaje histórico fascinante",
	    "Libro de cocina con recetas deliciosas y fáciles de seguir",
	    "Libro de viajes con consejos y recomendaciones para explorar el mundo",
	    "Libro infantil con ilustraciones coloridas e historias encantadoras",
	    "Libro de no ficción sobre un tema interesante y actual",
	    "Libro de texto para estudiantes de primaria, secundaria o universidad",
	    "Poesía contemporánea con versos emotivos y reflexivos",
	    "Colección de cuentos clásicos con moralejas para todos",
	    "Libro de autoayuda con consejos prácticos para mejorar tu vida"
	  ]
	},
	{
	  "tag": "viajes",
	  "patterns": [
	    "vuelos",
	    "hoteles",
	    "alojamientos",
	    "cruceros",
	    "viajes en tren",
	    "tours",
	    "paquetes vacacionales",
	    "rent a car",
	    "seguros de viaje",
	    "actividades turísticas"
	  ],
	  "responses": [
	    "Vuelos baratos a destinos nacionales e internacionales",
	    "Hoteles de lujo, boutique o económicos en diferentes ciudades",
	    "Alojamientos alternativos como apartamentos, villas o casas rurales",
	    "Cruceros por el Mediterráneo, Caribe o Alaska",
	    "Viajes en tren panorámicos por Europa",
	    "Tours guiados por las principales ciudades del mundo",
	    "Paquetes vacacionales personalizados para todos los gustos y presupuestos",
	    "Rent a car con diferentes modelos de vehículos",
	    "Seguros de viaje para cubrir imprevistos",
	    "Actividades turísticas como museos, parques temáticos o excursiones"
	  ]
	},
	{
	  "tag": "deportes",
	  "patterns": [
	    "ropa deportiva",
	    "calzado deportivo",
	    "accesorios deportivos",
	    "equipamiento deportivo",
	    "suscripciones a gimnasios",
	    "clases de fitness",
	    "material para deportes de equipo",
	    "material para deportes individuales",
	    "nutrición deportiva",
	    "complementos deportivos"
	  ],
	  "responses": [
	    "Ropa deportiva de alta calidad para correr, entrenar o hacer ejercicio",
	    "Calzado deportivo cómodo y resistente para diferentes disciplinas",
	    "Accesorios deportivos como relojes inteligentes, auriculares inalámbricos y cintas para el sudor",
	    "Equipamiento deportivo para gimnasio, yoga, pilates o entrenamiento en casa",
	    "Suscripciones a gimnasios con acceso a diferentes actividades",
	    "Clases de fitness como spinning, zumba o crossfit",
	    "Material para deportes de equipo como fútbol, baloncesto o voleibol",
	    "Material para deportes individuales como tenis, golf o natación",
	    "Nutrición deportiva para optimizar el rendimiento",
	    "Complementos deportivos para aumentar la energía, la fuerza o la recuperación"
	  ]
	},
	{
	  "tag": "entretenimiento",
	  "patterns": [
	    "películas",
	    "series de televisión",
	    "música",
	    "videojuegos",
	    "consolas de videojuegos",
	    "libros de cómics",
	    "entradas para eventos",
	    "instrumentos musicales",
	    "material de dibujo",
	    "juegos de mesa"
	  ],
	  "responses": [
	    "Películas de estreno en cine o en streaming",
	    "Series de televisión de diferentes géneros como drama, comedia o ciencia ficción",
	    "Música de todos los estilos, desde pop hasta rock o clásica",
	    "Videojuegos para PC, consola o móvil",
	    "Consolas de videojuegos de última generación como Playstation 5 o Xbox Series X",
	    "Libros de cómics de superhéroes, manga o novela gráfica",
	    "Entradas para conciertos, espectáculos teatrales o eventos deportivos",
	    "Instrumentos musicales como guitarras, pianos o baterías",
	    "Material de dibujo como lápices, colores, acuarelas o pinceles",
	    "Juegos de mesa para todas las edades, desde clásicos hasta modernos"
	  ]
	},
	{
	  "tag": "mascotas",
	  "patterns": [
	    "comida para mascotas",
	    "accesorios para mascotas",
	    "productos de higiene para mascotas",
	    "juguetes para mascotas",
	    "ropa para mascotas",
	    "camas para mascotas",
	    "servicios veterinarios",
	    "adopción de mascotas",
	    "cuidado de mascotas",
	    "adiestramiento de mascotas"
	  ],
	  "responses": [
	    "Comida para perros, gatos, conejos u otras mascotas",
	    "Accesorios para mascotas como collares, correas, arneses o transportines",
	    "Productos de higiene para mascotas como champús, cepillos o peines",
	    "Juguetes para mascotas de diferentes tamaños y materiales",
	    "Ropa para mascotas como abrigos, jerseys o impermeables",
	    "Camas para mascotas de diferentes tamaños y diseños",
	    "Servicios veterinarios como consultas, vacunas o cirugías",
	    "Adopción de mascotas de refugios o protectoras",
	    "Cuidado de mascotas a domicilio o en residencias",
	    "Adiestramiento de mascotas para corregir comportamientos y mejorar la convivencia"
	  ]
	}
]
```


## **Ejecución de la prueba 038**

```python
from Gravitad import ChatBot

response = ChatBot("config.json")
```


## **Output**

![Output](https://github.com/alexjszamora78/Gravitad/blob/main/resources/output2.png)


--------------------------------------------------------------------------------


# Arima Time Predictor (ATP)
Modelo de Promedio Móvil Integrado Autoregresivo. Es una técnica estadística utilizada para predecir valores futuros de una serie de tiempo. Es un modelo muy popular en el aprendizaje automático (ML) y se puede implementar en PyTorch.


## ARIMA tiene tres componentes:

* **AR (Autoregresivo):** Utiliza valores pasados de la serie de tiempo para predecir valores futuros. 

* **I (Integrado):** Remueve la tendencia de la serie de tiempo mediante diferencias.

* **MA (Promedio Móvil):** Utiliza valores pasados del error de la predicción para mejorar la predicción.

## Archivo CSV

Los archivos CSV (Comma Separated Values) son archivos de texto plano que almacenan datos en forma de tabla. Cada fila representa un registro y cada columna representa un campo, y los valores están separados por comas. 

Aqui le dejo un ejemplo de un [archivo csv](https://github.com/alexjszamora78/Gravitad/blob/main/resources/datos.csv) que recoge los datos del tráfico de internet

## Ejecución

```python
from Gravitad import ArimaTP

file_csv = ""
name_columna = ""
ArimaTP.run(file_csv,name_columna)
```

* Recuerda sustituir **file_csv** por el nombre de tu archivo csv y **name_table** por el nombre de la columna que contiene los valores de interés


![tabla](https://github.com/alexjszamora78/Gravitad/blob/main/resources/01.png)



En mi caso mi archivo csv se llama [datos.csv](https://github.com/alexjszamora78/Gravitad/blob/main/resources/datos.csv) y mi columna de valores se llama **TrafficCount** por lo que mi código quedaría estructurado así:


```python
from Gravitad import ArimaTP

file_csv = "datos.csv"
name_columna = "TrafficCount"
ArimaTP.run(file_csv,name_columna)
```


## Output

En la salida se obtendrán las fotos de los gráficos de predicciones


![Output](https://github.com/alexjszamora78/Gravitad/blob/main/resources/output1.png)



![Output](https://github.com/alexjszamora78/Gravitad/blob/main/resources/output21.png)



![Output](https://github.com/alexjszamora78/Gravitad/blob/main/resources/output3.png)


## Parámetros adicionales

* **Puedes modificar la cantidad de predicciones que se realizan pasando como argumento:** num_predictions

* **Por defecto se establece en 60**


```python
from Gravitad import ArimaTP

file_csv = "datos.csv"
name_columna = "TrafficCount"
#Establece la cantidad de predicciones a 15
ArimaTP.run(file_csv,name_columna,num_predictions=15)
```


## ¿ Cuándo usar ArimaTP como solución para proyectos ?

**Se usaría para proyectos que requieran:**

1. Predecir el precio de las acciones de una empresa.

2. Predecir el rendimiento de un fondo mutuo.

3. Estimar la volatilidad de un activo financiero.

4. Predecir la tasa de interés de los bonos.

5. Pronosticar el índice del mercado de valores (por ejemplo, S&P 500, Dow Jones).

6. Analizar el riesgo de crédito de una empresa.


7. Pronosticar la rentabilidad de una inversión.

8. Modelar las tasas de cambio de divisas.

9. Predecir el rendimiento de una cartera de inversión.

10. Analizar los patrones de gasto de los consumidores.

11. Pronosticar el valor de una propiedad inmobiliaria.

12. Estimar el riesgo de fraude financiero.

13. Identificar tendencias de inversión.

14. Predecir las ganancias de una empresa.

15. Modelar el comportamiento del mercado de valores.


16. Pronosticar la demanda de un producto.

17. Predecir las ventas de un artículo en particular.

18. Estimar los niveles de inventario.

19. Optimizar las estrategias de marketing.

20. Ajustar el precio de los productos.

21. Modelar el comportamiento de compra de los clientes.

22. Predecir el volumen de ventas.

23.  Pronosticar la tasa de conversión de ventas.

24. Identificar patrones de compra estacionales.

25. Optimizar los procesos de logística.

26. Predecir la demanda de servicios.

27.  Analizar las tendencias de consumo.

28.  Pronosticar la tasa de crecimiento del mercado.

29.  Estimar la cuota de mercado.

30.  Optimizar la gestión de la cadena de suministro.

31. Predecir el número de casos de una enfermedad.

32. Monitorizar la propagación de una epidemia.

33.  Pronosticar la demanda de atención médica.

34.  Analizar las tendencias de mortalidad.

35.  Predecir la duración de una hospitalización.

36.  Estimar el riesgo de infección.

37.  Monitorizar los resultados de un tratamiento médico.

38.  Pronosticar la necesidad de recursos médicos.

39.  Predecir la tasa de mortalidad infantil.

40.  Analizar los patrones de uso de medicamentos.

41. Pronosticar los niveles de contaminación del aire.

42. Predecir el impacto del cambio climático.

43.  Modelar las tendencias de la temperatura.

44.  Predecir la cantidad de lluvia.

45.  Analizar el nivel del mar.

46.  Pronosticar la frecuencia de incendios forestales.

47.  Evaluar el impacto de la deforestación.

48.  Modelar el crecimiento de las poblaciones de animales.

49.  Predecir la disponibilidad de recursos hídricos.

50.  Analizar la calidad del agua.

51. Pronosticar la demanda de transporte público.

52. Predecir los niveles de tráfico en las carreteras.

53.  Optimizar las rutas de transporte.

54.  Planificar la construcción de nuevas infraestructuras.

55.  Gestionar los tiempos de espera en los aeropuertos.

56.  Analizar los patrones de movilidad.

57.  Predecir los accidentes de tráfico.

58.  Optimizar la gestión del flujo de tráfico.

59.  Pronosticar la demanda de transporte de mercancías.

60.  Evaluar la eficiencia de los sistemas de transporte.

61. Predecir la demanda de energía eléctrica.

62. Pronosticar los precios de la energía.

63.  Optimizar la producción de energía.

64.  Gestionar las reservas de energía.

65.  Analizar el consumo energético.

66.  Modelar la producción de energía renovable.

67.  Pronosticar el impacto de los cambios climáticos en la producción de 
energía.

68.  Evaluar el rendimiento de las plantas de energía.

69.  Optimizar la distribución de la energía.

70.  Analizar el impacto económico de las fluctuaciones de los precios de la energía.

71. Predecir la rotación de personal.

72. Pronosticar la demanda de trabajadores cualificados.

73.  Analizar la satisfacción de los empleados.

74.  Evaluar la eficacia de los programas de formación.

75.  Predecir las necesidades de reclutamiento.

76.  Optimizar la gestión del talento.

77.  Analizar las tendencias del mercado laboral.

78.  Pronosticar el impacto de la automatización en el mercado laboral.

79.  Evaluar la eficiencia de los procesos de selección de personal.

80.  Modelar la gestión del rendimiento de los empleados.

81. Pronosticar el número de turistas.

82.  Predecir la demanda de alojamiento.

83.  Analizar las tendencias de viaje.

84.  Optimizar las estrategias de marketing turístico.

85.  Gestionar los recursos turísticos.

86.  Evaluar el impacto económico del turismo.

87.  Predecir el impacto de eventos en la demanda turística.

88.  Analizar las preferencias de los turistas.

89.  Modelar el impacto del clima en la demanda turística.

90.  Optimizar la gestión de destinos turísticos.

91. Predecir la tasa de crecimiento de la población.

92. Pronosticar las ventas de libros.

93.  Analizar las tendencias de las redes sociales.

94.  Predecir el impacto de la publicidad en las ventas.

95.  Modelar el comportamiento de los usuarios en Internet.

96.  Analizar las tendencias de la tecnología.

97.  Pronosticar el impacto de la innovación en la economía.

98.  Evaluar el riesgo de desastres naturales.

99.  Predecir la demanda de servicios financieros.

100.  Analizar el impacto de la política económica en el crecimiento económico.


## Información para Desarrolladores (DEV)

* [Aquí pueden ver el código fuente con que fue creado la librería ArimaTP](https://github.com/alexjszamora78/Gravitad/blob/main/resources/ArimaTP/main.py)

* [Aquí pueden ver el código fuente con que fue creado la librería TitanTorch](https://github.com/alexjszamora78/Gravitad/blob/main/resources/TitanTorch/main.py)