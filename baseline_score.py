def baseline_score(query, document):
    return len(set(query.terms) & set(document.terms))
