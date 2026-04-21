# Problem Set 4 — CSP, k-Nearest Neighbors y Decision Trees

## Objetivo del lab

Este problem set combina dos bloques principales:

- **Constraint Satisfaction Problems (CSP)**
- **aprendizaje supervisado básico**
  - **k-nearest neighbors**
  - **decision trees**

La idea es aprender a resolver problemas usando restricciones y, al mismo tiempo, entender cómo se clasifican ejemplos a partir de datos.

---

## 1. Constraint Satisfaction Problems

Un **CSP** es un problema en el que debemos asignar valores a variables cumpliendo ciertas restricciones.

### Elementos básicos

- **variables**: cosas a las que asignar un valor
- **dominio**: conjunto de valores posibles
- **restricciones**: condiciones que limitan las asignaciones válidas

### Idea general

Resolver un CSP consiste en encontrar una asignación que satisfaga todas las restricciones.

---

## 2. Propagación de restricciones

Cuando asignamos un valor a una variable, podemos reducir las opciones de las variables vecinas.

### Por qué es útil

- evita explorar combinaciones imposibles,
- reduce el espacio de búsqueda,
- y puede detectar conflictos antes de tiempo.

### Reducción de dominio

Si una variable pierde valores posibles, ese cambio puede propagarse a otras variables relacionadas.  
Esto hace que el problema se vaya simplificando progresivamente.

---

## 3. Estrategias de resolución

Al resolver un CSP, importa mucho el orden en que se eligen las variables y se prueban los valores.

### Algunas ideas útiles

- comprobar vecinos antes de asignar,
- propagar restricciones a variables afectadas,
- y mantener consistencia local o global según el método empleado.

La calidad de la estrategia afecta mucho al rendimiento del algoritmo.

---

## 4. k-Nearest Neighbors

El método **k-NN** se usa para clasificar una entrada comparándola con ejemplos conocidos.

### Idea principal

Si una muestra nueva está cerca de otras muestras ya clasificadas, probablemente pertenezca a la misma clase.

### Cómo funciona

1. se representa cada ejemplo como un punto en un espacio de características,
2. se calcula la distancia a los ejemplos conocidos,
3. se eligen los $\large k$ vecinos más cercanos,
4. se asigna la clase más frecuente o más cercana entre ellos.

---

## 5. Características del k-NN

### Ventajas

- simple de entender,
- fácil de implementar,
- útil cuando las clases están bien separadas.

### Limitaciones

- depende mucho de la métrica de distancia,
- puede ser costoso si hay muchos ejemplos,
- y no funciona tan bien con datos simbólicos o muy dispersos.

---

## 6. Decision trees

Cuando la información es simbólica o no numérica, los árboles de decisión suelen ser más adecuados que k-NN.

### Idea general

Un árbol de decisión hace preguntas sucesivas para separar los datos.

### Qué busca

Cada prueba debe dividir el conjunto de datos de forma lo más homogénea posible.

---

## 7. Desorden e información

Para elegir la mejor prueba se usa una medida de **desorden**.

### Idea

La mejor prueba es la que deja subconjuntos más puros o más homogéneos.

### Relación con Ockham

Esto encaja con la idea de la navaja de Ockham:

> entre varias explicaciones posibles, suele preferirse la más simple.

---

## 8. Simplificación de reglas

Una vez construido un árbol, algunas pruebas pueden resultar redundantes.

Si una condición no aporta información útil para separar clases, puede eliminarse sin empeorar el resultado.

Esto permite construir árboles más simples y más interpretables.

---

## 9. Qué conviene dominar para este lab

Para resolver bien este problem set debes entender:

- qué es una variable, un dominio y una restricción,
- cómo se propagan las restricciones en un CSP,
- cómo funciona la clasificación por vecinos cercanos,
- cómo se construye un árbol de decisión,
- y cómo se mide la calidad de una partición.

---

## 10. Resumen corto

Este lab combina dos maneras de razonar sobre datos:

- **CSP**: encontrar asignaciones que cumplan restricciones
- **k-NN**: clasificar por cercanía
- **Decision trees**: clasificar con pruebas sucesivas y medir el desorden

Es un puente entre búsqueda, restricciones y aprendizaje supervisado básico.