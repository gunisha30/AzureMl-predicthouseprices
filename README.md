# House Price Prediction

This project aims at predicting house sale prices in King County, USA. It consists of two parts, one involving model building using AutoML and another one is via Hyperdrive which is used to tune hyper-parameters. Microsoft Azure's Machine Learning Studio is used to run the project.

## Dataset

1. The dataset is taken from Kaggle. Link- https://www.kaggle.com/harlfoxem/housesalesprediction
2. Features: The data contains columns such as area in sq ft, number of bedrooms and bathrooms, year of build of the house, sale price, a rating of the condition of the house etc.
3. The task is a Regression problem where house sale prices have to be predicted.
4. The dataset is uploaded ot the Microsoft Azure portal. 


![image](https://github.com/gunisha30/AzureMl-predicthouseprices/blob/main/datasetname.png)
## Automated ML

1. Here are the details set for executing Auto ML run:

![image](https://github.com/gunisha30/AzureMl-predicthouseprices/blob/main/automlconfigurations.png)

2. The metric for evaluation is root mean squared error since the model is Linear Regression model. Early stopping is enabled to prevent over-fitting. Price is the target variable. 
3. Results

![image](https://github.com/gunisha30/AzureMl-predicthouseprices/blob/main/automlrundetails.png)
![image](https://github.com/gunisha30/AzureMl-predicthouseprices/blob/main/listofmodels.png)
![image](https://github.com/gunisha30/AzureMl-predicthouseprices/blob/main/automl.png)
![image](https://github.com/gunisha30/AzureMl-predicthouseprices/blob/main/automllogs.png)
![image](https://github.com/gunisha30/AzureMl-predicthouseprices/blob/main/rundetails.png)


The performance of predictions can be improved by using a more powerful algorithm. 

## Hyperparamter Tuning using Hyperdrive

1. Linear Regression is used as it is a basic and easy to train model. 
2. The hyperparameter used is number of jobs (n_jobs), Linear Regression does not have a large variety of hyper parameters. 
3. Results:


