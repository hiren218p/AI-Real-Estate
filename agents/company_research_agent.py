import json


def research_company(company):

    with open("data/companies.json", "r") as file:
        companies = json.load(file)


    if company in companies:

        data = companies[company]

        return {
            "company": company,
            "location": data["location"],
            "projects": data["projects"],
            "type": data["type"],
            "overview":
            f"{company} is a {data['type']} real estate company located in {data['location']}."
        }


    return {
        "company": company,
        "location": "Unknown",
        "projects": [],
        "type": "Real Estate",
        "overview":
        f"{company} is a real estate company."
    }