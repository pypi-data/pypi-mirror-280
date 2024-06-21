from itertools import combinations_with_replacement


def list_allowed_terms(all_fields: list, allowed, order=4) -> list:
    """
    Make a list of all combinations of fields, that contain the charges of the field 'allowed'.

    :param all_fields: A list that contains all fields. Fields have to be an object of the
        :py:meth:`~constructterms.field.Field` class.
    :type all_fields: list
    :param allowed: All returned terms have to contain the representations/charges of this field.
        Has to be an object of the 'Field'-class.
    :type allowed: :py:meth:`~constructterms.field.Field`
    :param order: The order up to which terms are considered, i.e. how many fields are multiplied to yield a term.
    :type order: int
    :return: A list, whose elements are the terms whose charges coincide with 'allowed'. Elements are objects of
        :py:meth:`~constructterms.field.Field` class.
    :rtype: list
    """
    # Generate all possible combinations
    combinations = list(combinations_with_replacement(all_fields, order))
    for i in range(1, order):
        combinations = combinations + list(combinations_with_replacement(all_fields, i))
    # Generate all terms. Note that a term is a Field-class object
    all_terms = []
    for combo in combinations:
        term = combo[0]
        for field in combo[1:]:
            term = term.times(field)
        all_terms.append(term)
    # Sort out the not-allowed terms
    allowed_terms = []
    for term in all_terms:
        if term.is_desired(allowed):
            allowed_terms.append(term)
    # return the result
    return allowed_terms


