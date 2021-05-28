def floodFill(image, sr, sc, newColor):
    color = image[sr][sc]

    if color == newColor:
        return image

    def dfs(image, sr, sc):
        image[sr][sc] = newColor
        lst = [[sr-1, sc], [sr+1, sc], [sr, sc-1], [sr, sc+1]]
        for row, column in lst:
            if row >= 0 and column >= 0 and row < len(image) and column < len(image[0]) and image[row][column] == color:
                dfs(image, row, column)

    dfs(image, sr, sc)

    return image
