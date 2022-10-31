def main(x1,x2,x3):
    """
    Given three integers, x1, x2, and x3, return the "[x1, x2, x3]" string.
    Args:
        x1: int
        x2: int
        x3: int
    Returns:
        str: return answer.
    """
    l = []
    l.append(x1)
    l.append(x2)
    l.append(x3) 
    return str(l)
print(main(1,2,3))