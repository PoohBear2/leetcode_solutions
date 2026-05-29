class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        impossible = set()
        seen = set()
        possible = set()

        for w in word:

            seen.add(w)

            if w.lower() in impossible:
                continue

            if w.islower() and w.upper() in seen:
                impossible.add(w)
                if w.lower() in possible:
                    possible.remove(w.lower())

            if w.isupper() and w.lower() in seen:
                possible.add(w.lower())
        
        return len(possible)

