def calc_fibo(fiboclass):
    fiboclass.n_current = fiboclass.calc_fibo_recursive(fib1.n_max)


class fibonacci_number:
    def __init__(self, nmax):
        self.n_current = 1
        self.n_max = nmax
        if self.n_max <= 1:
            self.n_current = 0

    def __repr__(self):
        return f'fibonacci number of {self.n_max}: {self.n_current}'

    def calc_fibo_recursive(self, n):
        if n > 1:
            return self.calc_fibo_recursive(n-1) \
                + self.calc_fibo_recursive(n-2)
        return n


fib1 = fibonacci_number(5)
calc_fibo(fib1)
