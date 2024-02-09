import requests
from datetime import datetime

USERNAME = "apexchaosliege"
TOKEN = "pppppppppppeeepeepooopookladfjal;sfdj"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXELA_PARAMETERS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_PARAMETERS)
APPENDIXN = "graph1"
# graph_config = {
#     "id": APPENDIXN,
#     "name": "AppendixN",
#     "unit": "pages",
#     "type": "int",
#     "color": "kuro"
# }
#
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)

today = datetime.now()

post_pixela_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? "),
}

revise_pixela_parameters = {
    "quantity": "10"
}

response = requests.post(url=f"{GRAPH_ENDPOINT}/{APPENDIXN}", json=post_pixela_parameters, headers=HEADERS)

# response = requests.put(url=f"{GRAPH_ENDPOINT}/{APPENDIXN}/{post_pixela_parameters['date']}", json=revise_pixela_parameters, headers=HEADERS)

# response = requests.delete(url=f"{GRAPH_ENDPOINT}/{APPENDIXN}/{post_pixela_parameters['date']}", headers=HEADERS)
print(response.text)
