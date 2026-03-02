
El machine learning es generar modelos en los que, basados en la representación y percepción de un problema, sean capaces de razonar y predecir una solución correcta.

En base a una representación precisa de la problemática que queremos resolver, pueden aparecer retricciones.

Con lo que, en esencia, se definen algoritmos que en base a unas restricciones expuestas por la representación del problema en cuestión, se dedican a pensar, percibir y actuar en bucle.

-- 

Uno de los métodos para resolver ciertos problemas es el concepto de "Generar y comprobar":
- Se genera una posible solución
- Se pone a prueba
	- Si es equivocada, se vuelve a generar una posible solución
	- Si es correcta, se valida

Es importante para este concepto, que el generador de soluciones esté bien acotado, que no sea redundante, que pueda tener reglas para evitar generar soluciones erróneas.


# 2. -Reasoning- Goal Trees and Problem Solving
#### Resolución de Problemas del Modelo

- **Generar tests**
- **Reducción del problema**


##### Árbol de Reducción del Problema

#### Transformaciones y Ejemplo

#### Reflexiones

---

Para abordar problemas complejos, como la siguiente integral:

![[Pasted image 20251029134252.png]]

la estrategia consiste en descomponerlo en problemas más sencillos, un método conocido como **reducción de problemas**.

![[Pasted image 20251029135000.png]]

Para resolver esta integral, se plantean una serie de teoremas que serán útiles tanto para este caso como para otros problemas de mayor complejidad.

Con el fin de verificar el proceso, se podría implementar un algoritmo con los siguientes pasos:
1.  Aplicar los teoremas simples o seguros.
2.  Consultar en la tabla de integrales.
3.  Verificar el resultado (validación).

Dado que el tercer diagrama descompone la integral original en sub-integrales, el **árbol de reducción del problema** se expande. Esto introduce un **nodo "AND"**, el cual requiere que la resolución de todos sus subproblemas sea exitosa para considerar resuelto el problema principal.

![[Pasted image 20251029135548.png]]

Con el "framework" construido hasta ahora (basado en el planteamiento de teoremas), el programa aún no sería capaz de resolver la integral completa. Debido a esta limitación, será necesario incorporar un **algoritmo heurístico**. El objetivo es transformar, **buscando equivalencias** para reducir/simplificar la resolución del problema.

Con la resolución completa puede darse el caso de que existan **varias posibles soluciones a nuestro problema**, lo que nos llevaría a la adición de un **nodo "OR"** (una bifurcación adicional)

![[Pasted image 20251029152910.png]]
**(Para diferenciar entre nodos "AND" y "OR" se utiliza el cuarto de luna, formando una figura parecida a la A)**

En este caso, para decidir entre los nodos derivados del OR, se evalua la profundidad de la expresión matemática. En esencia se ha hecho una **evaluación heurística** de los nodos resultantes para discernir que camino seguir para la resolución final.

![[Pasted image 20251029154407.png]]
En definitiva, el programa aplica transformaciones cono conocidas (teoremas) y comprueba en la tabla. Si este problema esta resuelto, se valida. En caso de que no lo esté, se evalúan los nodos con el objetivo de encontrar un siguiente problema derivado del original (ya sean AND u OR) se comprueba si es posible aplicar una transformada heurística y se cierra el bucle.

Con este procedimiento se logra resolver un problema complejo, reduciendo en apartados los diferentes pasos de la resolución y decidiendo que caminos se escogerán para realizar la resolución mas rápida

El enfoque que se debe tomar para empezar a desarrollar un programa de este estilo se resuelve con el siguiente catecismo:
- **Que tipo** de conocimientos se necesitan
- **Como se ha de representar** este conocimiento
- **Como se ha de usar** el conocimiento
- **Cuanto** conocimiento
- **Que exactamente**

# 3. Reasoning: Goal Trees and Rule-Based Expert Systems

En un ejemplo sencillo en el que un programa debe seguir un comando el cual ordena poner una caja encima de otra, se vuelve a generar un árbol de decisión/objetivo.

![[Pasted image 20251030160632.png]]

Este árbol contiene información que conforma una traza, información sobre el planteamiento y raciocinio de la solución.

Se pueden responder preguntas de **"¿Porqué haces X?"** mirando hacia arriba en la traza, dándole sentido a las acciones dependiendo de los objetivos. A su vez, se pueden responder preguntas de **"¿Como haces X?"** bajando hacia abajo en la traza, dando respuesta a las acciones que hace por conseguir cierto objetivo.

![[Pasted image 20251031081914.png]]

La figura de arriba representa el camino de una hormiga en una playa (Linea blanca -> camino, figuras verdes -> obstaculos), descrito en la **metáfora de la hormiga de Simon**. Esta metáfora quiere representar que la complejidad del comportamiento de un programa viene dado por el máximo de la complejidad del programa y la complejidad del problema a resolver **{max(Ccomportamiento) = max(Cprograma, Cproblema)}**. 


Los **sistemas basados en reglas** utilizan conocimiento encapsulado en simples reglas con las que hacen asociaciones para llegar a conclusiones
![[Pasted image 20251031082939.png]]

