def count_floating_parts(puzzle):
    height = len(puzzle)
    width = len(puzzle[0])

    count = 0

    for i in range(height):
        for j in range(width):
            if puzzle[i][j] == '0':
                if (i == 0 or puzzle[i - 1][j] == '0') and \
                   (i == height - 1 or puzzle[i + 1][j] == '0') and \
                   (j == 0 or puzzle[i][j - 1] == '0') and \
                   (j == width - 1 or puzzle[i][j + 1] == '0'):
                    count += 1

    return count


# Taking puzzle inputs from the user
width, height = map(int, input().split())
puzzle = []

for _ in range(height):
    row = input()
    puzzle.append(list(row))

floating_parts = count_floating_parts(puzzle)
print(floating_parts)
