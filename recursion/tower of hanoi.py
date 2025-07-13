def tower(n, source, helper, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        tower(n - 1, source, target, helper)
        print(f"Move disk {n} from {source} to {target}")
        tower(n - 1, helper, source, target)

res = tower(3, 'A', 'B', 'C')
print(res)  # This will print None, which is fine because the function only prints steps
