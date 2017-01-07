import requests
import json

def get_json_data(url=None, params=None):
    """
        Downloads data from provided URL and parameters
    """
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    return data