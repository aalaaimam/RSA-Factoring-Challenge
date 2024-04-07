import sys

def factors(filename):
    with open(filename, "r") as file:
        for line in file:
            n = int(line.strip())
            if n <= 1:
                continue

            # Try dividing by 2, 3, 4, 5,...
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    p = i
                    q = n // i
                    print(f"{n}={p}*{q}")
                    break

if __name__ == "__main__":
    if len(sys.argv)!= 2:
        print("Usage: factors <file>")
        sys.exit(1)

    factors(sys.argv[1])
