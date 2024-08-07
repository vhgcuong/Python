from math import sqrt


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    d = sum(m for m in range(1, number) if number % m == 0) - number
    return ("deficient", "perfect", "abundant")[(d >= 0) + (d > 0)]


if __name__ == '__main__':
    classify(28)
