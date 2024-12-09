from fastapi import FastAPI
from api_handler import FastAPIHandler

app = FastAPI()
app.handler = FastAPIHandler()

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(cus_id: int, cus_features: dict):
    prediction = app.handler.predict(cus_features)[0]
    return ({
             'PD': prediction,
             'cus_id': cus_id
            })