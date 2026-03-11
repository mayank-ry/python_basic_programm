def common_elements(l1,l2):
    cu = []
    if len(l1)==0 or len(l2)==0:  
        return []
    else:
        for i in l1:
            if i not in cu:
                if i in l2:
                    cu.append(i)  
    return cu

common_elements([1,2,3],[2,3,4])	
common_elements([5,6],[7,8])
common_elements([1,1,2],[1,2,2])
common_elements([], [1,2])