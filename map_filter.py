# this example show how map function works
countries = ["Nigeria", "Ghana", "Zimbawe", "Senegal","Central Africa"]

def find_countries(str):
    if str[0] == 'N':
        return str

# note that the map function will accept 2 parameters
map_country = map(find_countries, countries)
print(map_country)

for x in map_country:
    print(x)


# this section is for the filter function 

filter_country = filter(find_countries, countries)
print(filter_country)

for x in filter_country:
    print(x)