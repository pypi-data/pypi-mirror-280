import requests


class DatabaseManager:
    @staticmethod
    def insert_data(name, description, topics, output_format, is_active=True):
        result = requests.get(f"http://34.91.141.27/get/exists?name={name}").json()

        if result.get("status_code") != 200:
            return print("An error occurred while checking if the agent exists.")

        if "true" in result.get("message"):
            return print(f"An agent with the name '{name}' already exists.")

        data = {
            "name": name,
            "description": description,
            "topics": topics,
            "output_format": output_format,
            "is_active": is_active
        }

        requests.post("http://34.91.141.27/", json=data)
