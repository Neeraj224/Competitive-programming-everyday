class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, keyboards, drives, b):
        # pass
        most_expensive = -1
        
        for i in range(len(keyboards)):
            if keyboards[i] > b:
                continue
            else:
                for j in range(len(drives)):
                    if drives[j] > b:
                        continue
                    else:
                        if keyboards[i] + drives[j] <= b:
                            most_expensive = max(most_expensive, keyboards[i] + drives[j])
        
        return most_expensive
        

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([40, 50, 60], [5, 8, 12], 60))
    print(solver.solver([3, 1], [5, 2, 8], 10))
    # print(solver.solver())

if __name__ == "__main__":
    main()