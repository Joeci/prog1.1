def primteszt(n) -> str:

    db =0

    for d in range(2, n):
        if n % d == 0:
            db = db + 1
    if db >= 2:
        return "NEM"
    return "IGEN"

def main():
    n = int(input())
    print(primteszt(n))

if __name__ == "__main__":
    main()
