class Solution:
    def __init__(self):
        pass
    
    def solver(self, s: str, t: str):
        # pass
        s_map = {}
        t_map = {}
        
        for c in s:
            if c not in s_map:
                s_map[c] = 1
            else:
                s_map[c] += 1
        
        for c in t:
            if c not in t_map:
                t_map[c] = 1
            else:
                t_map[c] += 1
        
        for tkey, tval in t_map.items():
            if tkey not in s_map:
                return False
            elif s_map[tkey] != t_map[tkey]:
                return False
        
        return True
        

def main():
    solver = Solution()
    
    print(solver.solver(s = "anagram", t = "nagaram"))
    print(solver.solver(s = "rat", t = "car"))
    # print(solver.solver())
    
    # solver.solver()
    # solver.solver()
    # solver.solver()
    
if __name__ == "__main__":
    main()