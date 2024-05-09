# 1.	Stwórz listę dowolnych słowników, (może być taka jak w liście 4),
# a następnie ją zJSONUJ a później rozJSONUJ, za każdym razem wyświetlając wynik.

import json

database = {"name": "Emilia",
            "surname": "Wach",
            "age": 23,
            "sex": "female",
            "income": 8500,
            "property": 10000,
            "children": 0,
            "education": "first-degree studies",
            "cities": "Wrocław"}


# converting into JSON
json_database = json.dumps(database)
print(f'Database from Python to JSON: {json_database}')

# reconverting into python
re_json_database = json.loads(json_database)
print(f'Database from JSON to Python: {re_json_database}
