from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])

total_delivery = 0

while len(couriers) > 0 and len(packages) > 0:
    package = packages[-1]
    courier = couriers.popleft()

    if courier >= package:
        total_delivery += package
        packages.pop()
        courier -= 2 * package
        if courier > 0:
            couriers.append(courier)
    else:
        total_delivery += courier
        package -= courier
        packages[-1] = package

print(f"Total weight: {total_delivery} kg")
if len(packages) == 0 and len(couriers) == 0:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif len(couriers) == 0 and len(packages) > 0:
    print(
        f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
else:
    print(
        f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")
