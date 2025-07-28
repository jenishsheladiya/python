# JSON Handling
import json
data = '{"name": "Ravi", "age": 22}'
obj = json.loads(data)
print(obj["name"])
