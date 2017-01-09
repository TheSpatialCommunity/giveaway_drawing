from random import choice

def choose_winners(giveaway_pool=None, draw_winner_count=0):
    """
        Choose Winners from giveaway pool
    """
    winners = []

    while len(winners) < draw_winner_count:
        winner = choice(giveaway_pool.keys())
        winner = giveaway_pool[winner]
        if winner not in winners: # Don't allow someone to win twice
            winners.append(winner)

    return winners