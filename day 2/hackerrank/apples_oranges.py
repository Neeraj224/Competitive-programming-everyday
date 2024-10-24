class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, s, t, a, b, apples, oranges):
        # pass
        # apples should fall to the right -> so negative ones will never get to sam's place
        # oranges should fall to the left -> so positive ones will never get to sam's place (poor sam, aww)
        
        sams_apples = 0
        sams_oranges = 0
        
        for apple in apples:
            if s <= a + apple <= t:
                sams_apples += 1
        for orange in oranges:
            if s <= b + orange <= t:
                sams_oranges += 1
        
        print(sams_apples)
        print(sams_oranges)

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(7, 11, 5, 15, [-2, 2, 1], [5, -6]))
    print(solver.solver(7, 10, 4, 12, [2, 3, -4], [3, -2, -4]))
    # print(solver.solver())

if __name__ == "__main__":
    main()