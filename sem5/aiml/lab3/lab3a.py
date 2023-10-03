def dpll_3sat(formula, assignments={}):
    """
    Determine the satisfiability of a 3-CNF formula using the DPLL (Davis-Putnam-Logemann-Loveland) algorithm.
    formula: List of clauses where each clause is a list of literals.
    assignments: Dictionary of current variable assignments.
    return: (True, assignments) if satisfiable, (False, {}) otherwise.
    """
    # Check for unsatisfiable clauses
    for clause in formula:
        # If all literals in a clause evaluate to False, the clause (and thus the formula) is unsatisfied.
        if all([(lit in assignments and not assignments[lit]) or 
                (lit[0] == '-' and lit[1:] in assignments and assignments[lit[1:]]) for lit in clause]):
            return False, {}
    # Check if the entire formula is satisfied with the current assignments
    if all([any([(lit in assignments and assignments[lit]) or 
                 (lit[0] == '-' and lit[1:] in assignments and not assignments[lit[1:]]) for lit in clause]) for clause in formula]):
        return True, assignments
    # Unit propagation: Identify and assign values to literals that can be determined directly
    for clause in formula:
        # Find literals in the clause that are not yet assigned
        unassigned_lits = [lit for lit in clause if lit not in assignments and ('-' + lit) not in assignments]
        # If there's only one unassigned literal, set its value to satisfy the clause
        if len(unassigned_lits) == 1:
            lit = unassigned_lits[0]
            # Assign the appropriate boolean value based on the literal's sign
            if lit[0] == '-':
                assignments[lit[1:]] = False
            else:
                assignments[lit] = True
            return dpll_3sat(formula, assignments)
    # Splitting: If we can't determine the assignment directly, guess a value for an unassigned variable
    # Get the first unassigned variable
    var = list({lit for clause in formula for lit in clause if lit not in assignments and lit[0] != '-'})[0]
    new_assignments = assignments.copy()
    new_assignments[var] = True
    # Recurse with the new assignment
    sat, result_assignments = dpll_3sat(formula, new_assignments)
    if sat:
        return True, result_assignments
    # If the assignment didn't lead to a solution, try the opposite value
    new_assignments[var] = False
    return dpll_3sat(formula, new_assignments)
# Sample testing
# Define a 3-CNF formula for testing
formula = [["A", "B", "C"], ["-A", "-B", "-C"], ["A", "-B", "C"]]
# Check satisfiability of the formulas
result = dpll_3sat(formula)
print(result)
