from cgi import test
from flask import Flask, request, Response
from Rossmann import Rossmann
import pickle
import pandas as pd

# loading model
model = pickle.load(open(r'parameter/model_rossmann.pkl', 'rb'))

# Initialize API
app = Flask(__name__)

@app.route('/rossmann/predict', methods=['POST'])
def rossmann_predict():
    test_json = request.get_json()

    if test_json: # there is data
        if isinstance(test_json, dict): # Unique sample
            test_raw = pd.DataFrame(test_json, index=[0])

        else: # Multiple samples
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
        
        # Instantiate Rossmann class
        pipeline = Rossmann()

        # data cleaning
        df1 = pipeline.data_cleaning(test_raw)

        # feature engineering
        df2 = pipeline.feature_engineering(test_raw)

        # data preparation
        df3 = pipeline.data_preparation(test_raw)

        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)

        return df_response

    else:
        return Response('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)


