import pandas as pd
import joblib


def predict(data):
    model = joblib.load("./models/dtc_model.joblib")

    valid_data = preprocessData(data)

    if valid_data == 0:
        return -1

    prediction = model.predict([valid_data])

    return int(prediction[0].item())


def preprocessData(data):
    if len(data) != 15:
        return 0

    dataset = pd.read_csv("./dataset/lungCancerDatabase.csv")

    processed_data = []

    for index, item in enumerate(data):
        if index == 0 and type(item) == str:
            if item == "M" or item == "Male":
                processed_data.append(1)
            elif item == "F" or item == "Female":
                processed_data.append(0)
            else:
                return 0
        elif index == 1:
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


# print(predict(["M", 21, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
