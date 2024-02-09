import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, data):
        self.data = data

    def put_data(self, url):
        for i in range((len(self.data))):
            response = requests.put(url=url+f"/{i+2}", json={"price": self.data[i]})
            print(response)