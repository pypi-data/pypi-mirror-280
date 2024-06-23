from datadict import DataDict

data = [
    {"name": "John", "age": 20},
    {"name": "Jane", "age": 21},
    {"name": "Jim", "age": 22},
    {"name": "Jack", "age": 23, "heart_rate": {"value": 120, "unit": "bpm"}},
]

pyplup = DataDict(data)
# print(pyplup)
# print(type(pyplup[0]))


# print(pyplup.select("name"))
# print(pyplup.select("name", "age"))

print(pyplup.where("name", "==", "John"))
print(pyplup.where("heart_rate.value", ">", 100))

print(pyplup.where("heart_rate.value", ">", 100).select("name", "heart_rate.value"))

pyplup.append({"name": "Josh", "age": 35})

print(pyplup)

pyplup.sort(key=lambda x: x["age"], reverse=True)
sorted_data = pyplup
print("Sorted by age:", sorted_data)


# pyplup.append("hello")

# print(pyplup)

# print("\n")

# print(dir(list))


# print(dir(dict))

d = {"a": 1, "b": 2, "c": 3}
