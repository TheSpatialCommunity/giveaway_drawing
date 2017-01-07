import pandas as pd
from get_json_data import get_json_data

def get_active_users(path_to_csv=None, 
                     token=None):
    """ 
        Returns a dict of active users from The Spatial Community 
    """

    url = "https://slack.com/api/users.list"
    params = dict(
        token=token
    )

    member_list = dict()

    data = get_json_data(url=url, params=params)
    for member in data["members"]:
        member_list[member["name"]] = member["id"]

    df = pd.read_csv(path_to_csv)
    cols = df.columns
    cols = cols.map(lambda x: x.replace('-', '_') if isinstance(x, (str, unicode)) else x)
    df.columns = cols

    filtered_df = df.query("billing_active == 1")
    filtered_usernames = filtered_df.username.values.tolist()
    
    active_users = {v:k for k,v in member_list.iteritems() if k in filtered_usernames }

    return active_users
