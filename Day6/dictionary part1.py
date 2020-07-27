#Dictionary comes with pair(key&value)
#single key with single value->dictionary
#single key with multiple value->nested dictionary
#if it s duplicated then it will be replaced with latest

my_dict={"name":"Leka","city":"canada","Expinyrs":"3yrs"}
print(type(my_dict))
print(my_dict)
print(my_dict["name"])
print(my_dict.keys())
print(my_dict.values())
my_dict["course"]="python Selenium"
my_dict["name"]="sarath"
print(my_dict)
my_dict.pop("city")
print(my_dict)