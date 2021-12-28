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

# write your update damages function here:
def convert_damages(lst):
    damages_updated = []
    for damage in damages:
        if damage == "Damages not recorded":
            damages_updated.append("Damages not recorded")
        elif damage.__contains__("B"):
            index_B = damage.index("B")
            damage_float_B = float(damage[:index_B])
            damage_B = damage_float_B * (10 ** 9)
            damages_updated.append(damage_B)

        elif damage.__contains__("M"):
            index_M = damage.index("M")
            damage_float_M = float(damage[:index_M])
            damage_M = damage_float_M * (10 ** 6)
            damages_updated.append(damage_M)
    return damages_updated

#print(convert_damages(damages))

# write your construct hurricane dictionary function here:
def hurricane(lst):
    hurricanes = {}
    for i in range(len(lst)):
        hurricanes[names[i]] = dict({"Name": names[i], "Month": months[i], "Year": years[i],"Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Death": deaths[i]})
    return hurricanes

#print(hurricane(names))

# write your construct hurricane by year dictionary function here:
def hurricane_by_year(lst):
    hurricane_years = {}
    for i in range(len(years)):
        if years[i] != years[i-1]:
            values = [dict(
                {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i],
                 "Areas Affected": areas_affected[i], "Damage": damages[i], "Death": deaths[i]})]
            hurricane_years[years[i]] = values

        else:
            value = hurricane_years.get(years[i-1])
            value.append(dict({"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i],
                "Areas Affected": areas_affected[i], "Damage": damages[i], "Death": deaths[i]}))
            hurricane_years[years[i]] = value
    return hurricane_years

#print(hurricane_by_year(years))

# write your count affected areas function here:
def hurricane_num_per_area(lst):
    affected_area = {}
    areas = []
    for el in lst:
        for area in el:
            if area not in areas:
                areas.append(area)
                affected_area[area] = 1
            else:
                affected_area[area] = affected_area.get(area) + 1
    return affected_area

#print(hurricane_num_per_area(areas_affected))

# write your find most affected area function here:
def most_affected_are(lst):
    affected_area = {}
    areas = []
    for el in lst:
        for area in el:
            if area not in areas:
                areas.append(area)
                affected_area[area] = 1
            else:
                affected_area[area] = affected_area.get(area) + 1

    max_area_count = max(affected_area.values())
    for key in affected_area.keys():
        if affected_area.get(key) == max_area_count:
            max_area = key
            return "The area affected by the most hurricanes is " + max_area + ", and it was hit by this hurricane " + str(max_area_count) + " times."

#print(most_affected_are(areas_affected))

# write your greatest number of deaths function here:
def max_deaths(lst):
    max_death = max(deaths)
    index_of_max_death = deaths.index(max_death)
    name_of_hurricane_max_death = names[index_of_max_death]

    #print(name_of_hurricane_max_death)
    #print(max_death)

#max_deaths(deaths)

# write your catgeorize by mortality function here:
def rating_by_death(lst):
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for death in deaths:
        if death == 0:
            index_death = deaths.index(death)
            hurricanes_by_mortality[0].append(names[index_death])
        elif death > 0 and death <= 100:
            index_death = deaths.index(death)
            hurricanes_by_mortality[1].append(names[index_death])
        elif death > 100 and death <= 500:
            index_death = deaths.index(death)
            hurricanes_by_mortality[2].append(names[index_death])
        elif death > 500 and death <= 1000:
            index_death = deaths.index(death)
            hurricanes_by_mortality[3].append(names[index_death])
        elif death > 1000 and death <= 10000:
            index_death = deaths.index(death)
            hurricanes_by_mortality[4].append(names[index_death])
        elif death > 10000:
            index_death = deaths.index(death)
            hurricanes_by_mortality[5].append(names[index_death])
    return hurricanes_by_mortality

#print(rating_by_death(deaths))

# write your greatest damage function here:
def damage_rating(lst):
    # converting damages table into more readable format
    damages_updated = []
    for damage in damages:
        if damage == "Damages not recorded":
            damages_updated.append("Damages not recorded")
        elif damage.__contains__("B"):
            index_B = damage.index("B")
            damage_float_B = float(damage[:index_B])
            damage_B = damage_float_B * (10 ** 9)
            damages_updated.append(damage_B)

        elif damage.__contains__("M"):
            index_M = damage.index("M")
            damage_float_M = float(damage[:index_M])
            damage_M = damage_float_M * (10 ** 6)
            damages_updated.append(damage_M)

    # finding the max damage & its index
    new_damage = []
    for item in damages_updated:
        if item != "Damages not recorded":
            new_damage.append(item)
    max_damage = max(new_damage)
    index_max = damages_updated.index(max_damage)
    name_of_most_damaged_hurricane = names[index_max]
    print(max_damage)
    print(name_of_most_damaged_hurricane)

#damage_rating(damages)

# write your catgeorize by damage function here:
def rating_by_damage(lst):
    damages_updated = []
    for damage in damages:
        if damage == "Damages not recorded":
            damages_updated.append("Damages not recorded")
        elif damage.__contains__("B"):
            index_B = damage.index("B")
            damage_float_B = float(damage[:index_B])
            damage_B = damage_float_B * (10 ** 9)
            damages_updated.append(damage_B)

        elif damage.__contains__("M"):
            index_M = damage.index("M")
            damage_float_M = float(damage[:index_M])
            damage_M = damage_float_M * (10 ** 6)
            damages_updated.append(damage_M)

    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],}
    for damage in damages_updated:
        if damage == "Damages not recorded":
            index_damage = damages_updated.index(damage)
            hurricanes_by_damage[0].append(names[index_damage])
        elif 0 < damage <= 100000000:
            index_damage = damages_updated.index(damage)
            hurricanes_by_damage[1].append(names[index_damage])
        elif 100000000 < damage <= 1000000000:
            index_damage = damages_updated.index(damage)
            hurricanes_by_damage[2].append(names[index_damage])
        elif 1000000000 < damage <= 10000000000:
            index_damage = damages_updated.index(damage)
            hurricanes_by_damage[3].append(names[index_damage])
        elif 10000000000 < damage <= 50000000000:
            index_damage = damages_updated.index(damage)
            hurricanes_by_damage[4].append(names[index_damage])
    return hurricanes_by_damage

#print(rating_by_damage(damages))







