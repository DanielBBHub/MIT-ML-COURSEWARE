# Problem Set 2 — Search, Heuristics, Optimal Search y Graph Heuristics

## Objetivo del lab

Este problem set trata sobre **búsqueda en espacios de estados** y sobre cómo usar **heurísticas** para explorar mejor un problema.

Los conceptos más importantes son:

- representación de nodos y fronteras de búsqueda,
- **Depth-First Search**,
- **Breadth-First Search**,
- **Hill Climbing**,
- **Beam Search**,
- y criterios heurísticos para priorizar caminos.

---

## 1. La lista de cola y los nodos visitados

En una búsqueda, es importante llevar control de:

- los nodos que todavía se van a explorar,
- y los nodos que ya se han visitado.

Esta lista de cola permite decidir el orden de expansión y evitar repetir trabajo innecesario.

### Por qué importa

Si sabemos que un nodo ya fue explorado, podemos evitar evaluarlo otra vez.  
Eso mejora el rendimiento del algoritmo y reduce exploraciones redundantes.

Esta idea es fundamental tanto en:

- **Depth-First Search**
- **Breadth-First Search**

---

## 2. Depth-First Search

En **Depth-First Search**, el algoritmo profundiza por una rama antes de explorar otras.

### Características

- explora un camino lo más lejos posible,
- usa poca memoria comparado con BFS,
- puede quedar atrapado en ramas poco útiles si no se controla bien.

### Relación con la cola

Los nodos se insertan al principio de la cola, lo que favorece seguir profundizando por la rama más reciente.

---

## 3. Breadth-First Search

En **Breadth-First Search**, se exploran primero los nodos más cercanos al origen.

### Características

- visita por niveles,
- encuentra soluciones cortas si existen,
- pero puede consumir mucha memoria.

### Relación con la cola

Los nodos se encolan al final de la cola, lo que hace que se exploren por orden de llegada.

---

## 4. Hill Climbing

**Hill Climbing** es una estrategia de búsqueda guiada por una heurística.

En lugar de seguir un orden fijo, el algoritmo elige el nodo que parece **más cercano a la meta**.

### Idea clave

No se expande cualquier nodo, sino el que tenga mejor evaluación local.

### Ventaja

Puede ser muy rápido si la heurística es buena.

### Problema

Puede quedarse atascado en:

- máximos locales,
- puntos muertos,
- o decisiones que parecen buenas pero no llevan a la solución real.

### Interpretación

La elección del siguiente nodo se guía por una medida aproximada de cercanía al objetivo, como en:


$next(node) = min(length(NODE_n))$


---

## 5. Beam Search

**Beam Search** es una variante de búsqueda por niveles, pero limitada por un ancho fijo.

### Cómo funciona

1. se expanden varios nodos del nivel actual,
2. se evalúan heurísticamente,
3. solo se conservan los mejores `W`,
4. se repite el proceso.

### Ventaja

Reduce mucho el espacio de búsqueda frente a una exploración completa.

### Limitación

Si el ancho `W` es demasiado pequeño, pueden perderse soluciones buenas.

---

## 6. Algoritmo general de búsqueda

La idea general es mantener una cola de nodos y decidir cómo insertar los nuevos candidatos.

### Estrategias principales

- **Depth-First**: insertar al principio de la cola.
- **Breadth-First**: insertar al final de la cola.
- **Hill Climbing**: insertar ordenado según heurística.
- **Beam Search**: conservar solo los mejores `W` nodos.

---

## 7. Qué conviene dominar para este lab

Para resolver bien este problem set debes entender:

- cómo se representa una frontera de búsqueda,
- cómo cambian DFS y BFS según el orden de inserción,
- qué papel juega una heurística,
- por qué hill climbing puede atascarse,
- y cómo beam search controla la expansión del árbol.

---

## 8. Resumen corto

Este lab introduce las bases de la búsqueda informada y no informada:

- **DFS**: profundiza primero
- **BFS**: explora por niveles
- **Hill Climbing**: elige el nodo que parece mejor
- **Beam Search**: mantiene solo los mejores candidatos

La idea general es explorar mejor un espacio enorme sin recorrerlo por completo.