class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, steps, path):
        # pass
        num_valleys = 0
        sea_level = 0
        
        i = 0
        while i <= len(path) - 1:
            if path[i] == 'U':
                sea_level += 1
                
                if sea_level == 0:
                    num_valleys += 1
            elif path[i] == 'D':
                sea_level -= 1
            
            i += 1
        
        # print("current sea level: " + str(sea_level))
        # print("down steps: " + str(down_steps))
        
        # # if down_steps and sea_level != 0:
        # #     if sea_level == 0 and down_steps > 0:
        # #         num_valleys += 1
        
        return num_valleys
    
def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(6, "DDDUUU"))
    print(solver.solver(12, "DDUUDDUDUUUD"))
    print(solver.solver(8, "DDUUUUDD"))
    print(solver.solver(8, "UDDDUDUU"))

if __name__ == "__main__":
    main()