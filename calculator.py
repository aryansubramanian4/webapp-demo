import math
from typing import Union


def quadratic(a: float, b: float, c: float) -> Union[tuple[float, float], None]:
    """
    Solve a quadratic equation of the form ax^2 + bx + c = 0.

    Parameters:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        tuple[float, float] or None: A tuple of two real roots if they exist, or None if no real roots exist.
    """
    if a == 0:
        raise ValueError(
            "Coefficient 'a' must be nonzero for a valid quadratic equation."
        )

    discriminant = b**2 - 4 * a * c  # calculate the discriminant

    if discriminant >= 0:  # equation has solutions
        x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x_1, x_2
    else:
        return None


def main():
    a = float(input('please enter a number:'))
    b = float(input('please enter a number:'))
    c = float(input('please enter a number:'))
    sol = quadratic(a, b, c)
    if sol is not None:
        sol_1, sol_2 = sol
        print(f'The two roots are: {sol_1}, {sol_2}.')
    else:
        print('No real solutions exist for the given coefficients.')


if __name__ == '__main__':
    main()
