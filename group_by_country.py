from collections import defaultdict
from itertools import islice, groupby

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data=data):
    country_names_dict = defaultdict(list)
    for item in islice(data.splitlines(), 1, None):
        country_list = item.strip().split(',')
        country_names_dict[country_list[-1]].append(' '.join(country_list[:-1]))
    return country_names_dict



def group_names_by_country_two(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    for line in data.splitlines()[1:]:
        last_name, first_name, country = line.split(',')
        name = f'{first_name} {last_name}'
        countries[country].append(name)
    return countries

print(group_names_by_country())
print(group_names_by_country())