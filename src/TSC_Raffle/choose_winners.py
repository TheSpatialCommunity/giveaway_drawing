from random import choice

def choose_winners(raffle_pool=None, draw_winner_count=0):
    """
        Choose Winners from raffle pool
    """
    winners = []

    while len(winners) < draw_winner_count:
        winner = choice(raffle_pool.keys())
        winner = raffle_pool[winner]
        if winner not in winners: # Don't allow someone to win twice
            winners.append(winner)

    return winners