import json

# сериализация
# dump(), dumps()

# dict -> object
# list, tuple -> array
# str -> string
# int, float -> number
# True, False -> true, false
# None -> null

data = {
    "data1": {
        "data2": 1,
        "data3": 2
    }
}

# with open("json_example.json", "w") as json_file:
#     json.dump(data, json_file)

# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))

# десериализация
# load(), loads()

# with open("example_1.json") as json_to_read:
#     read_data = json.load(json_to_read)
#
# print(read_data)
# print(type(read_data))
