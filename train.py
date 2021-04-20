from sklearn.linear_model import LinearRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
from azureml.core.run import Run
from azureml.core import Dataset
from sklearn.preprocessing import StandardScaler

run = Run.get_context()
ws = run.experiment.workspace
ds = ws.datasets['housedata']

def clean_data(data):
    data=data.to_pandas_dataframe()
    dCol = ['id', 'date', 'zipcode', 'waterfront', 'yr_renovated']
    data.drop(dCol, axis=1, inplace=True)
    x, y = data.drop('price', axis=1), data['price']
    return x,y

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()


    parser.add_argument('--n_jobs', type=int, default=1, help="Number of jobs")

    args = parser.parse_args()


    run.log("Number of jobs:", np.int(args.n_jobs))
    x, y = clean_data(ds)
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    st = StandardScaler()
    x_train = st.fit_transform(x_train)
    x_test = st.transform(x_test)
    model = LinearRegression(n_jobs=args.n_jobs).fit(x_train, y_train)
    y_pred = model.predict(x_test)
    mse= mean_squared_error (y_test,y_pred)
    run.log("MSE", np.float(mse))

    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/project_model.joblib')

if __name__ == '__main__':
    main()
