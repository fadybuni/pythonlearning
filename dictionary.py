capitals = {"USA" : "WASHINGTON DC","india" : "New Delhi","China" : "beijing","Russia" : "Moscow"}

#print(dir(capitals))
#print(help(capitals))
print(capitals.get("USA"))

if capitals.get("japan"):
    print("That capital exists")
else:
    print("The capital doesn't exist")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#capitals.clear()

#keys = capitals.keys()

#values = capitals.values()
#print(keys)

#print(values)

items = capitals.items()
for key,value in capitals.items():
    print(f"{key}: {value}")