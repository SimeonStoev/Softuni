"""
Bullet and Lock Simulation

This program simulates a scenario where bullets are fired at locks to unlock them.
Each bullet has a size, and each lock has a size. A bullet unlocks a lock if its size is greater than or equal to the lock's size.
The gun has a barrel capacity, requiring reloading when empty.
The goal is to unlock all locks using the bullets, calculating earnings based on bullets used and intelligence value.
"""

from collections import deque


def simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence):
    """
    Simulates the bullet and lock scenario.

    Args:
        bullet_price (int): Cost per bullet.
        gun_barrel (int): Capacity of the gun barrel.
        bullets (list): List of bullet sizes.
        locks (deque): Deque of lock sizes.
        value_of_intelligence (int): Value earned if all locks are unlocked.

    Returns:
        list: List of output strings from the simulation.
    """
    bullets_in_barrel = gun_barrel
    bullets_used = 0
    output = []

    while len(bullets) > 0 and len(locks) > 0:
        bullet = bullets.pop()
        bullets_in_barrel -= 1
        bullets_used += 1
        lock = locks[0]

        if lock >= bullet:
            locks.popleft()
            output.append("Bang!")
        else:
            output.append("Ping!")

        if bullets_in_barrel == 0 and len(bullets) > 0:
            output.append("Reloading!")
            bullets_in_barrel = gun_barrel

    if len(locks) == 0:
        bullets_left = len(bullets)
        money_earned = value_of_intelligence - (bullets_used * bullet_price)
        output.append(f"{bullets_left} bullets left. Earned ${money_earned}")
    else:
        locks_left = len(locks)
        output.append(f"Couldn't get through. Locks left: {locks_left}")

    return output


# Read input values
bullet_price = int(input())
gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value_of_intelligence = int(input())

# Run simulation and print output
results = simulate_bullet_lock(bullet_price, gun_barrel, bullets, locks, value_of_intelligence)
for result in results:
    print(result)
