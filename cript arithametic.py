print("CRIPT ARITHEMATIC PROBLEM")
print("KIND + MORE == HONEY")
from re import sub
def solve(q):
    try:
        n = (i for i in q if i.isalpha()).__next__()
    except StopIteration:
        return q if eval(sub(r'(^|[^0-9])0+([1-9]+)', r'\1\2', q)) else False
    else:
        for i in (str(i) for i in range(10) if str(i) not in q):
            r = solve(q.replace(n, str(i)))
            if r:
                return r
        return False

if __name__ == "__main__":
    query = "KIND + MORE == HONEY"
    r = solve(query)
    print(r if r else "No solution found.")
