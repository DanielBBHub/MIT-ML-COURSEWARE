# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = '2'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch
def cube(x):
    return x**3
    # raise NotImplementedError

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
    # raise NotImplementedError

def count_pattern(pattern, lst):
    contador = 0

    for i in range(len(lst)):
        if pattern[0] == lst[i]:
            if pattern == lst[i:i+len(pattern)]:
                contador += 1

    return contador
    # raise NotImplementedError

# Problem 2.2: Expression depth
def depth(expr: list) -> int:    # Aquí le indicamos a python q es una función con parámetros y regresa un entero. Es decir, que se recibe algo como [lista], devuelva numeroso (int), o sea número de profundidad en la lista
    if type(expr) is int:    # Aquí estoy mirando si el argumento es una cifra numérica -> no tenemos nada más que hacer con listas, regresará error.
      return  0     # Si es entonces devuelvo profundidad de la lista en ese caso 0 (es decir simplemente estoy retornado). En python estos tipos son "primitivos" y tampoco hay recursividad para ir aumentando una cifra numérica.

    elif type(expr) is list or type(expr) is tuple:   # Aquí se mira si el argumento es un lista (que puede ser de expresiones arithméticas u otras cosas). Si son, entonces hagamos nuestro cálculos recursivamente.
      return max(depth(i) for i in expr ) + 1 # Aquí estoy haciendo un "map" en python y regresando el máximo de todos los elementos (+1 para incluir la lista por sí sola). Este es nuestro cálculo.

    elif type(expr) is str:   # Aquí estoy mirando si el argumento es un número decimal (float)
        level = 0
        for char in expr:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
        return level
    else:
      raise ValueError(f'El tipo {type(expr)} no soportado') # Aquí estoy mirando que hay un error, y lo que hago solo regresará "Value Error" con el mensaje de qué tipo está incorrectamente pasada en la función.


# Problem 2.3: Tree indexing
def tree_ref(tree, index):
    """ 
    Your job is to write a procedure that is analogous to list referencing, but for trees. This "tree_ref"
    procedure will take a tree and an index, and return the part of the tree (a leaf or a subtree) at that index.
    For trees, indices will have to be lists of integers. Consider the tree in Figure 1, represented by this
    Python tuple: (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
    To select the element 9 out of it, we’d normally need to do something like tree[3][1]. Instead, we’d
    prefer to do tree_ref(tree, (3, 1)) (note that we’re using zero-based indexing, as in list-ref,
    and that the indices come in top-down order; so an index of (3, 1) means you should take the fourth
    branch of the main tree, and then the second branch of that subtree). As another example, the element 6
    could be selected by tree_ref(tree, (1, 1, 1)).
    Note that it’s okay for the result to be a subtree, rather than a leaf. So tree_ref(tree, (0,))
    should return ((1, 2), 3).  
    """
    if len(index) == 1:
        return tree[index[0]]
    else:
        return tree_ref(tree[index[0]], index[1:])

    #raise NotImplementedError


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = ""

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = ""

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = ""

# How many hours did this lab take?
HOURS = ""
