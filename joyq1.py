def unique_elements(L):
    result = []
    for element in L:
        if element not in result:
            result.append(element)
    return result
        
