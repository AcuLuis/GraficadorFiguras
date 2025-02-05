# Optimización de Espacios - Graficador de espacios

Este proyecto es una aplicación gráfica desarrollada en Python utilizando la biblioteca `PyQt5`. La aplicación permite a los usuarios crear y manipular figuras geométricas en un área de trabajo, con el objetivo de optimizar el espacio disponible. La aplicación incluye funcionalidades para crear, configurar, guardar y cargar figuras, así como para ajustar sus propiedades como tamaño, color y rotación.

## Características Principales

- **Creación de Figuras**: Permite crear figuras geométricas como rectángulos, cuadrados, círculos, trapecios y triángulos.
- **Configuración de Figuras**: Ajusta el tamaño, color y rotación de las figuras seleccionadas.
- **Guardado y Carga**: Guarda y carga el estado del área de trabajo en formato JSON, permitiendo la persistencia de los datos.
- **Interfaz Gráfica Intuitiva**: La interfaz de usuario es fácil de usar, con menús y paneles de configuración accesibles.
- **Manipulación de Figuras**: Las figuras pueden ser movidas, copiadas, pegadas y eliminadas directamente desde la interfaz gráfica.

## Requisitos

- Python 3.x
- PyQt5

## Instalación

1. Clona este repositorio o descarga el código fuente.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. Instala las dependencias necesarias:

   ```bash
   pip install PyQt5

## Uso
- **Crear una Nueva Figura**:
Selecciona la forma deseada desde el menú "Forma".
Haz clic en el área de trabajo para colocar la figura.

- **Configurar una Figura**:
Selecciona una figura haciendo clic sobre ella.
Utiliza el panel de configuración para ajustar el tamaño, color y rotación de la figura.

- **Guardar y Cargar**:
Guarda el estado actual del área de trabajo seleccionando "Guardar" en el menú "Opciones".
Carga un estado previamente guardado seleccionando "Cargar" en el menú "Opciones".

- **Manipular Figuras**:
Mueve las figuras arrastrándolas con el ratón.
Copia y pega figuras utilizando el menú contextual (clic derecho).
Elimina figuras seleccionándolas y utilizando la opción "Eliminar" en el menú contextual.

## Estructura del Código
- **MainWindow**: Clase principal que maneja la ventana principal de la aplicación y los menús.

- **ConfigPanel**: Clase que gestiona el panel de configuración de las figuras.

- **WorkSpace**: Clase que maneja el área de trabajo y las operaciones sobre las figuras.

- **DialogEscala**: Clase que gestiona el diálogo para establecer la escala del área de trabajo.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme en luisacudev@gmail.com.