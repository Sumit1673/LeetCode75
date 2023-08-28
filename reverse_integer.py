def reverse_integer(num : int) -> int :
    """ Reverses an integer

    Args:
        num (int): number to reverse

    Returns:
        int: reversed number
    """
    try:
        return int(str(num)[::-1]) if num > 0 else int(str(num)[0] + str(num)[:0:-1])
    except:
        print("Check your input")

if __name__ == '__main__':
    print(reverse_integer(-345.0))
    