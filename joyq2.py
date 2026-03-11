def course_ends(courses):
    if len(courses)==0:
        print(courses)
        return courses   
    elif len(courses)==1:
        print(tuple(courses+courses))
        return tuple(courses+courses)  
    else:
        last = len(courses)
        print(tuple(courses[0]+courses[last-1]))
        return tuple(courses[0]+courses[last-1])
    
course_ends(('Math','CS','Physics'))
course_ends(('AI',))
course_ends(())
course_ends(('Bio','Chem'))
