'''
Here I will be ereplacing -> for implication with > and |- with = sp
P -> Q |- F will be written as P > Q = F
and not is ~
Or is V
and is ^

 this program will encapsulate all the funcitonality in a single fucntion
'''

import random
import string
import numpy as np


# expr = input("Input the theorem to be checked for proof : ")

# print("The expression entered is {}".format(expr))

def remove_spaces_from_expr(expr):
    '''
    This function will remove any uneeded space form expression
    '''
    return "".join(expr.split())
    

# print("The expression entered is {}".format(remove_spaces_from_expr(expr)))


# simplify
def simplify_expression(expr):
    '''
    When the equation will be entered it will alredy be stripped of its outer brackets
    '''
    expr = remove_spaces_from_expr(expr)
    if expr[0] == '(':
        # remove the brackets
        expr = expr[1:]
        expr = expr[:-1]
    # print(expr)
    no_brackets = 0
    for it, i in enumerate(expr):
        # print(i, no_brackets)
        if i == '(':
            no_brackets += 1
        elif i == ')':
            no_brackets -= 1
        elif i == '>':
            if no_brackets == 0:
                # zero brackets encountered till no
                return "(" + simplify_expression(expr[0:it]) + ">" +  simplify_expression(expr[it+1:])+")"
    # at this point we have got the single expression
    # 
    if len(expr) == 1:
        return expr
    # now compund statemtn
    if expr[0] == '~':
        newexp = simplify_expression(expr[1:])   
        return "(" + newexp + ">" + "F"   + ")"
    
    # now check for 'or' , 'and'
    no_brackets = 0
    for it,i in enumerate(expr):
        if i == '(':
            no_brackets += 1
        elif i == ')':
            no_brackets -= 1
        elif i == '^' or i == 'V' :
            if no_brackets == 0:
                exp1 = simplify_expression(expr[0:it])
                exp2 = simplify_expression(expr[it+1:])
                if i == 'V' : # it is the OR value
                    return "((" + exp1 + ">" + "F)>" + exp2 + ")"
                else:
                    return "((" + exp1 + ">(" + exp2 + ">F))>F)" 

    # print("Single Expression  : {}".format(expr))
    return  "(" + expr + ")"


expr1 = '((P>Q)>((~Q>P)>Q))'
expr2 = '(P>(PVQ))'
expr3 = '((P^Q)>(PVP))'
expr4 = '((PVQ)>(PVP))' # according to me this should fail


# print("Expression : {}\nSimplified : {}".format(expr1, simplify_expression(expr1)))
# print("Expression : {}\nSimplified : {}".format(expr2, simplify_expression(expr2)))
# print("Expression : {}\nSimplified : {}".format(expr3, simplify_expression(expr3)))

# print(simplify_expression(expr2))
# print(simplify_expression(expr3))

left_hand_expressions = [] # the left hand expressions while getting a F on the rights
# we will input sets of values with left hand and right hand.

def separate_expression(expr):
    if expr[0] == '(':
        expr = expr[1:]
        expr = expr[:-1]
    no_brackets = 0
    for it, i in enumerate(expr):
        # print(i, no_brackets)
        if i == '(':
            no_brackets += 1
        elif i == ')':
            no_brackets -= 1
        elif i == '>':
            if no_brackets == 0:
                # zero brackets encountered till no
               return (expr[0:it], expr[it+1:])
    return (None, expr)
    # at this point we have got the single expression

    # find the >

# change the expression value over here for 
def generate_left_hand_expression(expr):
    '''
    THis function will generate a list containing the componenets in the left hand side of the deductino theorem to 
    have a 'F' on the right side
    expr : This is the expression and need not be simplied
    return  : list
    '''
    left_hand_expressions = []
    expression = simplify_expression(expr)
    while expression != 'F':
    # if the right side is not F, separate the left and right side
        (lhs, rhs) = separate_expression(expression)
        if lhs == None:
            # i.e. we have reached to a single term and 
            if rhs != 'F':
                # if the right hand side is not F, meaning we have to do negation
                # we need to generate a negation for the term
                # left hand expression
                lhe = "(" + rhs + ">" + "F)"
                left_hand_expressions.append(lhe)
                rhs = "F"
        else:
            left_hand_expressions.append(lhs)

        expression = rhs
    return left_hand_expressions

