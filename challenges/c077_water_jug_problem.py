def solve_water_jugs(size1, size2, desired_liters):
    return _solve_water_jugs_helper(size1, size2, desired_liters, 0, 0, {})


def _solve_water_jugs_helper(size1, size2, desired_liters, current_jug1, current_jug2, already_tried):
    if is_solved(current_jug1, current_jug2, desired_liters):
        print("Solved Jug 1:", current_jug1, " / 2:", current_jug2)
        return True
    key = (current_jug1, current_jug2)
    if not key in already_tried:
        already_tried[key] = True
        print("Jug 1:", current_jug1, " / 2: ", current_jug2)
        min_2_1 = min(current_jug2, (size1 - current_jug1))
        min_1_2 = min(current_jug1, (size2 - current_jug2))
        result = _solve_water_jugs_helper(size1, size2, desired_liters,
                                          0, current_jug2, already_tried) or \
            _solve_water_jugs_helper(size1, size2, desired_liters,
                                     current_jug1, 0, already_tried) or \
            _solve_water_jugs_helper(size1, size2, desired_liters,
                                     size1, current_jug2, already_tried) or \
            _solve_water_jugs_helper(size1, size2, desired_liters,
                                     current_jug1, size2, already_tried) or \
            _solve_water_jugs_helper(size1, size2, desired_liters,
                                     current_jug1 + min_2_1, current_jug2 - min_2_1, already_tried) or \
            _solve_water_jugs_helper(size1, size2, desired_liters,
                                     current_jug1 - min_1_2, current_jug2 + min_1_2, already_tried)
        already_tried[key] = result
        return result
    return False


def is_solved(current_jug1, current_jug2, desired_liters):
    return (current_jug1 == desired_liters and current_jug2 == 0) or \
           (current_jug2 == desired_liters and current_jug1 == 0)


def main():
    print(solve_water_jugs(4, 3, 2))
    print(solve_water_jugs(4, 4, 2))


if __name__ == "__main__":
    main()
