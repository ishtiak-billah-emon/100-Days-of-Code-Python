city = [ "Dhaka", "Khulna", "Chittagong", "Rajshahi", "Barishal", "Syhlet", "Cox's Bazar"]

# list [i] == list [i - n]

del city[0]
city.remove("Syhlet")
city.append("Dinajpur")
length = len(city)
print(city)