def axiom1(A,B):
    '''
    A→(B→A)
    '''
    axm1 =  "(" + str(A) + ">" +"("  + str(B) + ">" + str(A) + "))" 
    return simplify_expression(axm1)

    

def axiom2(A,B,C):
    '''
    (A→(B→C))→((A→B)→(A→C))
    '''
    axm2 = "(({}>({}>{}))>(({}>{})>({}>{})))".format(A,B,C,A,B,A,C)
    return simplify_expression(axm2)

def axiom3(A,B):
    '''
    (¬A→¬B)→(B→A)
    '''
    axm3 = "((({}>F)>({}>F))>({}>{}))".format(A,B,B,A)
    return simplify_expression(axm3)


def axiom3_2(A):
    '''
    ((A→F)→F)→A)
    '''

def apply_modes_ponens(left_hand_expr , times = 1, parents = None):
    '''
    Apply modes Ponens on all posssible combinations with 'times'
    number of times
    return : The list of modified left_hand_expr
    '''
    if parents == None:
        parents = dict()
    all_expr = set()
    for t in range(times):
        for expr1 in left_hand_expr:
            for expr2 in left_hand_expr:
                if expr1 == expr2 :
                    # ignore this version
                    continue 
                else:
                    all_expr.add(expr1)
                    all_expr.add(expr2)
                    (le, re) = separate_expression(expr2)
                    if le == expr1 :
                        all_expr.add(re)
                        if re not in parents:
                            parents[re] = []
                        parents[re].append((expr1, expr2))
        left_hand_expr = all_expr.copy()
                
    return (left_hand_expr, parents)

                # apply modes ponenes among these two
def modes_ponenes(left_eq, right_eq):
    '''
    not implementing at the moment 
    '''
    pass


def get_all_possible_expression(expressions):
    '''

    '''
    pass
    
def get_all_possible_atom_expression(expressions):
    set_all_atom_expression = set()
    lse = set()
    rse = set()
    atomic_literals = set()
    for expr in expressions:
        if len(expr) == 1:
            
            lse.add(expr)
            atomic_literals.add(expr)
        else:
            (l,r) = separate_expression(expr)
            lse.add(l)
            rse.add(r)
            atomic_literals.add(l)
            atomic_literals.add(r)
    for ep in expressions:
        # set_all_expression.add(ep)
        set_all_atom_expression.add(ep)
    for ep in rse:
        set_all_atom_expression.add(ep)
    for ep in lse:
        set_all_atom_expression.add(ep)
    return set_all_atom_expression



def create_all_possible_axioms(set_all_expression , axiom, num_elements):
    """
    Give the function pointer for the axiom and the number of elements the axiom takes as input 
    """
    all_expression_from_axioms = set()
    if num_elements == 2 :
        for ep1 in set_all_expression:
            for ep2 in set_all_expression:
                all_expression_from_axioms.add(axiom(ep1,ep2))
    elif num_elements == 3:
        for ep1 in set_all_expression:
            for ep2 in set_all_expression:
                for ep3 in set_all_expression:
                    all_expression_from_axioms.add(axiom(ep1,ep2,ep3))

    return all_expression_from_axioms




    
