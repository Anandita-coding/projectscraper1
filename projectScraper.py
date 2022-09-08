from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(url)
print(page)

soup = bs(page.text,'html.parser')
star_table= soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')
for i in table_rows:
    table_division = i.find_all('td')
    row = [j.text.rstrip() for j in table_division]
    temp_list.append(row)
    
star_names = []
distance = []
radius = []
mass = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    radius.append(temp_list[i][6])
    mass.append(temp_list[i][5])

df = pd.DataFrame(list(zip(star_names,distance,radius,mass)), columns = ['Star name','Distance','Radius','Mass'])
print(df)
df.to_csv('stars.csv')