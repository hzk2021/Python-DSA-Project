# Student Name: He Zhenkai
# Admin Number: 204304Z
# Tutorial Group: IT2154 Group 4


def RecursiveCheckSumsExist(seq, z, smallestIndex, largestIndex):
    if smallestIndex >= largestIndex:  # Base case to exit recursion if condition is met
        return print("X = not found\nY = not found\nFALSE "
                     "(since there does not exist two integers X and Y in SEQ,"
                     " where  sum of X and Y = Z)\n")
    else:
        if seq[largestIndex] >= z:  # Check if last element is bigger or equals to z value. If yes, cut it off
            largestIndex -= 1

        if seq[smallestIndex] + seq[largestIndex] == z:  # Returns True if 2 values sums up to z
            return print("X = {}\nY = {}\nTRUE (since {} + {} = {})\n"
                         .format(seq[smallestIndex], seq[largestIndex],seq[smallestIndex], seq[largestIndex], z))
        elif seq[smallestIndex] + seq[largestIndex] > z:  # Recursive case 1. Cut off largest index if sum of smallest & largest is bigger than z
            return RecursiveCheckSumsExist(seq, z, smallestIndex, largestIndex - 1)
        else:  # Recursive case 2. Cut off smallest index if sum of smallest & largest is smaller than z
            return RecursiveCheckSumsExist(seq, z, smallestIndex + 1, largestIndex)


# Test Cases
list_of_numbers = [2, 3, 5, 7, 8, 10, 15, 16, 23, 28]
smallest_index = 0
largest_index = len(list_of_numbers) - 1

z_valueOne = 21
z_valueTwo = 3

RecursiveCheckSumsExist([2, 3, 5, 7, 8, 10, 15, 16, 23, 28], z_valueOne, smallest_index, largest_index)
RecursiveCheckSumsExist([2, 3, 5, 7, 8, 10, 15, 16, 23, 28], z_valueTwo, smallest_index, largest_index)
