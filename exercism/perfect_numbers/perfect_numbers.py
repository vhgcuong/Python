from math import sqrt


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"

    factors = {1}
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)

    factor_sum = sum(factors)

    match (factor_sum == number, factor_sum < number):
        case (True, False):
            return "perfect"
        case (False, True):
            return "deficient"
        case (_, _):
            return "abundant"


if __name__ == '__main__':
    classify(28)
