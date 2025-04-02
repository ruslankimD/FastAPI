# FastAPI
<h1>Project Structure</h1>

<h3>main.py — The main file where the FastAPI application and endpoints for diabetes prediction are defined.
request.py — This file contains the DiabetesRequest class, which describes the structure of the input data for prediction.
train.py — This file is used to train models on the diabetes dataset.</h3>

<h1>Train file</h1>
<h3>The train file divided into several points

Loading data:
Data is loaded using pd.read_csv() (e.g. from diabetes_prediction_dataset.csv).
Features (X) and target variable (y) are extracted from the data.

Transforming data:
For numeric data, StandardScaler is used to standardize it.
For categorical data, OneHotEncoder is used to transform strings into numeric features.

RandomForest Model:
A pipeline with transformers and a RandomForest classifier is created.

Train the model: The model is trained on the training data, and then evaluated on the test data.

Save the model: The model is saved to the diabetes_model.pkl file using joblib.
train.

The accuracy of the model is 95 percent
</h3>

<h1>Request file</h1>

<h3>DiabetesRequest class: This is a data model defined using the Pydantic library. Each attribute in the class represents an input parameter for prediction, such as age, gender, hypertension, etc. 
The parameters are described using Field(), where you can specify additional constraints, such as: 
Pattern for gender (Male or Female only). 
Range of values ​​for some numeric fields.
to_features() method: Converts an object into a list of features that are used in the model to make predictions. This list is passed to the model, which makes a prediction based on the data passed in.
request
</h3>
