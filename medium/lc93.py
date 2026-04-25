class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        if len(s) < 4 or len(s) > 12:
            return []

        def backtrack(num_times, start, path):
            
            if num_times == 0:
                if start == len(s):
                    res.append(".".join(path))
                return
    
            cur = ""
            for i in range(start, min(len(s), start + 3)):
                
                cur = s[start: i + 1]
                
                if len(cur) > 1 and cur[0] == "0":
                    continue

                if 0 <= int(cur) <= 255:
                    path.append(cur)
                    backtrack(num_times - 1, i + 1, path)
                    path.pop()
        
        backtrack(4, 0, [])
        return res

