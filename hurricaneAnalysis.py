# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


# test function by updating damages
def update_damages():
    damages_update = []
    not_record = "Damages not recorded"
    for r in range(len(damages) - 1):
        if damages[r] == not_record:
            damages_update.append(not_record)
        else:
            new_word = ""
            for x in damages[r]:
                if x == 'M':
                    new_word = float(new_word)
                    damages_update.append(int(new_word * conversion['M']))
                elif x == 'B':
                    new_word = float(new_word)
                    damages_update.append(int(new_word * conversion['B']))
                else:
                    new_word += str(x)
    return damages_update


damages = update_damages()

print(damages)
print('\n')

# 2
# Create a Table
new_dictionary = {}


def creating_data_dictionary():
    for r in range(len(names) - 1):
        new_dictionary[names[r]] = {'Name': names[r], 'Month': months[r], 'Year': years[r],
                                    'Max Sustained Wind': max_sustained_winds[r], 'Areas Affected': areas_affected[r],
                                    'Damage': damages[r], 'Deaths': deaths[r]}
    print(new_dictionary)
    print('\n')
    return new_dictionary


# Create and view the hurricanes dictionary
creating_data_dictionary()

# 3
# Organizing by Year
year_dictionary = {}


def new_year_dictionary():
    for y in years:
        year_dictionary[y] = []
        store_data = list(new_dictionary.values())
        for s in store_data:
            if s["Year"] == y:
                year_dictionary[y].append(s)
    print(year_dictionary)
    print('\n')
    return year_dictionary


# create a new dictionary of hurricanes with year and key
new_year_dictionary()


# 4
# Counting Damaged Areas
def counting_damaged_areas():
    list_areas_affected = []
    empty_list = []
    for x in areas_affected:
        for y in x:
            list_areas_affected.append(y)
            empty_list.append('')
    list_areas_affected.sort()
    new_dict = {k: v for k, v in zip(list_areas_affected, empty_list)}
    for n in new_dict:
        count = list_areas_affected.count(n)
        new_dict[n] = count
    print(new_dict)
    print('\n')
    return new_dict


# create dictionary of areas to store the number of hurricanes involved in
counting_damaged_areas()


# 5
# Calculating Maximum Hurricane Count
def calc_max_hurricane_count():
    count = 0
    name = []
    dict_internal = counting_damaged_areas()
    for i in dict_internal:
        if dict_internal[i] > count:
            name = i
            count = dict_internal[i]
        elif dict_internal[i] == count:
            name.append(i)
        else:
            continue
    print('{name} has been affected {count} times. It is the most affected area.'.format(name=name, count=count))
    return {name: count}


# find most frequently affected area and the number of hurricanes involved in
print(calc_max_hurricane_count())
print('\n')


# 6
# Calculating the Deadliest Hurricane
def calc_deadliest_hurricane():
    name = []
    count = 0
    num_index = 0
    for d in deaths:
        if d > count:
            count = d
            num_index = deaths.index(d)
        else:
            continue
    name = names[num_index]
    print('The hurricane that caused the greatest number of deaths was {name} with {count} deaths.'.format(name=name,
                                                                                                           count=count))
    return {name: count}


# find highest mortality hurricane and the number of deaths
print(calc_deadliest_hurricane())
print('\n')

# 7
# Rating Hurricanes by Mortality
mortality_scale = {
    0: 0,
    1: 100,
    2: 500,
    3: 1000,
    4: 10000}


def rate_hurricane_by_mort():
    rate_hurricanes = {}
    rate_mortality_scale = list(mortality_scale)
    rate_list = []
    for d in deaths:
        if d >= 10000:
            rate_list.append(rate_mortality_scale[-1])
        elif d >= 1000:
            rate_list.append(rate_mortality_scale[-2])
        elif d >= 500:
            rate_list.append(rate_mortality_scale[-3])
        elif d >= 100:
            rate_list.append(rate_mortality_scale[-4])
        else:
            rate_list.append(rate_mortality_scale[0])
    rate_hurricanes = {k: v for k, v in zip(names, rate_list)}
    print(rate_hurricanes)
    print('\n')
    return rate_hurricanes


# categorize hurricanes in new dictionary with mortality severity as key
rate_hurricane_by_mort()


# 8 Calculating Hurricane Maximum Damage
def calc_great_damage_hurricane():
    name = []
    count = 0
    num_index = 0
    for d in damages:
        if isinstance(d, str):
            continue
        elif d > count:
            count = d
            num_index = damages.index(d)
        else:
            continue
    name = names[num_index]
    print('The hurricane that caused the greatest damages was {name} with a cost of {count} dollars.'.format(name=name,
                                                                                                             count=count
                                                                                                             ))
    print('\n')
    return {name: count}


# find highest damage inducing hurricane and its total cost
calc_great_damage_hurricane()

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


def rate_hurricane_by_damage():
    rate_hurricanes_damage = {}
    rate_damage_scale = list(damage_scale)
    damage_usd_rate = list(damage_scale.values())
    rate_list = []
    for d in damages:
        if isinstance(d, str):
            rate_list.append(rate_damage_scale[0])
        else:
            if d >= damage_usd_rate[-1]:
                rate_list.append(rate_damage_scale[-1])
            elif d >= damage_usd_rate[-2]:
                rate_list.append(rate_damage_scale[-2])
            elif d >= damage_usd_rate[-3]:
                rate_list.append(rate_damage_scale[-3])
            elif d >= damage_usd_rate[-4]:
                rate_list.append(rate_damage_scale[-4])
            else:
                rate_list.append(rate_damage_scale[0])
    rate_hurricanes_damage = {k: v for k, v in zip(names, rate_list)}
    print(rate_hurricanes_damage)
    print('\n')
    return rate_hurricanes_damage


# categorize hurricanes in new dictionary with damage severity as key
rate_hurricane_by_damage()