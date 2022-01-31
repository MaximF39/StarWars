class JSONClass:

    def __init__(self, json) -> None:
        for key, value in json.items():
            setattr(self, key, value)

