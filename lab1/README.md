# Problem Set 1 — Forward Chaining, Backward Chaining y Goal Trees

## Objetivo del lab

Este problem set se centra en el **razonamiento simbólico**: cómo un programa puede llegar a conclusiones a partir de hechos, reglas y objetivos.

Los conceptos más importantes son:

- **goal trees**
- **forward chaining**
- **backward chaining**
- **rule-based expert systems**
- **trazas de razonamiento**

---

## 1. Representación del conocimiento

En IA, resolver un problema empieza por **representar bien el conocimiento**.

Un sistema puede trabajar con:

- **hechos**: información conocida
- **reglas**: relaciones del tipo “si ocurre esto, entonces concluye aquello”
- **objetivos**: metas que queremos demostrar o alcanzar

La idea es que el programa no solo almacene información, sino que también pueda **usar esa información para razonar**.

---

## 2. Método de generar y comprobar

Una forma básica de resolver problemas es:

1. generar una posible solución,
2. comprobar si funciona,
3. si no funciona, probar otra.

En este lab, esa idea aparece de forma más estructurada: el sistema no genera soluciones al azar, sino que usa **reglas** para construir razonamientos válidos.

---

## 3. Reducción del problema

Muchos problemas pueden resolverse descomponiéndolos en otros más pequeños.

En vez de intentar resolver el objetivo final directamente, el sistema:

- identifica subobjetivos,
- resuelve cada parte,
- y combina los resultados.

Esto se llama **reducción del problema** y es la base de los **goal trees**.

---

## 4. Goal trees

Un **goal tree** es un árbol que organiza un objetivo en subobjetivos.

### Tipos de nodos

- **AND**: todos los subobjetivos deben resolverse.
- **OR**: basta con resolver una de las opciones.

Esta estructura permite modelar problemas de razonamiento donde hay varias rutas posibles o varias condiciones simultáneas.

### Para qué sirve

- para descomponer objetivos complejos,
- para organizar el proceso de razonamiento,
- y para registrar cómo se llegó a una conclusión.

---

## 5. Forward chaining

El **forward chaining** parte de los hechos conocidos y aplica reglas para derivar nuevos hechos.

### Flujo general

1. se parte de hechos iniciales,
2. se buscan reglas aplicables,
3. se obtienen conclusiones nuevas,
4. se repite el proceso.

### Cuándo conviene

Es útil cuando queremos saber **qué se puede deducir** a partir de una base de conocimiento dada.

---

## 6. Backward chaining

El **backward chaining** parte de una hipótesis o meta y trata de demostrarla.

### Flujo general

1. se formula una conclusión deseada,
2. se buscan reglas que la justifiquen,
3. se convierten sus premisas en subobjetivos,
4. se repite hasta llegar a hechos conocidos.

### Cuándo conviene

Es útil cuando queremos comprobar si una afirmación es cierta y tenemos una meta concreta en mente.

---

## 7. Sistemas basados en reglas

Los **rule-based expert systems** usan conocimiento encapsulado en reglas simples para tomar decisiones.

Un sistema de este tipo puede:

- encadenar reglas,
- justificar conclusiones,
- y reconstruir el proceso de inferencia.

Esto es lo que hace posible el razonamiento explicable.

---

## 8. Trazas de razonamiento

El árbol o la cadena de inferencia constituyen una **traza**.

Gracias a esa traza, el sistema puede responder:

- **¿Por qué haces X?**  
  Mirando hacia arriba en el árbol.

- **¿Cómo haces X?**  
  Mirando hacia abajo en el árbol.

Esto es importante porque una buena IA no solo debe acertar, sino también poder explicar su razonamiento.

---

## 9. Qué conviene dominar para este lab

Para este problem set debes entender bien:

- cómo representar hechos y reglas,
- cómo funciona la deducción hacia delante,
- cómo funciona la deducción hacia atrás,
- cómo construir un goal tree,
- y cómo interpretar una traza de razonamiento.

---

## 10. Resumen corto

La idea central del lab 1 es que un sistema puede razonar simbólicamente si organiza el conocimiento en reglas y objetivos.

- **Forward chaining**: partir de hechos y derivar conclusiones
- **Backward chaining**: partir de una meta y buscar sus justificaciones
- **Goal trees**: descomponer objetivos en subobjetivos
- **Rule-based systems**: aplicar reglas para inferir conocimiento

Este es el fundamento del razonamiento simbólico que se usará después en otros temas del curso.