En este caso, un s**istema basado en reglas** utiliza los hechos presentados para enlazarlos de forma progresiva con el objetivo de llegar a la conclusión de que animal se esta hablando. Este sistema se considera **"Forward-Chaining"**.

También se puede revertir el proceso y trabajar a partir de una hipótesis (que sea un guepardo), para encontrar las evidencias de que lo es. 

Al conjunto de estas modalidades podríamos considerarlo un sistema de deducción, con modo **"hacia delante/detrás"** 

# 4. Search: Depth-First, Hill Climbing, Beam


Otro concepto importante es el uso de **"La lista de la cola"**, es decir, los nodos que **vas a visitar/ has visitado**. Esto nos ayuda a definir las ordenes a ejecutar y llevar la cuenta de los nodos que ya hemos visitado.

Esto último es importante para mejorar el rendimiento del algoritmo, por que al saber que ya hemos visitado un nodo en concreto y que hemos extendido el camino a partir de él, podemos evitar volver a evaluarlo, ya que no contiene la resolución al problema (Esto es aplicable a "Depth first" y a "Breadth first").

Existe otro método de búsqueda llamado "Hill climbing" el cual ignora el orden léxico de los nodos y los ordena por su cercanía a la meta.

![[Pasted image 20251104185222.png]]

En este caso, la unión entre los nodos tenía asignada un valor arbitrario, el cual se ha utilizado para elegir el camino más corto, siendo este el resultado. Esto sería otro ejemplo mas de una evaluación heurística para agilizar el proceso de resolución del problema. (next(node) = min(length(NODEn)))

Por último, existe la búsqueda **"BEAM"**, la cual es una variante de **"Breadth first"** con un número constante de niveles despues de los cuales parar, para aplicar una evaluación heurística.
![[Pasted image 20251104185929.png]]

En este ejemplo se aplica una profundidad máxima de 2 nodos, tras los cuales se aplicará la misma evaluación heurística de antes, comprobar cual de los dos nodos está mas cerca del objetivo

El algoritmo para implementar estas búsquedas quedaría de la siguiente manera:
![[Pasted image 20251104190258.png]]

El concepto es crear una cola y extender sobre los nodos elegidos, dependiendo del tipo de búsqueda que se realice tendrán las siguientes propiedades:
- Depth first: se encolará al principio del a cola
- Breadth first: se encolará al final de la cola
- Hill climbing: se encolará al principio de la cola de manera ordenada en base a una evaluación heurística
- Beam: se encolará al principio de la cola en base a la mejor W



# 6. Minimax, Alpha-Beta
	Cuando se genera un arbol de decisión en el que intervienen dos actores, cada nivel de los nodos representa la acción de uno de ellos. El nodo inicial representa el estado del primero de los actores, así como los nodos impares, mientras que el segundo nodo, así como los nodos pares, representan los estados del segundo de los actores.

	A este actor principal se le llama Max, mientras que al actor secundario se le denomina min. Esto es la base del algoritmo Minimax.

	Con estas denominaciones se pretende que el actor Max elija los nodos con mayor valor (asignados mediante evaluaciones heurísticas), mientras que para el actor Min lo contrario.

![[Pasted image 20251214095818.png]]

	En este ejemplo, el jugador Min escogería, lógicamente, el nodo con valor 2; el nodo con mayor valor dentro de sus opciones, dejando al jugador Max con las opciones 2 y 7, de las cuales elegiria el 7.

	El número de posibles nodos finales es igual a el ancho de los nodos (b) elevado a la profundidad de búsqueda (d), es decir b^d

	Desarrollando el algorítmo de Minimax, aparece el Alpha-Beta para remediar la necesidad de potencia de procesado que requiere. El principal problema del algoritmo Minimax es que el objetivo óptimo de este algoritmo es llegar lo mas lejos posible, para tomar la mejor decisión posible, lo cual presenta un gran número de posibilidades. 

	El algorítmo Alpha-Beta intenta solucionar este problema eliminando ramas enteras basandose en sus valores estáticos. Se evaluan el valor de los nodos finales y se les adjudica valores a los nodos previos. El resultado de esta búsqueda de una solución no es ni el mayor ni el menor número, si no el mayor número dentro de un camino en el que se han hecho compromisos para maximizar los valores del actor Max mientras que se minimizaban los valores para el actor Min

![[Pasted image 20251214102821.png]]


# 7. Restricciones: Interpretar dibujos lineales

Con el objetivo de poder reconocer objetos en imágenes y partiendo de la representación de cubos de jugetes, se representan con líneas los objetos apilados.

Para esta tarea se desarrolla la teoria del doble enlace, en la cual se define como parte de un objeto aquellos vertices de tres caras; los vertices que están conectados por 2 enlaces varias veces

![[Pasted image 20260205175330.png]]

Es interesante ver la representación como grafo de los diferentes vértices y sus relaciones, las cuales nos revelan las diferentes caras de los objetos.

Guzman afirmaba que generalmente, los vertices de tres caras proyectan vertices con forma de flecha o "tenedor", con lo que abducimos que si el vertice tiene tres caras, es que este viene del mundo real

