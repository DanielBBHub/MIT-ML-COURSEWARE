from classify import *
import math
from collections import Counter

##
## CSP portion of lab 4.
##
from csp import BinaryConstraint, CSP, CSPState, Variable,\
    basic_constraint_checker, solve_csp_problem

# Implement basic forward checking on the CSPState see csp.py
def forward_checking(state, verbose=False):
    
    # Before running Forward checking we must ensure
    # that constraints are okay for this state.
    basic = basic_constraint_checker(state, verbose)
    if not basic:
        return False

    # Add your forward checking logic here.
    
    # Let X be the variable currently being assigned.
    current_X = state.get_current_variable()
    if current_X == None:
        return True

    # Find all the binary constraints that are associated with X. 
    current_consts = state.get_constraints_by_name(current_X.get_name())

    for const in current_consts:
        # Let Y be the variable connected to X by that binary constraint. 
        # For each variable value y in Y's domain
        current_Y_name = const.get_variable_j_name()
        current_Y = state.get_variable_by_name(current_Y_name)
        current_Y_dom = current_Y.get_domain()
        for val_y in current_Y_dom:
            # If constraint checking fails for X=x and Y=y
                if not const.check(state, current_X.get_assigned_value(), val_y):
                # Remove y from Y's domain
                    current_Y.reduce_domain(val_y)
                # If the domain of Y is reduced down to the empty set, then the entire check fails:
                if len(current_Y.get_domain()) == 0:
                    # return False.
                    return False
            
    return True
    
    # raise NotImplementedError

# Now Implement forward checking + (constraint) propagation through
# singleton domains.
def forward_checking_prop_singleton(state, verbose=False):
    # Run forward checking first.
    fc_checker = forward_checking(state, verbose)
    if not fc_checker:
        return False

    # Add your propagate singleton logic here.
    # Create a queue of singleton variables
    singleton_var = []
    # Create a queue of visited singleton variables
    visited_singleton_var = []

    # Find variables with domains of size 1.
    for var in state.get_all_variables():
        if var.domain_size() == 1:
            singleton_var.append(var)

    singleton_var = sorted(singleton_var, key= lambda  obj: len(state.get_constraints_by_name(obj.get_name())), reverse=True)

    while singleton_var:
        # Pop off the first singleton variable X
        current_var = singleton_var.pop(0)
        current_var_name = current_var.get_name()

        # Add X to list of visited singletons
        visited_singleton_var.append(current_var)
        # Find all the binary constraints that singleton X is associated with
        # For each constraint therein
        var_constraints = state.get_constraints_by_name(current_var_name)
        for const in var_constraints:
         # Let Y be the variable connected to X by that binary constraint      
            var_j = state.get_variable_by_name(const.get_variable_j_name())
            
            # Obtener el valor singleton: puede estar asignado o ser el único valor del dominio
            current_var_value = current_var.get_assigned_value() if current_var.is_assigned() else current_var.get_domain()[0]
            
         # For each value of y in Y's domain
            for val_y in var_j.get_domain():  
                # If constraint check fails for X = (X's singleton value) and Y = y
                if not const.check(state, current_var_value, val_y):
                    # Remove y from Y's domain
                    var_j.reduce_domain(val_y)
                
                # If the domain of Y is reduced down to the empty set, then the entire check fails:
                if var_j.domain_size() == 0:
                    # return False.
                    return False
        
        for var in state.get_all_variables():
            if var.domain_size() == 1 and var not in visited_singleton_var and var not in singleton_var:
                singleton_var.append(var)    


        singleton_var = sorted(singleton_var, key= lambda  obj: len(state.get_constraints_by_name(obj.get_name())), reverse=True)

    return True

## The code here are for the tester
## Do not change.
from moose_csp import moose_csp_problem
from map_coloring_csp import map_coloring_csp_problem

def csp_solver_tree(problem, checker):
    problem_func = globals()[problem]
    checker_func = globals()[checker]
    answer, search_tree = problem_func().solve(checker_func)
    return search_tree.tree_to_string(search_tree)

##
## CODE for the learning portion of lab 4.
##

### Data sets for the lab
## You will be classifying data from these sets.
senate_people = read_congress_data('S110.ord')
senate_votes = read_vote_data('S110desc.csv')

house_people = read_congress_data('H110.ord')
house_votes = read_vote_data('H110desc.csv')

