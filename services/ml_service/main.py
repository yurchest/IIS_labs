from fastapi import FastAPI
from api_handler import FastAPIHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Gauge, Counter, Summary

app = FastAPI()
app.handler = FastAPIHandler()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

prediction_metric = Histogram(
    'prediction_metric_histogram',
    'histogram of predicted score',
    buckets=(0.2, 0.4, 0.6, 0.8, 1)
)

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(cus_id: int, cus_features: dict):
    prediction = app.handler.predict(cus_features)[0]
    prediction_metric.observe(prediction)
    return ({
             'PD': prediction,
             'cus_id': cus_id
            })