
import logging
import pandas as pd
import dill as pkl

logger = logging.getLogger("uvicorn.error")
class FastAPIHandler():

    def __init__(self):
        logger.warning('Loading model...')
        try:
            self.model = pkl.load(open('../models/model.pkl', 'rb'))
            logger.info('Model is loaded')

        except Exception as e:
            logger.error('Error loading model')

    def predict(self, cus_features:dict):
        item_df = pd.DataFrame(data=cus_features, index=[0])
        prediction = self.model.predict_proba(item_df)
        return (prediction[0])