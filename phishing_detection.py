import requests

def check_url(url):
    try:
        api_url = f"https://phishstats.info:2096/api/phishing?url={url}"
        response = requests.get(api_url, timeout=5)
        
        if response.ok:
            data = response.json()
            if isinstance(data, list) and len(data) > 0 and 'is_phishing' in data[0]:
                return data[0]['is_phishing']
            else:
                print("Unexpected response format.")
                return False
        else:
            print("Failed to get response from API.")
            return False
    except requests.RequestException as e:
        print(f"Error in API request: {e}")
        return False