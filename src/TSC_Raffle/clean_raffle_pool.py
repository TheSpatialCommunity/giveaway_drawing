

def clean_raffle_pool(active_users=None, channel_members=None):
    """
        Returns a filtered dictionary of channel members intersected with active users
    """
    
    return {k:v for k,v in active_users.iteritems() if k in channel_members}