#cars={"key":{"key":"value"}}

cars={"BMW":{"model":2020,"color":"brown"},"Audi":{"model":2019,"color":"white"}}
print(cars)
print(cars["BMW"]["color"])
print(cars.keys())
print(cars.values())

for k,v in cars.items():
    print(k,v)