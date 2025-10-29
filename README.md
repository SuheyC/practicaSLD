

## 🗂️ Estructura de carpetas

Crea una carpeta llamada:

```
prologSLD/
│
├── sdl_practice.py
├── recetas_completas.json
├── tupla.py
├── tuplasKB.py
└── README.md
```

---

## 📘 Contenido 


# 🔍 Proyecto: Resolución SLD en Python - prologSLD

## 📖 Descripción

Este proyecto implementa una **resolución SLD (Selective Linear Definite-clause resolution)** en Python, aplicada al dominio de recetas de cocina mexicanas.  
Permite consultar una **base de conocimiento** de recetas para determinar si son **vegetarianas** o **completas**, basándose en reglas lógicas y un proceso de unificación.

---

## 🧩 Archivos del proyecto

 Archivo y Descripción 

 `sdl_practice.py`= Script principal que implementa la resolución SLD, la unificación y la consulta interactiva. 
 `recetas_completas.json`= Base de conocimiento (hechos) con recetas, ingredientes y categorías. 
 `tupla.py` = Contiene ejemplos de hechos representados como tuplas para la tarea de las tupls. 
 `tuplasKB.py` = Contiene ejemplos de hechos representados como tuplas para la base de conocimiento de nuestro proyecto final. 
 `README.md` = Documento descriptivo del proyecto, equipo y explicación del modelo lógico. 

---

## ⚙️ Ejecución del programa

1. Clona o descarga este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/prologSLD.git
   cd prologSLD
````

2. Ejecuta el programa en consola:

   ```bash
   python sdl_practice.py
   
````
3. Ingresa el **nombre exacto de la receta** según aparece en el archivo `recetas_completas.json`:

   ```
   === Sistema de consulta de recetas (modo SLD) ===

   Escribe el nombre de la receta IGUAL QUE EN EL JSON (o 'salir' para terminar):
   > enchiladas_vegetarianas
   ```

   Resultado:

   ```
   Resultados para 'enchiladas_vegetarianas':
     - Es vegetariana: Sí
     - Es completa: Sí
   ```

---

---  
## 🧠 Base de Conocimiento
  ```
Ejemplo de hechos (recetas):

```prolog
Receta(chilaquiles_verdes)
Receta(arroz_con_pollo)
Receta(enchiladas_vegetarianas)
```

Ejemplo de cláusulas de Horn utilizadas:

1. **Una receta es vegetariana si tiene proteína vegetal y no tiene proteína animal.**

   ```
   vegetariana(X) :- proteina_vegetal(X), ¬proteina_animal(X).
   ```

2. **Una receta es completa si tiene proteína, carbohidrato y verdura.**

   ```
   completa(X) :- proteina(X), carbohidrato(X), verdura(X).
   ```

---


## 🔬 Funcionamiento lógico

El script realiza los pasos del razonamiento SLD:

1. **Unificación:** compara los hechos y variables mediante el método de sustitución.
2. **Reglas de inferencia (cláusulas de Horn):** determinan propiedades de las recetas.
3. **Resolución SLD:** permite derivar respuestas lógicas a consultas tipo `¿es vegetariana?` o `¿es completa?`.

---
````
## 👩‍💻 Informacion

| Nombre                       | Matrícula | Correo                                                |
| ---------------------------- | --------- | ----------------------------------------------------- |
| Yulianna Suhey Carrera Brito | 22760731  | [al22760731@ite.edu.mx](mailto:al22760731@ite.edu.mx) |

---

## 🏫 Instituto

**Tecnológico Nacional de México – Instituto Tecnológico de Ensenada**
**Carrera:** Ingeniería en Sistemas Computacionales
**Materia:**    Programacion Logica
**Tema:** Resolución SLD (Prolog en Python)

---



## 🧾 Confirmación final

Tu repositorio **prologSLD** contendrá:

✅ `sdl_practice.py` → tu código principal.  
✅ `recetas_completas.json` → tu base de conocimiento.  
✅ `tupla.py` → hechos representados en tuplas.  
✅ `tuplasKB.py` → hechos representados en tuplas. 
✅ `README.md` → documentación con descripción, reglas y equipo.

