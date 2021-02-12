#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[ ]:


run = Run.get_context()
ws = run.experiment.workspace
ds = ws.datasets['housedata']


# In[ ]:


def clean_data(data):
    dCol = ['id', 'date', 'zipcode', 'waterfront', 'yr_renovated']
    data.drop(dCol, axis=1, inplace=True)
    x, y = data.drop('price', axis=1), data['price']
    return x,y


# In[ ]:


def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('lrate', type=float, default=1.0, help="Learning rate")
    parser.add_argument('niter', type=int, default=100, help="Number of iterations")

    args = parser.parse_args()

    run.log("Learning rate:", np.float(args.lrate))
    run.log("Number of iterations:", np.int(args.niter))
    x, y = clean_data(ds)
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    st = StandardScaler()
    x_train = st.fit_transform(x_train)
    x_test = st.transform(x_test)
    model = LinearRegression(lrate=args.lrate, niter=args.niter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/project_model.joblib')

if __name__ == '__main__':
    main()

