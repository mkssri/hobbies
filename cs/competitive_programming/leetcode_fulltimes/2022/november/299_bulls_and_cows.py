class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        bulls, cows = 0, 0

        b = collections.Counter( secret )

        # bulls processing
        for x,y in zip( secret, guess ):

            if x == y:
                bulls += 1
                b[x] -= 1

        # cows processing
        for x,y in zip( secret, guess ):

            if x != y and b[y] > 0:
                cows += 1
                b[y] -= 1

        return '{}A{}B'.format( bulls, cows )