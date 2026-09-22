def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    copy = []
    for m in matrix:
        copy += [m[::-1]]
    return copy

if __name__ == "__main__":
    print(mirror_matrix([[1,2,3],[4,5,6]]))
    print(mirror_matrix([[1,2],[3,4],[5,6]]))
    print(mirror_matrix([[7]]))
    print(mirror_matrix([[1,2,3,4]]))
    print(mirror_matrix([[-1,-2],[-3,-4]]))