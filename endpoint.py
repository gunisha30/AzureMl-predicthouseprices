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
            bedrooms
              bathrooms
              sqft_living
              sqft_lot
              floors
              view
              condition
              grade
              sqft_above
              sqft_basement
              yr_built
              lat
              long
              sqft_living15
              sqft_lot15

          },
          {
            "city_development_index": 0.665,
            "gender": "Female",
            "relevent_experience": "Has relevent experience",
            "enrolled_university": "no_enrollment",
            "education_level": "Graduate",
            "major_discipline": "STEM",
            "experience": 18,
            "company_size": "100-500",
            "company_type": "Pvt Ltd",
            "last_new_job": 4,
            "training_hours": 43
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

