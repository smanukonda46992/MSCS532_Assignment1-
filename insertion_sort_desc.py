def sort_descending(numbers):
    """
    Sorts the given list in monotonically decreasing order
    using a modified insertion sort approach.
    """

    # Start from the second element since the first element
    # by itself is already considered sorted
    for current_index in range(1, len(numbers)):
        current_value = numbers[current_index]
        position = current_index - 1

        # Shift elements that are smaller than the current value
        # one position to the right
        while position >= 0 and numbers[position] < current_value:
            numbers[position + 1] = numbers[position]
            position -= 1

        # Insert the current value at the correct position
        numbers[position + 1] = current_value

    return numbers


# Driver code to verify functionality
if __name__ == "__main__":
    sample_data = [96, 106, 56, 305, 26 ]
    print("Before sorting:", sample_data)

    sort_descending(sample_data)

    print("After sorting (descending):", sample_data)
