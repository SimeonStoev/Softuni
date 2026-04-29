"""
This program simulates a factory where robots process products over time.
Robots have individual processing times, and products arrive in a queue.
Time advances second by second, and robots become available after their processing time expires.
Products are assigned to the first available robot; if none are free, the product is re-queued.
"""

from collections import deque


def get_time(p_start_time, p_seconds):
    """
    Adds a given number of seconds to a starting time and returns the new time in HH:MM:SS format.
    Handles wrapping around minutes and hours, and ensures hours cycle within 24.

    Args:
        p_start_time (str): The starting time in "HH:MM:SS" format.
        p_seconds (int): The number of seconds to add to the starting time.

    Returns:
        str: The new time in "HH:MM:SS" format after adding the seconds.
    """
    time_parts = p_start_time.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    p_seconds += int(time_parts[2])

    # Convert excess seconds to minutes
    while p_seconds >= 60:
        p_seconds -= 60
        minutes += 1

    # Convert excess minutes to hours
    while minutes >= 60:
        minutes -= 60
        hours += 1

    # Wrap hours within 24-hour cycle
    hours = hours % 24
    return f"{hours:02d}:{minutes:02d}:{p_seconds:02d}"


# Read input for robots: format "robot_name-processing_time;robot_name-processing_time;..."
robots_input = input().split(";")
robots = {}
start_time = input()  # Starting time in HH:MM:SS format
products = deque()  # Queue to hold products

# Initialize robots dictionary with name, processing time, status, and next free time
for robot in robots_input:
    robot_data = robot.split("-")
    robots[robot_data[0]] = {"proc_time": int(robot_data[1]), "status": "Free", "next_free_time": "0"}

# Read products until "End" command
while True:
    command = input()
    if command == "End":
        break
    products.append(command)

# Main processing loop: while there are products in the queue
while len(products) > 0:
    product = products.popleft()  # Get the next product from the front of the queue
    start_time = get_time(start_time, 1)  # Advance time by 1 second
    is_product_taken = False
    # Check each robot to see if it's free or becomes free at the current time
    for robot_name, robot_data in robots.items():
        if robot_data["next_free_time"] == start_time:
            robot_data["status"] = "Free"  # Mark robot as free if its next free time matches the current time
            robot_data["next_free_time"] = "0"

        if robot_data["status"] == "Free" and not is_product_taken:
            is_product_taken = True
            robot_data["status"] = "Busy"  # Mark robot as busy
            robot_data["next_free_time"] = get_time(start_time,
                                                    robot_data["proc_time"])  # Calculate when it will be free
            print(f"{robot_name} - {product} [{start_time}]")  # Output assignment

    # If no robot was available, put the product back at the end of the queue
    if not is_product_taken:
        products.append(product)
