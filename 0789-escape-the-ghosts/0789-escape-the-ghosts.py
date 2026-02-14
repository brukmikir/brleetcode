class Solution(object):
    def escapeGhosts(self, ghosts, target):

        d=abs(target[0])+abs(target[1])

        for g in ghosts:
            distance= abs(target[0]-g[0]) + abs(target[1] - g[1])

            if distance <= d:
                return False
        return True
                               
        