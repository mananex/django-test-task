import requests

requests.post('http://127.0.0.1:8000/api/create',
             data = {
                 "header": "Dogs is cool",
                 "text": "Lorem ipsum...",
                 "tags": "animals"
            },
            files = {"image": open('camera.jpg', 'rb')}) 