class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]  # entries are '0' or '1'
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for r in range(rows):
            row = matrix[r]
            for c in range(cols):
                heights[c] = heights[c] + 1 if row[c] == '1' else 0

            stack = [-1] 
            for i in range(cols + 1):
                curr = heights[i] if i < cols else 0
                while stack[-1] != -1 and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    area = h * w
                    if area > max_area:
                        max_area = area
                stack.append(i)

        return max_area
