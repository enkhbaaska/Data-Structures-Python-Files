def print_pegs(pegs):
    print(f"A = {pegs['A']}")
    print(f"B = {pegs['B']}")
    print(f"C = {pegs['C']}")
    print("-" * 25)


def move(pegs, source, target, n):
    disk = pegs[source].pop()
    pegs[target].append(disk)
    print(f"[n={n}] Move disk {disk} from {source} to {target}")
    print_pegs(pegs)


def tower_of_hanoi(n, pegs, source, spare, target):
    print(f"Entering: n={n}, source={source}, spare={spare}, target={target}")
    
    if n == 1:
        move(pegs, source, target, n)
    else:
        tower_of_hanoi(n - 1, pegs, source, target, spare)
        move(pegs, source, target, n)
        tower_of_hanoi(n - 1, pegs, spare, source, target)
    
    print(f"Leaving: n={n}, source={source}, spare={spare}, target={target}")


# Setup
pegs = {
    'A': [6,5,4,3, 2, 1],
    'B': [],
    'C': []
}

print("Start:")
print_pegs(pegs)

tower_of_hanoi(6, pegs, 'A', 'B', 'C')