last_senate_people = read_congress_data('S109.ord')
last_senate_votes = read_vote_data('S109desc.csv')


### Part 1: Nearest Neighbors
## An example of evaluating a nearest-neighbors classifier.
senate_group1, senate_group2 = crosscheck_groups(senate_people)
#evaluate(nearest_neighbors(hamming_distance, 1), senate_group1, senate_group2, verbose=1)

## Write the euclidean_distance function.
## This function should take two lists of integers and
## find the Euclidean distance between them.
## See 'hamming_distance()' in classify.py for an example that
## computes Hamming distances.

def euclidean_distance(list1, list2):

    assert isinstance(list1, list)
    assert isinstance(list2, list)
    res = 0
    for x1, x2 in zip(list1, list2):
        res += (x1 - x2) ** 2 
    
    return math.sqrt(res)

#Once you have implemented euclidean_distance, you can check the results:
evaluate(nearest_neighbors(euclidean_distance, 1), senate_group1, senate_group2)

## By changing the parameters you used, you can get a classifier factory that
## deals better with independents. Make a classifier that makes at most 3
## errors on the Senate.

my_classifier = nearest_neighbors(euclidean_distance, 1)
evaluate(my_classifier, senate_group1, senate_group2, verbose=1)

### Part 2: ID Trees
# print (CongressIDTree(senate_people, senate_votes, homogeneous_disorder))

## Now write an information_disorder function to replace homogeneous_disorder,
## which should lead to simpler trees.

def information_disorder(yes, no):
    # return homogeneous_disorder(yes, no)
    count = Counter()
    nb = len(yes) 
    nb2 = len(no)

    for c1 in yes:
        count[c1] +=  1
    
    res1 = 0
    for k in count.keys():
        res1 += - (count[k] / nb) * math.log( (count[k] / nb) ,2)

    count = Counter()
    for c2 in no:
        count[c2] +=  1
    
    res2 = 0
    for k2 in count.keys():
        res2 += - (count[k2] / nb2) * math.log( (count[k2] / nb2) ,2)

    nbt = nb + nb2

    res = res1 * (nb / nbt) + res2 * (nb2 / nbt)
    return res


print (CongressIDTree(senate_people, senate_votes, information_disorder))
#evaluate(idtree_maker(senate_votes, homogeneous_disorder), senate_group1, senate_group2)

## Now try it on the House of Representatives. However, do it over a data set
## that only includes the most recent n votes, to show that it is possible to
## classify politicians without ludicrous amounts of information.

def limited_house_classifier(house_people, house_votes, n, verbose = False):
    house_limited, house_limited_votes = limit_votes(house_people,
    house_votes, n)
    house_limited_group1, house_limited_group2 = crosscheck_groups(house_limited)

    if verbose:
        print( "ID tree for first group:")
        print( CongressIDTree(house_limited_group1, house_limited_votes,
                             information_disorder) )
        print()
        print( "ID tree for second group:" )
        print( CongressIDTree(house_limited_group2, house_limited_votes,
                             information_disorder) )
        print()
        
    return evaluate(idtree_maker(house_limited_votes, information_disorder),
                    house_limited_group1, house_limited_group2)

                                   
## Find a value of n that classifies at least 430 representatives correctly.
## Hint: It's not 10.
N_1 = 45
rep_classified = limited_house_classifier(house_people, house_votes, N_1)

## Find a value of n that classifies at least 90 senators correctly.
N_2 = 67
senator_classified = limited_house_classifier(senate_people, senate_votes, N_2)

## Now, find a value of n that classifies at least 95 of last year's senators correctly.
N_3 = 25
old_senator_classified = limited_house_classifier(last_senate_people, last_senate_votes, N_3)


## The standard survey questions.
HOW_MANY_HOURS_THIS_PSET_TOOK = ""
WHAT_I_FOUND_INTERESTING = ""
WHAT_I_FOUND_BORING = ""


## This function is used by the tester, please don't modify it!
def eval_test(eval_fn, group1, group2, verbose = 0):
    """ Find eval_fn in globals(), then execute evaluate() on it """
    # Only allow known-safe eval_fn's
    if eval_fn in [ 'my_classifier' ]:
        return evaluate(globals()[eval_fn], group1, group2, verbose)
    else:
        raise Exception( "Error: Tester tried to use an invalid evaluation function: '%s'" % eval_fn )

    
