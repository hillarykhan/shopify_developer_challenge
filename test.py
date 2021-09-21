import requests
import json

BASE = "http://127.0.0.1:5000/"

# test_videos = [{"name": "Agatha's video", "views": 15, "likes": 10},
#                 {"name": "Bernie's video", "views": 35, "likes": 11},
#                 {"name": "Cathy's video", "views": 55, "likes": 12},
#                 {"name": "David's video", "views": 85, "likes": 20},
#                 {"name": "Esther's video", "views": 805, "likes": 100}]

# for i in range(len(test_videos)):
#     response = requests.put(BASE + "videos/" + str(i), test_videos[i])
#     print(response.json())
response = requests.get(BASE + "videos/2")
print(response.json())

input() 
response = requests.patch(BASE + "videos/2", {"views": 105, "likes": 104})
print(response.json())
