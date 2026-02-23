def top_student(records):
    max_total = 0
    top_name = ""

    for name in records:
        total = 0
        for marks in records[name]:
            total = total + marks

        if total > max_total:
            max_total = total
            top_name = name

    return top_name