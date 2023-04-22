import pandas as pd
from pypmml import Model
from typing import List


def predict(data: List[any]):
    model = Model.fromFile("./dtc.pmml")

    valid_data = preprocessData(data)

    if valid_data == 0:
        return -1

    prediction = model.predict(valid_data)
    print(model.inputNames)
    print(model.outputNames)
    return prediction


def preprocessData(data: List[any]):
    if len(data) != 15:
        return 0

    dataset = pd.read_csv("./lungCancerDatabase.csv")

    processed_data = []

    for index, item in enumerate(data):
        if index == 4 and type(item) == str:
            if item == "M" or item == "Male":
                processed_data.append(1)
            elif item == "F" or item == "Female":
                processed_data.append(0)
            else:
                return 0
        elif index == 5:
            if type(item) == int:
                min_val = min(dataset.iloc[:, 1])
                max_val = max(dataset.iloc[:, 1])

                processed_data.append(
                    (item - min(min_val, item))
                    / (max(max_val, item) - min(min_val, item))
                )
            else:
                return 0
        elif item == 0 or item == 1:
            processed_data.append(item)
        else:
            return 0

    return processed_data


print(predict([1, 1, 1, 1, "F", 30, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
#  1    2  3  4  5  6  7  8  9 10 11 12 13 14 15
