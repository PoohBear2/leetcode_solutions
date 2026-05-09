class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        memo = {}
        def solution(remaining_needs):

            if tuple(remaining_needs) in memo:
                return memo[tuple(remaining_needs)]

            best = sum(price[i] * remaining_needs[i] for i in range(len(price)))

            for deal in special:
                works = True
                for i in range(len(price)):
                    if deal[i] > remaining_needs[i]:
                        works = False
                        break
                if works:
                    best = min(
                        best, 
                        deal[-1] + solution([
                            remaining_needs[i] - deal[i] for i in range(len(price))
                            ]
                        )
                    )


            memo[tuple(remaining_needs)] = best
            return memo[tuple(remaining_needs)]

        return solution(needs)
        
