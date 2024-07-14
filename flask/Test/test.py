import base64
import requests
import json

import config


def create_payload():
    
    payload_structure = {
        "body": {
            "name": True
        }
    }

    return payload_structure
    

def get_features(path: str, url: str = config.HOSTED_URL):
    """
    send a post REST api request to flask backend
    """
    image_payload = create_payload()
    headers = {'Content-Type': 'application/json'}
    endpoint_response = requests.post(url, data = json.dumps(image_payload), headers = headers)
    response = getattr(endpoint_response, '_content').decode("utf-8")
    #final_response = json.loads(response)

    return response


if __name__ == "__main__":
    image_path = "test_image.jpg"
    response = get_features(image_path)
    print(response)