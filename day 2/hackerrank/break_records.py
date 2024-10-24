class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, scores):
        # pass
        max_changed = 0
        min_changed = 0
        
        current_max = scores[0]
        current_min = scores[0]
        
        if len(scores) == 1:
            return [max_changed, min_changed]
        
        for i in range(len(scores)):
            if scores[i] > current_max:
                current_max = scores[i]
                max_changed += 1
            
            if scores[i] < current_min:
                current_min = scores[i]
                min_changed += 1
        
        return [max_changed, min_changed]

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([12, 24, 10, 24]))
    print(solver.solver([10, 5, 20, 20, 4, 5, 2, 25, 1]))
    # print(solver.solver())

if __name__ == "__main__":
    main()