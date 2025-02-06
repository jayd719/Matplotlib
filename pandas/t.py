import json
import pandas as pd


class JsonObject(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_json(self):
        """Convert the dictionary to a JSON string."""
        return json.dumps(self, indent=4)

    @classmethod
    def from_json(cls, json_str: str):
        """Create an instance of JsonObject from a JSON string."""
        return cls(json.loads(json_str))

    @classmethod
    def from_json(cls, fh: open):
        """Create an instance of JsonObject from a JSON string."""
        return cls(json.load(fh))

    def save(self, fh: open):
        return json.dump(self, fh)

    def print(self):
        df = pd.DataFrame(self)
        print(df.transpose())


# Example Usage
data = JsonObject().from_json(open("data.json", "r", encoding="utf-8"))
print(data)
