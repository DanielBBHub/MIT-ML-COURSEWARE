from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables

from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    # Paso 1: Buscar reglas que puedan probar la hipótesis
    matching_rules = []
    alternatives = []
    for rule in rules:
        # Verificar si la conclusión de la regla coincide con la hipótesis
        bindings = match(rule.consequent()[0], hypothesis)
        if bindings is not None:
            matching_rules.append((rule, bindings))
    # print(f"MATCHING RULES? {not matching_rules}")
    # Paso 2: Si no hay reglas que prueben la hipótesis, es un hecho base
    if not matching_rules:
        # print(f"ALTERNATIVAS: {alternatives}")
        return hypothesis    
    
    
    add_rules = [populate(rule[0].antecedent(), rule[1])  for rule in matching_rules]
    for rule_antecedents in add_rules:
        # print(f"REGLA ANTECEDENTES: {rule_antecedents} DE TIPO: {type(rule_antecedents)}")
        if isinstance(rule_antecedents, str):
            subtree = backchain_to_goal_tree(rules, rule_antecedents)
            alternatives.append(subtree)
        elif len(rule_antecedents) == 1:
            # Solo una condición, hacer backchain directamente
            
            subtree = backchain_to_goal_tree(rules, rule_antecedents[0])
            alternatives.append(subtree)
        else:
            # Múltiples condiciones, crear un nodo AND
            and_branches = []
            for hyp_ex in rule_antecedents:
                subtree = backchain_to_goal_tree(rules, hyp_ex)
                and_branches.append(subtree)
            alternatives.append(AND(and_branches))

            
    
    flattened_alternatives = []
    for alt in alternatives:
        if isinstance(alt, OR):
            # Si la alternativa es un OR, agregar sus elementos directamente
            flattened_alternatives.extend(alt)
        else:
            flattened_alternatives.append(alt)
    return OR([hypothesis] + flattened_alternatives)


# Here's an example of running the backward chainer - uncomment
# it to see it work:
print( backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin'))
