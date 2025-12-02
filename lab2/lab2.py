# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.
""" Graph() -> Node([]),Edge([]),Dict({Heuristic}), Dict({Edges}) 
                Node(str)
                Edge(str(name), str(node1),str(node2),int(length))"""

def bfs(graph, start, goal):
    """  breadth-first search extiende todos los nodos creando primero
         los niveles horizontales, es decir, busca todos los nodos conectados
         al nodo evaluado"""
    # Comprobacion picara por si entrase un nodo inicial == nodo final
    if start == goal:
        return [start]
    
    agenda = []
    visited = set()
    pathDict = {}
    pathXT = []
    eval_node = ""
    # Inicializamos la cola calculando los nodos conectados y encolandolos
    nodos_conectados = graph.get_connected_nodes(start)
    agenda = sorted(nodos_conectados)
    # Inicializamos el diccionario que guardara los paths por nodo con el string
    # de nodo como llave
    for nodo in agenda:
        pathDict.setdefault(nodo, list(start) + list(nodo))
    # Definimos el nodo de inicio como ya visitado para no dar la vuelta
    visited.add(start)
    while agenda:
        # Empezamos el bucle sacando el primer valor de la lista
        eval_node = agenda.pop(0)

        # Comprobamos que vayamos a evaluar el nodo objetivo
        if eval_node == goal:
            print(pathDict[eval_node])
            return pathDict[eval_node]

        # Si es un nodo ya extendido se continua evaluando los siguientes
        elif eval_node in visited:
            continue
        
        else:
            # Se calculan los nodos conectados al nodo a evaluar
            eval_conected = graph.get_connected_nodes(eval_node)
            # Se recorren los nodos adjuntos al nodo evaluado
            for nodo in eval_conected:
                # Se ignoran los nodos ya visitados
                if nodo not in visited:
                    # Si el nodo adjunto no esta visitado se agrega a la cola/agenda de nodos a visitar
                    agenda.append( nodo)
                    # Se recoge el path que hemos extendido con el nodo a evaluar 
                    pathXT = pathDict[eval_node]
                    # Se asocia al nodo conectado una lista con el path del nodo evaluado + el nuevo nodo evaluado
                    pathDict.setdefault(nodo, pathXT + list(nodo))
            # Se agrega el nodo evaluado a la lista de nodos visitados
            visited.add(eval_node)
            

    return pathDict[goal]
    # raise NotImplementedError

## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    """  depth-first search extiende todos los nodos de un camino en orden alfabetico
         hasta alcanzar la maxima verticalidad. Es decir, dado un arbol que empiece en
         el nodo S y acabe en el nodo G: 
         vecinosNodo(start) = ["A", "B"] -> 
         vecinosNodo("A") = ["C", "D"] -> 
         vecinosNodo("C") = ["F", "G"]
         
    """
    # Comprobacion picara por si entrase un nodo inicial == nodo final
    if start == goal:
        return [start]
    
    agenda = []
    visited = set()
    pathDict = {}
    pathXT = []
    eval_node = ""
    # Inicializamos la cola calculando los nodos conectados y encolandolos
    nodos_conectados = graph.get_connected_nodes(start)
    agenda = sorted(nodos_conectados)
    # Inicializamos el diccionario que guardara los paths por nodo con el string
    # de nodo como llave
    for nodo in agenda:
        pathDict.setdefault(nodo, list(start) + list(nodo))
    visited.add(start)

    while agenda:
        eval_node = agenda.pop(0)

        # Comprobamos que vayamos a evaluar el nodo objetivo
        if eval_node == goal:
            print(pathDict[eval_node])
            return pathDict[eval_node]

        # Si es un nodo ya extendido se continua evaluando los siguientes
        elif eval_node in visited:
            continue

        else: 
            eval_connected = graph.get_connected_nodes(eval_node)
            for nodo in sorted(eval_connected):
                if nodo not in visited:
                    # Se recoge el path que hemos extendido con el nodo a evaluar 
                    pathXT = pathDict[eval_node]
                    # Se asocia al nodo conectado una lista con el path del nodo evaluado + el nuevo nodo evaluado
                    pathDict.setdefault(nodo, pathXT + list(nodo))
            # Se agrega el nodo evaluado a la lista de nodos visitados
            agenda = eval_connected + agenda
            visited.add(eval_node)

    # raise NotImplementedError


## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    """ 
    Hill climbing con backtracking: intenta el vecino con mejor heurística,
    pero si llega a un callejón sin salida, retrocede e intenta otras opciones.
    """
    # Evaluamos si el nodo inicial es el objetivo
    if start == goal:
        return start
    
    # Evaluamos si el ultimo nodo del path es el objetivo
    if start[-1] == goal:
        return list(start)
    
    eval_node = start[-1]
    eval_connected = graph.get_connected_nodes(eval_node)
    heuristic_nodes = []
    for node in eval_connected:
        heuristic_nodes.append((node, graph.get_heuristic(node, goal)))

    heuristic_nodes.sort(key=lambda x: x[1])
    result = ""
    for node in heuristic_nodes:
        if node[0] not in start:
            new_path = start + node[0]
            result = hill_climbing(graph, new_path, goal)
            if result is not None:
                return result

    # raise NotImplementedError

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):

    if start == goal:
        return start
    
    eval_node = start[-1]
    eval_connected = []
    eval_connected = graph.get_connected_nodes(eval_node)
    visited = set ()
    visited.add(start)
    heuristics_connected = []
    pathDict = {}
    for connected in eval_connected:
        if connected not in start:
            heuristics_connected.append((connected, graph.get_heuristic(connected, goal)))
            pathDict.setdefault(connected, eval_node + connected)
    heuristics_connected.sort(key=lambda x: x[1])

    while heuristics_connected:
    
        filtered_connected = []
        for i, connected in enumerate(heuristics_connected, 1):
            if i <= beam_width:
                filtered_connected.append(connected)
            else:
                pathDict.pop(connected[0])
          
        heuristics_connected = filtered_connected
        for eval_node in heuristics_connected:
            eval_connected = graph.get_connected_nodes(eval_node[0])
            for connected in eval_connected:
                if connected not in visited:
                    heuristics_connected.append((connected, graph.get_heuristic(connected, goal)))
                    pathDict.setdefault(connected, eval_node + connected)
                    visited.add(connected)
            heuristics_connected.pop(eval_node)
        heuristics_connected.sort(key=lambda x: x[1])

    
    
    return 
    # raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    raise NotImplementedError


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''
