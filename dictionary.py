person ={
    "fist_name": "Brian",
    "last_name": "kiptoo",
    "age": 20,
    "gender": "male",
    "isActive": True

}

# accessing values using key 

# print(person["height"])

# accessing value using get method

# print(person.get("height", "key not found"))


# accessing keys using key() method 

# person_keys = person.keys()
# print(person_keys)

# accessing values using value method 

# person_values = person.values()
# print(person_values)

# ạccessing both keys and values using items() method 

items = person.items()
# print(items)

for key, value in items:
    print(f' {key} : {value}')