# lung-cancer-api

This repo is part of an Artificial Intelligence lesson that involves training several classification models with different algorithms, and implementing the most accurate one with a front-end interface to make new predictions.

This API was designed to enable my [Android application](https://github.com/carled7/lung-cancer-predictor.git) to handle a Python object that has been exported as a `.joblib` file after being trained in Google Colab. This allows the user to input new data and obtain a predicted result.

## AI model

The model was trained on a [lung cancer dataset](https://www.kaggle.com/datasets/nancyalaswad90/lung-cancer), which is a `.csv` table that has 16 features, with one of them being the target variable, and approximately 300 rows. Tasks such as data pre-processing, plotting, encoding, and splitting were performed in a Google Colab [notebook](https://colab.research.google.com/drive/1Ykb9ENb7G2OHcHCxXh5GQnooAujCDK0s?usp=sharing). The following algorithms were used for training:

- Decision Tree
- Support Vector Machine
- K Nearest Neighbors
- RNA Multi-Layer Perceptron

The most accurate algorithm was the Decision Tree, which was exported as a `.joblib` file for this API to handle. Despite being the most accurate, the model may give some questionable results, likely due to the dataset having too few records and variables such as age, as well as the target variable being highly unbalanced.
