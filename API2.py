import pandas as pd
import json
import requests


def main():
    df = pd.read_csv("SalesLT_Customer.csv").drop(columns=["ModifiedDate"]).head(5)
    df.head()

    model_input_data = df

    data_dict = model_input_data.to_dict(orient='list')
    data_json = json.dumps({"data": data_dict})

    with open("uri.json", "r") as f:
        scoring_uri = json.load(f)["URI"][0]

    headers = {"Content-Type": "application/json"}

    response = requests.post(scoring_uri, data=data_json, headers=headers)

    if response.status_code == 200:
        result = json.loads(response.json())
        print(result)
        parsed_data = json.loads(data_json)
        parsed_data["Exited"] = result
        print("="*50)
        print("Datos Originales:")
        print(parsed_data)
    else:
        print(f"Error: {response.text}")


if __name__ == "__main__":
    main()