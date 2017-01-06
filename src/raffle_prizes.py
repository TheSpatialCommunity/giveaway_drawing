import random, requests
from slack_config import config

def get_channel_members(channel, token):
	""" return a list of users in a channel using channel info method 
		https://slack.com/api/channels.info?token=XYZ&channel=C06QBUKCK
		"id": "C3NFP1J84",
            	"name": "raffle_devsummit_2017",
		"id": "C3NBEP5CK",
            	"name": "raffle_foss4g_2017",
		"id": "C3P4B10F9",
            	"name": "raffle_pycon_2017","""
	user_ids = []
	# return the user name and their ID
	return user_ids

def get_user_name (user_id, token):
	""" check if user is active. looks like if the user is not found it is inactive.
	i tested with user ID "T06QBQ0DV" (known inactive and i get "no such user" error)
		https://slack.com/api/users.info?token=XYZ&user=XYZ"""
	user_name = ""
	#get user name from the winning ID
	return user_name
	
def main():
	""" 
		TSC Raffle Prize 
	"""
	
	pass

if __name__ == "__main__":
	main()
