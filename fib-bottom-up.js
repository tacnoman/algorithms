const fib = (n) => {
    if (n === 1 || n === 2) {
        return 1;
    }

    const fibs = [];
    fibs[1] = 1;
    fibs[2] = 1;

    for (let i = 3; i <= n; i++) {
        fibs[i] = fibs[i - 1] + fibs[i - 2];
    }

    return fibs[n];
}

console.log(fib(5));
