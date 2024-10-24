class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, a, b):
        candidates = []
    
        for i in range(1, 101):
            candidates.append(i)
            for k in range(len(a)):
                if i % a[k] != 0:
                    candidates.pop()
                    break
        
        # print(candidates)
        
        for i in range(len(candidates)):
            # print("now testing " + str(candidates[i]))
            for k in range(len(b)):
                # print(str(b[k]) + " and " + str(candidates[i]))
                if b[k] % candidates[i] != 0:
                    # print(str(candidates[i]) + " removed!")
                    candidates[i] = '_'
                    break
        
        good_count = 0
        for sym in candidates:
            if sym != "_":
                good_count += 1
        
        return good_count

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver([2, 6], [24, 36]))
    # print(solver.solver())
    # print(solver.solver())

if __name__ == "__main__":
    main()