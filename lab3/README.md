# Problem Set 3 — Game Search

## Objetivo del lab

Este problem set trata sobre la búsqueda en juegos de dos jugadores, donde cada decisión depende de un adversario que también juega de forma estratégica.

Los conceptos principales son:

- **Minimax**
- **Alpha-Beta pruning**
- árboles de decisión para juegos
- evaluación de posiciones finales

---

## 1. Árbol de juego con dos jugadores

En un juego de dos jugadores, el árbol de decisión alterna entre ambos participantes.

### Roles

- **Max**: intenta maximizar el valor de la posición.
- **Min**: intenta minimizarlo.

Cada nivel del árbol representa el turno de uno de los jugadores.

---

## 2. Minimax

**Minimax** es el algoritmo básico para decidir jugadas en un juego adversarial.

### Idea general

- Max elige la mejor opción para sí mismo.
- Min responde eligiendo la opción que peor deja a Max.
- El valor de los nodos se propaga desde las hojas hasta la raíz.

### Interpretación

El algoritmo asume que ambos jugadores juegan de forma óptima.  
Por eso, cada decisión se toma pensando en la mejor respuesta del oponente.

---

## 3. Complejidad de búsqueda

El número de nodos terminales que puede explorar minimax crece muy rápido.

Se expresa como:


$\large b^d$


donde:

- `b` es el factor de ramificación,
- `d` es la profundidad de búsqueda.

Esto hace que el algoritmo sea costoso cuando el árbol es grande.

---

## 4. Alpha-Beta pruning

**Alpha-Beta pruning** mejora Minimax eliminando ramas que ya no pueden influir en la decisión final.

### Idea clave

Si una rama no puede superar una alternativa ya conocida, no hace falta seguir explorándola.

### Ventaja

- reduce el número de nodos evaluados,
- mantiene el mismo resultado que minimax,
- permite profundizar más con el mismo coste.

### Qué representa

Alpha-Beta no busca el máximo o el mínimo puro de forma aislada.  
Busca el mejor valor dentro de un proceso de optimización en el que se descartan ramas inútiles.

---

## 5. Qué conviene dominar para este lab

Para resolver este problem set debes tener claro:

- cómo se alternan los turnos en un árbol de juego,
- qué hacen Max y Min,
- cómo se calcula una decisión con minimax,
- por qué el coste crece como $b^d$,
- y cómo alpha-beta poda el árbol sin cambiar el resultado.

---

## 6. Resumen corto

Este lab introduce la base de la búsqueda en juegos:

- **Minimax**: modela un juego de dos jugadores con decisiones óptimas
- **Alpha-Beta**: optimiza minimax podando ramas innecesarias

Es la base para entender cómo razonan los algoritmos en situaciones competitivas.