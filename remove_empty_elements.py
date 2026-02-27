def remove_empty(given):
    return [item for item in given if item]


# Example
given = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), ""]
print(remove_empty(given))