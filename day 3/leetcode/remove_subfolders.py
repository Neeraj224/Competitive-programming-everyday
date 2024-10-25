class Solution:
    def __init__(self) -> None:
        pass
    
    def solver(self, folder):
        # pass
        if not folder:
            return []

        folder.sort()

        res, prev = [folder[0]], folder[0] + '/'

        for f in folder[1:]:
            if not f.startswith(prev):
                res.append(f)
                prev = f + '/'
        
        return res

def main():
    solver = Solution()
    
    #solver.solver()
    print(solver.solver(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]))
    print(solver.solver(folder = ["/a","/a/b/c","/a/b/d"]))
    print(solver.solver(folder = ["/a/b/c","/a/b/ca","/a/b/d"]))

if __name__ == "__main__":
    main()