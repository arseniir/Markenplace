from dj_map.celery import app
import requests


@app.task
def sale_beet_task():
    response = requests.get('http://127.0.0.1:8000/api/products/')

    products = response.json()
    for price in products.price:
        result = price - (price*10)/100
        print('this task works well')
        return result

    


