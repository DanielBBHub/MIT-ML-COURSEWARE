# Problem Set 5 — Neural Nets y Boosting

## Objetivo del lab

Este problem set se centra en dos grandes ideas de aprendizaje automático:

- **redes neuronales**
- **boosting**

La meta es entender cómo un modelo puede aprender a partir de datos, ajustar sus parámetros y combinar múltiples clasificadores para mejorar el rendimiento final.

---

## 1. Redes neuronales: idea básica

Una neurona artificial recibe entradas, las multiplica por pesos y decide si se activa o no.

### Esquema básico

1. entra un input $X_n$,
2. se multiplica por un peso $W_n$,
3. se suman todas las contribuciones,
4. si el resultado supera un umbral $T$, la neurona se activa.

### Conceptos clave

- **pesos sinápticos**
- **umbral**
- **comportamiento binario**
- **influencia acumulativa**

La salida de una red depende de la entrada, los pesos y los umbrales:

$\vec{Z} = f(\vec{X}, \vec{W}, \vec{T})$

---

## 2. Función de precisión y ajuste de pesos

Para entrenar una red, necesitamos comparar la salida obtenida con la salida deseada.

Una forma de medirlo es con una función de desempeño del tipo:

$P = -\|\vec{D} - \vec{Z}\|^2$

donde:

- $\vec{D}$ es el resultado deseado,
- $\vec{Z}$ es el resultado obtenido.

### Idea central

Si la red se equivoca, hay que ajustar los pesos y/o umbrales para mejorar la salida.

### Ascenso de gradiente

El ajuste puede hacerse usando derivadas parciales, moviendo los pesos en la dirección que mejora la función de precisión.

---

## 3. De función discreta a función continua

Para poder entrenar una red con gradiente, conviene usar una función continua.

Por eso se sustituye el escalón por una función suave, normalmente una **sigmoide**:


$T = \frac{1}{1 + e^{-\alpha}}$


### Interpretación

- valores grandes de $\large \alpha$ $\large \rightarrow$ salida cercana a 1
- valores muy pequeños $\large \rightarrow$ salida cercana a 0

Esto permite que el entrenamiento sea diferenciable.

---

## 4. Redes neuronales simples

En una red simple, el proceso consiste en:

- propagar la información hacia delante,
- calcular la salida,
- comparar con la salida esperada,
- y ajustar los pesos.

### Qué conviene entender

- cómo se propaga la activación,
- cómo se calcula el error,
- cómo influyen los pesos en la salida,
- y cómo se actualizan esos pesos.

---

## 5. Escalado de redes

Si duplicamos una red o la hacemos más grande, no necesariamente el coste crece de forma explosiva.

Muchas veces se pueden reutilizar cálculos entre capas o nodos, aunque la red total tenga más conexiones.

### Idea importante

El coste computacional depende sobre todo de:

- la profundidad de la red,
- y el número de conexiones posibles.

---

## 6. Redes neuronales profundas

Las **deep nets** procesan la información por etapas.

### Flujo típico en visión por computador

1. **Convolución**
2. **Pooling**
3. **Predicción**

#### Convolución
Se aplica un kernel o ventana sobre la imagen para extraer patrones locales.

#### Pooling
Se reduce la información conservando valores representativos, como máximos o mínimos.

#### Predicción
La representación reducida se introduce en una red que devuelve una clase o una probabilidad de clase.

---

## 7. Capas intermedias y autocoding

Una capa intermedia estrecha puede aprender una representación comprimida de la entrada.

Si la red intenta reconstruir la entrada a partir de esa representación reducida, está aprendiendo una **generalización útil**.

### Idea clave

Menos neuronas no significa peor rendimiento automáticamente:  
a veces significa que la red está capturando la estructura relevante del problema.

---

## 8. Capas de salida y Softmax

La salida de una red suele interpretarse como probabilidades por clase.

Cada neurona de salida representa una clase posible, y sus valores se normalizan para obtener una distribución probabilística.

Eso se conoce como **Softmax**.

### Idea central

La red no solo decide una clase, sino que asigna una probabilidad relativa a cada una.

---

## 9. Dropout

**Dropout** consiste en desactivar aleatoriamente algunas neuronas durante el entrenamiento.

### Para qué sirve

- reduce el sobreajuste,
- evita que la red dependa demasiado de neuronas concretas,
- mejora la robustez del modelo.

---

## 10. Robustez frente a perturbaciones

Las redes neuronales pueden ser sorprendentes: a veces pequeños cambios en la entrada alteran la clasificación, y otras veces deformaciones fuertes siguen manteniendo la clase correcta.

### Interpretación

La red aprende patrones suficientemente locales como para reconocer clases incluso cuando la imagen no es perfecta.

Esto muestra que la red no siempre entiende como un humano, sino que aprovecha regularidades estadísticas del dato.

---

## 11. Boosting: combinar clasificadores débiles

El **boosting** busca construir un clasificador fuerte combinando varios clasificadores débiles.

### Idea general

Si cada clasificador comete errores distintos, la combinación puede mejorar mucho el resultado final.


$H(x)=\operatorname{sign}(h_1(x)+h_2(x)+h_3(x))$

---

## 12. Stumps y error ponderado

Un **decision stump** es una prueba simple, no un árbol completo.

### Error simple

Si todas las muestras pesan igual, el error es la suma de las clasificaciones incorrectas.

### Error ponderado

Si algunas muestras pesan más que otras, entonces esas muestras influyen más en el error total.

Esto permite dar más importancia a los ejemplos difíciles.

---

## 13. Algoritmo iterativo de boosting

El algoritmo de boosting funciona de forma secuencial:

1. inicializa los pesos de las muestras,
2. elige el clasificador que minimiza el error ponderado,
3. calcula su peso en la combinación final,
4. actualiza los pesos de las muestras,
5. repite.

### Qué ocurre al actualizar pesos

- las muestras bien clasificadas pierden peso relativo,
- las mal clasificadas ganan importancia,
- y el siguiente clasificador se enfoca en corregir los fallos anteriores.

---

## 14. Relación entre redes neuronales y boosting

Aunque son métodos distintos, ambos buscan mejorar el rendimiento a partir de muchos componentes más simples:

- en redes neuronales, muchas neuronas colaboran para formar una representación útil,
- en boosting, muchos clasificadores débiles se combinan para formar un clasificador fuerte.

---

## 15. Qué conviene dominar para este lab

Para resolver bien este problem set debes entender:

- el modelo básico de una neurona artificial,
- cómo se ajustan los pesos mediante gradiente,
- por qué se usa una sigmoide,
- cómo funcionan convolución, pooling y softmax,
- qué hace dropout,
- y cómo boosting combina clasificadores débiles.

---

## 16. Resumen corto

Este lab reúne dos enfoques de aprendizaje:

- **Redes neuronales**: aprender ajustando pesos y capas
- **Boosting**: aprender combinando clasificadores débiles de forma secuencial

La idea común es construir modelos más potentes a partir de componentes simples.