from sys import stdin

def check(n):
    if n < 2 : 
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    s = set()
    ls = list()
    pref = [0]
    for i in range(int(next(it))):
        x = int(next(it)) 
        if not x in s:
            s.add(x)
            ls.append(x)
            pref.append(pref[-1] + x)
    ok = False
    for i, x in enumerate(pref):
        if check(x) and check(pref[-1] - x):
            print(i - 1)
            ok = True
            break
    if not ok : 
        print("NOT FOUND")

if __name__ == "__main__":
    main()