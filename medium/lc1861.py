class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        rows, cols = len(boxGrid), len(boxGrid[0])
        res_arr = [["." for _ in range(rows)] for _ in range(cols)]

        for r in range(rows):
            
            res_arr_bottom_col = rows - 1 - r
            res_arr_bottom_row = cols

            for c in range(cols - 1, -1, -1):

                if boxGrid[r][c] == ".":
                    continue
                
                if boxGrid[r][c] == "*":
                    res_arr_bottom_row = c

                    res_arr[res_arr_bottom_row][res_arr_bottom_col] = "*"
                
                elif boxGrid[r][c] == "#":
                    
                    res_arr[res_arr_bottom_row - 1][res_arr_bottom_col] = "#"

                    res_arr_bottom_row -= 1
        
        return res_arr
                
