class Solution:
    def findWinners(self, matches):
        loss_count = {}
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss_count[loser] = loss_count.get(loser, 0) + 1

        no_loss = []
        one_loss = []

        for player in players:
            losses = loss_count.get(player, 0)
            if losses == 0:
                no_loss.append(player)
            elif losses == 1:
                one_loss.append(player)

        no_loss.sort()
        one_loss.sort()

        return [no_loss, one_loss]
