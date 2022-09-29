class fibonacci_number:
    def __init__(self, nmax):
        self.n_ant = 0
        self.n_current = 1
        self.n_max = nmax
        self.n = 2
        if self.n_max <= 1:
            self.n_current = 0

    def __repr__(self):
        return f'fibonacci number of {self.n_max}: {self.n_current}'

    def calc_fibo(self):
        while self.n < self.n_max:
            aux1 = self.n_current
            self.n_current += self.n_ant
            self.n_ant = aux1
            self.n += 1


fib1 = fibonacci_number(1)
fib1.calc_fibo()
