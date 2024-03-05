def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    x=abs(a)
    if x%10==0:
        return "two-digit even number"
    if x%10==1:
        return  "two-digit odd number"
    if x%1000==1:
        return "three-digit odd number"
    if x%1000==0:
        return "three-digit even number"
    
print(main(24))