Por otra parte, Huffman partia de las siguientes asunciones:
- que los objetos se representaban en posición general (como una vista isometrica que te deje ver las tres dimensiones del objeto)
- que el mundo era triédrico + tres caras
- existen varios tipos de líneas: concavas, convexas y bordes

Esta concepción del mundo no contemplaba rajas o sombras en las representaciones.

Por último, Waltz queria expandir en esta idea para poder abarcar rajas, sombras, vertices triedricos y luz en las diferentes representaciones

Con esto en mente amplió las etiquetas para las lineas de 4->50, aumentando exponencialmente las posibles combinaciones. 

Con la combinación del algoritmo de Huffman y Waltz se genera un DFS con backtracking que es capaz de etiquetar lineas y, en base a unas restricciones, eliminar posibilidades de etiquetas para vertices anteriores y posteriores.

# 8. Restricciones: Búsquedas y reducción de dominio

Con problemas como el de colorear todas las comunidades autonomas sin que ninguna adyadente tenga el mismo color, podemos incurrir en el caso de que eligas tres colores diferentes para tres CA y una que toque estas tres no sea compatible. Esto arrastraría el bloqueo hasta el momento de decidir el color para esta cuarta CA.

Podemos tener en consideración las restricciones que nos plantean los diferentes vecinos para plantear las diferentes posibilidades que tenemos para tomar una decisión.

 ![[Pasted image 20260226162942.png]]
	 
Como podemos ver en el ejemplo de la figura, en una primera evaluación se ha elegido el color amarillo, que acababa la rotación RGBY y no rompía la regla, pero al llegar al estado de Texas se ha visto imposible colorear con ningún de estos colores, con lo que se ha vuelto a LA, se ha reevaluado pintándolo de rojo y de esta manera se ha quedado el amarillo libre para poder cumplir con la restricción.

A este fenómeno se le identifica como "Restricciones locales no descubiertas", los cuales provocan bloqueos a lo largo de la resolución.


#### Vocabulario
	1. Variable v: algo a lo que asignar
	2. Valor x: algo que asignar
	3. Dominio d: conjunto de valores
	4. Restricción c: límite entre variables-valores

En el ejemplo anterior, los estados serían las variables, los colores son valores y el dominio es el conjunto de posibles colores por usar, así como la restricción es que los estados adyacentes no pueden compartir colores.

A esta manera de proceder se le denomina "Reducción de dominio"

![[Pasted image 20260226164621.png]]

Hay que apuntar que el segundo punto de iteración "Por cada variable Vi considerada" queda abierta a interpretación, ya que podríamos considerar diferente número de estados dependiendo de unos u otros criterios. Es importante definir "como consideramos" las variables por que impactaran grandemente en la ejecución de la resolución.

Las posibles consideraciones para la resolución del ejemplo anterior pueden ser las siguientes:
![[Pasted image 20260226165632.png]]
Las opciones 3,4 y 5 son especialmente interesantes debido a que si resuelven el problema:
3. Comprueba los vecinos antes de asignar un valor: Tiene el problema de encontrarse con muchos puntos muertos debido al poco alcance de consideración que tiene
4. Propagar la comprobación a otras variables con el dominio reducido a 1 valor: resuelve el problema con dificultad reducida al no tener que comprobar restricciones para un dominio grande, sin puntos muertos 
5. Propagar la comprobación a otras variables con el dominio reducido: resuelve el problema pero debido al gran alcance de consideración que tiene debe comprobar muchas restricciones, pero sin puntos muertos

# 9. Restricciones: Reconocimiento visual de objetos

Una de las estrategias del reconocimiento visual de objetos es encontrar puntos reconocibles en la forma del objeto a detectar (pj: vertices) y mediante una base de conocimiento previa, que depende de la cantidad de variables de movimiento pueda tener el objeto, podemos calcular una correlación entre las posciones [x,y] de los puntos que queremos detectar en la figura.

![[Pasted image 20260302201054.png]]

En la figura anterior podemos ver como se correlacionan los puntos en las muestras A,B y C y, gracias a esa relación entre coordenadas, se podrá adivinar en la figura input, permitiendonos detectar el objeto en cuestión.

Esta detección se puede hacer en el caso idilico de tener una vista ortografica de la figura (en la cual no aplique la profundidad de campo). Además, cuantos mas grados de libertad haya en las posibles entradas, mas variables habrá que calcular en la correlación de los puntos a detectar.

![[Pasted image 20260302201358.png]]

En el caso de tener rotación únicamente en el eje Z, podemos utilizar las proyecciones para calcular el ángulo de rotación de los puntos, calculando así la relación lineal que siguen los puntos en las diferentes figuras.

El problema de este acercamiento a la solución es la rigidez del marco de trabajo; esta únicamente funciona si tiene puntos reconocibles, una vista ortografica y mantienen el tamaño entre muestras, lo cual hace de este método uno poco aceptable para "el mundo natural" en el que las figuras u objetos que representan las imágenes son irregulares e imperfectas.

