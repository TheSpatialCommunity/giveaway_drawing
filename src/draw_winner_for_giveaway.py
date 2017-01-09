import click
import sys
from slack_config import config
import TSC_Giveaway

@click.command()
@click.option('--channel', type=click.Choice(config["channels"].keys()), prompt="The channel name to use for the giveaway pool", help="The name of the channel to pull the user list from for the giveaway")
@click.option('--count', prompt="Number of winners to choose?", default=1, help="The number of winners to choose from the pool")
@click.option('--member_csv', prompt="Path to the members list csv", help="The path to the members list csv from Slack")
def run_giveaway(channel=None, count=0, member_csv=None):
    """ 
        The Spatial Community - Draw Winner(s) for giveaway
    """
    print("\nInput Items\n")
    channel = channel.replace("#","") # In case the user provides the #
    
    if channel not in config["channels"]:
        print("The channel provided does not exist in the config file.  Aborting.\n")
        sys.exit(0)

    channel_id = config["channels"][channel]
    print("Channel:          #{0} [{1}]".format(channel, channel_id))
    print("# of Winners:     {0}".format(count))
    print("Members List CSV Path: {0}".format(member_csv))

    print("\nReading user list from members list csv")
    active_users = TSC_Giveaway.get_active_users(path_to_csv=member_csv, token=config["slack_token"])
    print("{} active users in The Spatial Community".format(len(active_users)))

    print("\nQuerying Slack API for user list from #{0}".format(channel))
    channel_members = TSC_Giveaway.get_channel_member_ids(channel_id=channel_id, token=config["slack_token"])
    print("{} users in the giveaway pool".format(len(channel_members)))

    print("\nFiltering inactive users from giveaway pool")
    cleaned_giveaway_pool = TSC_Giveaway.clean_giveaway_pool(active_users=active_users, channel_members=channel_members)
    print("{} eligible members in the giveaway".format(len(cleaned_giveaway_pool.keys())))
    
    print("\nThe winners are...")
    for i, winner in enumerate(TSC_Giveaway.choose_winners(giveaway_pool=cleaned_giveaway_pool, draw_winner_count=count)):
        print("  {0} - {1}".format(i+1, winner))

    print("\n")

if __name__ == "__main__":
    print("\nThe Spatial Community - giveaway Draw\n")
    run_giveaway()