def fib(N):
    if N == 0 or 1:
        N = 1
    elif N >= 2:
        (N - 1) + (N - 2)
    elif N < 0:
        raise ValueError('numero não pode ser negativo')
    return N

