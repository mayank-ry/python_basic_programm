def recursive_min(L):
    if len(L) == 1:
        return L[0]
    rest_min = recursive_min(L[1:])
    if L[0] < rest_min:
        return L[0]
    else:
        return rest_min