from functools import cache


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = "".join(sorted(hand))
        INF = 10 ** 10
        @cache
        def reduce(s):
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j-i >=3:
                    s = s[:i] + s[j:]
                    i = 0
                else:
                    i = j
            return s
        @cache
        def fn(board, hand):
            if not board: return 0
            if not hand: return INF 
            ans = INF 
            for i in range(len(hand)): 
                if i == 0 or hand[i-1] != hand[i]:
                    newHand = hand[:i] + hand[i+1:]
                    for j in range(len(board)): 
                        if hand[i] == board[j] or (j != 0 and board[j-1] == board[j]): 
                            
                            newBoard = reduce(board[:j] + hand[i] + board[j:])
                           
                            ans = min(ans, 1 + fn(newBoard, newHand))
            return ans 
        
        res = fn(board, hand)
        return res if res != INF else -1