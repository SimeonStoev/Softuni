def fill_the_box(*args):
    args = list(args)
    height = args[0]
    length = args[1]
    width = args[2]
    box_volume = height * length * width
    curr_index = 3

    while args[curr_index] != "Finish" and box_volume > 0:
        if int(args[curr_index]) <= box_volume:
            box_volume -= args[curr_index]
        else:
            args[curr_index] -= box_volume
            box_volume = 0
            break

        curr_index += 1

    if box_volume == 0:
        return f"No more free space! You have {sum(args[curr_index:-1])} more cubes."

    return f"There is free space in the box. You could put {box_volume} more cubes."
