def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    answer=str(f"({x}+{y})*2={(x+y)*2}")
    return answer
print(main(4,6))