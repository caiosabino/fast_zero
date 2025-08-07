from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schema import Message, User

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    message = 'hello world'
    return {'message': message}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_html():
    html = """
    <html>
        <head>
            <title>Nosso Olá Mundo</title>
        </head>
        <body>
            <h1>Olá Mundo</h1>
        </body>
    </html>
    """

    return html


@app.get('/user', status_code=HTTPStatus.OK, response_model=User)
def read_user():
    return {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'age': 30,
        'is_admin': False,
    }
