#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://d86c8f6d-4026-41c5-88ac-8bcd72752825.southcentralus.azurecontainer.io/score"

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
              bedrooms:3
              bathrooms:2.25
              sqft_living:1715
              sqft_lot:6819
              floors:2
              view:0
              condition:3
              grade:7
              sqft_above:1715
              sqft_basement:0
              #yr_built
              lat:47.3097
              long:-122.327
              sqft_living15:2238
              sqft_lot15:6819

          },
          {
            bedrooms:3
              bathrooms:1.75
              sqft_living:2450
              sqft_lot:2691
              floors:2
              view:0
              condition:3
              grade:8
              sqft_above:1750
              sqft_basement:700
              #yr_built
              lat:47.6386
              long:-122.36
              sqft_living15:1760
              sqft_lot15:3573
          },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())

