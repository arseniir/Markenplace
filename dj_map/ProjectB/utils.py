import requests


class important:
    def ara():
        response = requests.get('http://127.0.0.1:8000/api/comment/')
        tojson = response.json()
        return tojson
    

