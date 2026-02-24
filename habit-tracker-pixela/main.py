import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

TOKEN = "efsfew234dfgdfg"
USER = "microcoulomb"

# create user
# r_user = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(r_user.text)

# create graph definition
graph_header = {
    "X-USER-TOKEN": TOKEN,
}

graph_param = {
    "id": "graph1",
    "name": "Workout",
    "unit": "min",
    "type": "float",
    "color": "momiji"
}

# r_graph = requests.post(url=f"{PIXELA_ENDPOINT}/{USER}/graphs", json=graph_param, headers=graph_header)
# print(r_graph.text)

today = datetime(year=2026,month=1,day=4)
# pixel_param = {
#     "date": datetime.strftime(today, "%Y%m%d"),
#     "quantity": "5.6",
# }
#
# r_pixel = requests.post(url=f"{PIXELA_ENDPOINT}/{USER}/graphs/graph1", json=pixel_param, headers=graph_header)
# print(r_pixel.text)

pixput_param = {
    "quantity": "10.5",
}

# r_pixput = requests.put(url=f"{PIXELA_ENDPOINT}/{USER}/graphs/graph1/{datetime.strftime(today, "%Y%m%d")}",
#                         json=pixput_param,
#                         headers=graph_header)
# print(r_pixput.text)