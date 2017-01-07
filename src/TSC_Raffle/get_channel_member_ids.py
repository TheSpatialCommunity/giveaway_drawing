from get_json_data import get_json_data

def get_channel_member_ids(channel_id=None, token=None):
    """ 
        Returns a list of users in a channel using Slack API channel info method 
    """
    user_ids = []

    url = "https://slack.com/api/channels.info"
    params = dict(
        token=token,
        channel=channel_id
    )
    data = get_json_data(url=url, params=params)

    # return the list of user_ids
    return data["channel"]["members"]