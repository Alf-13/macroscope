import requests

def bls_survey_list():
    url = "https://api.bls.gov/publicAPI/v2/surveys"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for HTTP errors
        data = response.json()  # Converts the response to JSON format
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return data

# Example usage
if __name__ == "__main__":
    print(bls_survey_list())

