"""
Runtime state that must be mutated in place by one bot/*.py module and read by
another. Kept separate to avoid a circular import between apply_form.py (mutates)
and orchestrator.py (reads for the end-of-run summary).
"""

randomly_answered_questions = []


def add_unique(collection: list, item) -> None:
    '''
    Appends `item` to `collection` if not already present, preserving insertion order (unlike a set).
    '''
    if item not in collection:
        collection.append(item)
