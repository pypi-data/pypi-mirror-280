# Easy TUI

## Descripción

`Easy TUI` es una biblioteca de Python que permite crear interfaces de usuario de texto (TUI) simples y manejables. Utiliza `simple_screen` para manejar la pantalla y proporciona una estructura básica para crear y gestionar controles como botones, entradas y etiquetas.

## Instalación

Puedes instalar la biblioteca utilizando pip:

```bash
pip install easy_tui
```

## Uso

### Inicialización

Primero, importa las bibliotecas necesarias y define algunas variables globales:

```python
import easy_tui as eTUI
from easy_tui import controls
```

### Crear Widgets

Define tus controles utilizando las clases proporcionadas. Por ejemplo, una etiqueta (`Label`), una entrada de texto (`Entry`), y un botón (`KeyButton`):

```python
label = controls.Label(col=10, fila=5, text="Nombre:")
entry = controls.Entry(col=18, fila=5, label="Nombre")
button = controls.KeyButton(col=10, fila=10, key=eTUI.ENTER, label="Enviar", command=mi_funcion)
```

### Configurar el Bucle Principal

Usa la función `loop` para manejar la interacción del usuario y actualizar la pantalla:

```python
eTUI.loop()
```

### Ejemplo Completo

```python
import easy_tui as eTUI
from easy_tui import controls

hello = controls.Label(25, 3, "Hola, mundo")

nombre = controls.Entry(25, 4, "Nombre: ")
apellidos = controls.Entry(25, 5, "Apellidos: ")

def cambiaNombre():
    hello.text = f"Hola, {nombre.value} {apellidos.value}"

def limpiaTodo():
    nombre.value = ""
    apellidos.value = ""
    cambiaNombre()


f1 = controls.KeyButton(0, key=eTUI.F1, label="Reset", command=limpiaTodo)
f2 = controls.KeyButton(16,key=eTUI.F2, command=cambiaNombre, label="Saluda")


eTUI.loop()

```

Nota: Las teclas y controles para modificacion basica de la pantalla se heredan de simple_screen y pueden ser invocados usando eTUI. Así, el locate de simple_screen se transforma en

```
eTUI.locate(columna, fila, texto)
```

y las teclas F de simple_screen, por ejemplo F2 en

```
eTUI.F2
```

los atributos de pantalla, tales como A_INVERSE se usan igual

```
eTUI.A_INVERSE.on()
... (pintar cosas)
eTUI.A_INVERSE.off()

```


## Documentación

### Clases y Métodos Principales

Finalmente el ancho del control no se controla.

#### `Control`

- `__init__(self, col=0, fila=0, ancho=16, alto=1)`: Inicializa el control.
- `draw(self)`: Método abstracto para dibujar el control.

#### `Label(Control)`

- `__init__(self, col=0, fila=0, text="Label")`: Inicializa una etiqueta.
- `draw(self)`: Dibuja la etiqueta en la posición especificada.

#### `Entry(Control, TabulatableMixin)`

- `__init__(self, col=0, fila=0, label="", ancho=16)`: Inicializa una entrada de texto.
- `draw(self)`: Dibuja la entrada de texto.
- `handle_input(self, key)`: Maneja la entrada del usuario.

#### `KeyButton(Control, ButtonMixin)`

- `__init__(self, col=0, fila=LAST_ROW, key=None, command=None, label="")`: Inicializa un botón con una tecla específica.
- `click(self)`: Ejecuta el comando asociado al botón.
- `draw(self)`: Dibuja el botón.


## Licencia

Este proyecto está licenciado bajo la Licencia MIT.

---

Con esta estructura, podrás crear aplicaciones de consola simples y efectivas usando `simple_screen` y `easy_tui`. ¡Disfruta programando!