def md_nre_single_sample(y, y_hat, n, p):
    result = (y**(1/n)-y_hat**(1/n))**p
    return print(result)


def divide(a, b):
    return a/b


md_nre_single_sample(1, 0.5, 2, 1)
