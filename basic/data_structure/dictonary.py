class Dictionary:
    map = {1: "Ram"}
    map[2] = "Shyam"
    map[3] = "hari"
    map[3] = "Hari"

    print(map)
    keys = map.keys()
    values = map.values()
    print(keys)
    print(values)
    items = map.items()
    print(items)
    if "Ram" in map:
        print("True")

    print(map.get(1, "Lakshman"))

    for key in map:
        print(key)

    for key, value in map.items():
        print(f"kes: {key} value: {value}")

    print(map.pop(2))