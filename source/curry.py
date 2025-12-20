def curry(func, arity):
    if arity <= 0:
        raise ValueError("Arity must be positive")

    def step(collected_args):
        if len(collected_args) == arity:
            return func(*collected_args)

        def next_func(x):
            return step(collected_args + [x])

        return next_func

    return step([])


def uncurry(curried_func, arity):
    if arity <= 0:
        raise ValueError("Arity must be positive")

    def normal_func(*args):
        if len(args) != arity:
            raise ValueError("Wrong number of arguments")

        f = curried_func
        for x in args:
            f = f(x)
        return f

    return normal_func


if __name__ == "__main__":

    def sum3(x, y, z):
        return x + y + z

    sum3_c = curry(sum3, 3)
    print(sum3_c(1)(2)(3))

    sum3_u = uncurry(sum3_c, 3)
    print(sum3_u(1, 2, 3))
