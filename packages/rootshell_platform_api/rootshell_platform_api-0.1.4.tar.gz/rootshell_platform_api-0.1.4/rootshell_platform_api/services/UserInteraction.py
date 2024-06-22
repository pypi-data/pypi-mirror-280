class UserInteraction:
    def __init__(self, client):
        self.client = client

    def list_entities(self, fetch_method, entity_name: str):
        entities = fetch_method()
        if not entities or not isinstance(entities, dict) or "data" not in entities:
            print(f"No {entity_name} found.")
            return []

        print(f"\nAvailable {entity_name.capitalize()}:")
        for entity in entities["data"]:
            print(f"- {entity_name.capitalize()} ID: {entity['id']}, {entity_name.capitalize()} Name: {entity['name']}")

        return entities["data"]

    def select_entity(self, fetch_method, entity_name: str):
        entities = self.list_entities(fetch_method, entity_name)
        if not entities:
            return None

        while True:
            try:
                entity_id = int(input(f"\nEnter the {entity_name.capitalize()} ID: "))
                if any(entity["id"] == entity_id for entity in entities):
                    return entity_id
                else:
                    print(f"Invalid {entity_name.capitalize()} ID. Please select from the list.")
            except ValueError:
                print(f"Invalid input. Please enter a valid {entity_name.capitalize()} ID.")
