from itertools import product

# Logic functions
def a(R, C): return not R or C        # Raining → Cloudy
def b(E, T): return not E or T        # Exam → TV
def c(M, B): return M or B            # Math ∨ Biology
def d(S):    return not S             # ¬Student
def e(R, S): return R and S           # Rock ∧ Sea

def truth_table(func, variables):
    print(f"\nTruth Table for {func.__name__}:")
    header = " | ".join(variables) + " | Result"
    print(header)
    print("-" * len(header))
    for values in product([True, False], repeat=len(variables)):
        result = func(*values)
        row = " | ".join(str(v) for v in values) + f" | {result}"
        print(row)

truth_table(a, ["Raining", "Cloudy"])
truth_table(b, ["Got_100", "Win_TV"])
truth_table(c, ["Is_Math", "Is_Biology"])
truth_table(d, ["Is_Student"])
truth_table(e, ["Is_Rock", "In_Sea"])

