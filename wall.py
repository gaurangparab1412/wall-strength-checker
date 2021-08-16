class CheckWallStrength:
    def __init__(self):
        """
        Following is a matrix that defines a wall with bricks where each element is defined as a brick.
        Element with value 1 stands for a non porus brick while 0 stands for a porus brick
        If wanted as discussed on call we can have a class Brick that defines the element of a matrix and a brick can
        have its property as porus or non prous. This is just a simple version of the same.
        """
        self.wall = [
            [1, 1, 1, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 0, 1]
        ]

    def check_water_flow(self, element, x, y):
        if element == 0:
            total_rows_in_wall = len(self.wall) - 1
            if x < total_rows_in_wall:
                # following condition will help check if porus wall exists in next row. If it does not exists we
                # can safely say that the wall is safe.
                if 0 in self.wall[x + 1]:
                    successive_element_1 = self.wall[x + 1][y]
                    # This below condition is just to handle -1 index in case of column 0th element
                    if y - 1 < 0:
                        successive_element_2 = 1
                    else:
                        successive_element_2 = self.wall[x + 1][y - 1]
                    successive_element_3 = self.wall[x + 1][y + 1]
                    if successive_element_1 == 0:
                        intermediary_result = self.check_water_flow(successive_element_1, x+1, y)
                        return intermediary_result
                    if successive_element_2 == 0:
                        intermediary_result = self.check_water_flow(successive_element_2, x+1, y - 1)
                        return intermediary_result
                    if successive_element_3 == 0:
                        intermediary_result = self.check_water_flow(successive_element_3, x + 1, y + 1)
                        return intermediary_result
                    return True
                else:
                    # This will help code to exit in specific condition where next row has no porus brick
                    return "End with True"
            else:
                return False
        return True

    def perform_strength_check(self):
        first_row = self.wall[0]
        # I will first check if there is a porus wall in first row at all.
        # If it is not there, no point in checking further
        if 0 in first_row:
            for i in first_row:
                final_result = self.check_water_flow(i, self.wall.index(first_row), first_row.index(i))
                if final_result is False:
                    return False
                elif final_result == "End with True":
                    return True
                else:
                    continue
        else:
            return True


cw = CheckWallStrength()
# Below code will always run with a time complexity of O(n)
result = cw.perform_strength_check()
if result:
    print("This wall is safe")
else:
    print("This wall is unsafe")
