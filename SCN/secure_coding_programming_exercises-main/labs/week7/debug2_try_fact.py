def h_fact(n):
    if n <= 1:
        return 0
    else:
        result = h_fact(n - 1)
        a = n - 2 * result
        print(f"For n={n}, a = {n} - 2 * {result} = {a}")
        return a

print(h_fact(8))
