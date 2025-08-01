from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    message = 'hello world'
    return {'message': message}
