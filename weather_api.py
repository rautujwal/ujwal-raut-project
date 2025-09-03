from flask import Flask,request,jsonify
from flask_cors import CORS
import joblib
import pandas as pd

#creating flask app
app = Flask(__name__)
CORS(app)


#connect post API call_-__-> make a predict()function

@app.route('/predict',methods=['POST'])
def predict():
 feature_data=request.json
 for a in feature_data:
  for key,value in a.items():
   if isinstance(value,str):
    a[key]=value.lower().strip()
 df=pd.DataFrame(feature_data)
 df=df.reindex(columns=cols)
 prediction=list(model.predict(df))
 probability=list(model.predict_proba(df))
 return jsonify({'based on the features given, it will':prediction,
                'probability of rain is':probability[0][1],
                'probability of not raining is':probability[0][0]})
 

if __name__=='__main__':
 model=joblib.load('rain_model.pkl')
 cols=joblib.load('weather_columns.pkl')
 app.run(debug=True)