# Actividad DUOC UC - Debugging CRUD en Python

## Descripción de la actividad

Este proyecto corresponde a una actividad práctica de programación en Python.

El sistema simula un pequeño CRUD de estudiantes, donde se deberían poder realizar las siguientes acciones:

- Crear estudiante
- Listar estudiantes
- Buscar estudiante
- Actualizar estudiante
- Eliminar estudiante
- Salir del programa

Sin embargo, el código contiene errores intencionales.  
La misión de cada estudiante será corregirlos usando Git y GitHub.

---

## Objetivo de aprendizaje

Al finalizar esta actividad, el estudiante será capaz de:

- Identificar errores de sintaxis en Python.
- Identificar errores lógicos.
- Corregir problemas de parámetros entre funciones.
- Comprender el uso de listas y diccionarios.
- Aplicar estructuras de control `if`, `elif`, `else`.
- Usar ciclos `while` y `for`.
- Practicar flujo de trabajo con Git:
  - clonar repositorio
  - crear rama
  - corregir código
  - hacer commit
  - subir cambios
  - solicitar revisión

---

## Instrucciones para el estudiante

1. Clonar el repositorio entregado por el docente.

```bash
git clone https://github.com/juazocar/fpy1101-009v-desafio-1.git
```

2. Entrar a la carpeta del proyecto.

```bash
cd nombre-del-repositorio
```

3. Crear una nueva rama con tu nombre.

```bash
git checkout -b correccion-nombre-apellido
```

Ejemplo:

```bash
git checkout -b correccion-juan-perez
```

4. Ejecutar el programa.

```bash
python main.py
```

5. Identificar y corregir los errores.

6. Probar que el sistema funcione correctamente.

7. Guardar los cambios.

```bash
git add .
git commit -m "Corrección de errores CRUD estudiantes"
git push origin correccion-nombre-apellido
```

---

## Reglas del sistema esperado

El programa corregido debe permitir:

### 1. Agregar estudiante

Debe solicitar:

- RUT
- Nombre
- Carrera
- Edad

Y guardar los datos dentro de una lista de estudiantes.

---

### 2. Listar estudiantes

Debe mostrar todos los estudiantes registrados.

Si no hay estudiantes, debe mostrar un mensaje indicando que no existen registros.

---

### 3. Buscar estudiante

Debe buscar un estudiante por RUT.

Si lo encuentra, debe mostrar sus datos.

Si no lo encuentra, debe mostrar un mensaje de error.

---

### 4. Actualizar estudiante

Debe buscar un estudiante por RUT y permitir modificar:

- Nombre
- Carrera
- Edad

---

### 5. Eliminar estudiante

Debe buscar un estudiante por RUT y eliminarlo de la lista.

---

### 6. Salir

Debe finalizar correctamente el programa.

---

## Pistas de errores

El proyecto contiene al menos 10 errores intencionales.

Revisa cuidadosamente los siguientes puntos:

1. En `main.py`, revisa la definición de la función que muestra el menú.
2. En `main.py`, revisa el tipo de dato de la variable `opcion`.
3. En `main.py`, revisa si las comparaciones del menú usan texto o número.
4. En `main.py`, revisa si la función `listar_estudiantes` recibe los parámetros correctos.
5. En `main.py`, revisa qué variable se está enviando al buscar un estudiante.
6. En `main.py`, revisa si la función `actualizar_estudiante` recibe todos los datos necesarios.
7. En `main.py`, revisa el orden de los parámetros al eliminar.
8. En `funciones.py`, revisa si al agregar un estudiante se está usando correctamente la lista.
9. En `funciones.py`, revisa cómo se accede al campo `edad`.
10. En `funciones.py`, revisa si la búsqueda se hace por RUT o por nombre.
11. En `funciones.py`, revisa el uso de `=` y `==`.
12. En `funciones.py`, revisa si la edad actualizada realmente se guarda.
13. En `funciones.py`, revisa si hay errores de sintaxis en las condiciones.
14. Revisa que todas las funciones tengan parámetros coherentes entre llamada y definición.

---

## Desafío adicional

Una vez corregido el programa, mejora el sistema agregando:

- Validación para que la edad sea numérica.
- Validación para que el RUT no se repita.
- Opción para confirmar antes de eliminar.
- Menú que no se caiga si el usuario escribe letras.
- Datos precargados para pruebas.

---

## Resultado esperado

Al terminar la actividad, el programa debe ejecutarse sin errores y permitir realizar correctamente todas las operaciones CRUD.

---

## Archivos del proyecto

```text
main.py
funciones.py
README.md
```

---

## Autor

Actividad preparada para práctica de Python inicial en contexto DUOC UC.
