import json


def recommend_property(location, budget):

    with open("data/property_data.json","r") as file:
        properties = json.load(file)


    result = []


    for p in properties:

        if (
            p["location"].lower() == location.lower()
            and p["price"] <= budget
        ):
            result.append(p)


    return result