def Solvable_Expression(expres = expr3, set_all_expression = None):
    left_hand_expressions = []
    Expr = expres
    # print("Expression : {}\nSimplified : {}".format(Expr, simplify_expression(Expr)))

    expression = simplify_expression(Expr)
    
    while expression != 'F':
        # if the right side is not F, separate the left and right side

        (lhs, rhs) = separate_expression(expression)
        # print(" {}   :   {}".format(lhs, rhs))
        if lhs == None:
            # i.e. we have reached to a single term and 
            if rhs != 'F':
                # if the right hand side is not F, meaning we have to do negation
                # we need to generate a negation for the term
                # left hand expression
                lhe = "(" + rhs + ">" + "F)"
                left_hand_expressions.append(lhe)
                rhs = "F"
        else:
            left_hand_expressions.append(lhs)

        expression = rhs

    # capture the individual elements of the right hand side
    left_elements = dict()
    le = []
    lse = set()
    righ_elements = dict()
    re = []
    rse = set()
    atomic_literals = set()
    for expr in left_hand_expressions:
        # print(expr)
        if len(expr) == 1:
            le.append(expr)
            lse.add(expr)
            atomic_literals.add(expr)
        else:
            (l,r) = separate_expression(expr)
            le.append(l)
            lse.add(l)
            re.append(r)
            rse.add(r)
            atomic_literals.add(l)
            atomic_literals.add(r)


    # apply Modes Ponenes on each pair and add the results to teh respective set
    # print("All the left hand literals : {}".format(lse))
    # print("All the right hand literals : {}".format(rse))
    # print("All the literals : {}".format(atomic_literals))
    parents = dict() # parents of expressions

    
        
    # print(apply_modes_ponens(left_hand_expressions, len(left_hand_expressions)))
    left_hand_expressions,_ = apply_modes_ponens(left_hand_expressions, len(left_hand_expressions))
    if set_all_expression is None:
        set_all_expression = set()
    set_all_atom_expression = set()
    for ep in left_hand_expressions:
        set_all_expression.add(ep)
        set_all_atom_expression.add(ep)
    for ep in rse:
        set_all_atom_expression.add(ep)
    for ep in lse:
        set_all_atom_expression.add(ep)

    

    # print("All the Liters 2 : {}".format(set_all_atom_expression))
    # print(len(set_all_expression))
    # try:
    #     set_all_expression.remove('F')
    # except:
    #     pass
    # print(set_all_expression)




    # approach 1 : Brute Force
    if 'F' in set_all_atom_expression:
        set_all_atom_expression.remove('F')
    axioms1_set = create_all_possible_axioms(set_all_atom_expression, axiom1, 2)
    axioms2_set = create_all_possible_axioms(set_all_atom_expression, axiom2, 3)
    axioms3_set = create_all_possible_axioms(set_all_atom_expression, axiom3, 2)
    set_all_expression  = set_all_expression.union(axioms1_set)
    set_all_expression  = set_all_expression.union(axioms2_set)
    set_all_expression  = set_all_expression.union(axioms3_set)
    # print(len(set_all_expression))
    # print(set_all_expression)
    parents = dict()
    iter = 0
    
    while 'F' not in set_all_expression:
        # print("Iterations  : {}".format(iter))
        (set_all_expression_new,parents) = apply_modes_ponens(set_all_expression, 1)
        if set_all_expression.issubset(set_all_expression_new) and set_all_expression_new.issubset(set_all_expression):
            # here I have modified the code so that it asks the user for additional theorem

            # fixme : This is the older version
            # additional_predicate = str(input("Not been able to prove at this point, enter an additionla condition, predicate, axiom that you may know to process further (else No): "))
            # if 'no' in additional_predicate.lower():
            #     print("Solution not possible")
            #     break
            #
            # else:
            #     # simplify the expression first
            #     pred = simplify_expression(additional_predicate)
            #     set_all_expression_new.add(pred)
            break
        # print("Not a subset")
        # set_all_atom_expression = get_all_possible_atom_expression(set_all_expression_new)
        # axioms1_set = create_all_possible_axioms(set_all_atom_expression, axiom1, 2)
        # axioms2_set = create_all_possible_axioms(set_all_atom_expression, axiom2, 3)
        # axioms3_set = create_all_possible_axioms(set_all_atom_expression, axiom3, 2)
        # set_all_expression_new  = set_all_expression_new.union(axioms1_set)
        # set_all_expression_new  = set_all_expression_new.union(axioms2_set)
        # set_all_expression_new  = set_all_expression_new.union(axioms3_set)
        set_all_expression  = set_all_expression_new.copy()
        iter += 1
        # print("Moving to next iteration")

    # print(set_all_expression)
    # for a in set_all_expression:
    #     print(a)
    # print("Does the F element exists or not : {}, \n If the above value is True -> that the theorem is valid otherwise the further work has to be done yet :)".format('F' in set_all_expression))
    if 'F' in set_all_expression:
        return True
    else:
        return False