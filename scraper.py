
import requests
import bs4
import pandas as pd
import datetime
import os
import time

#PATH = os.path.join(".","Users","xxx","Documents","py"

def table_to_df(table): 
  return pd.DataFrame([[td.text for td in row.findAll('td')] for row in table.tbody.findAll('tr')])

date = datetime.datetime(2020,1,1,12,4,5)
res = pd.DataFrame()

for i in range(314): 
    formattedDate = date.strftime("%m/%d/%y")
    print(formattedDate)

    url = 'https://coeapps.eugene-or.gov/EPDDispatchLog/Search'
    formdata = {'DateFrom': formattedDate, 'DateThrough': formattedDate, 'IncidentType': '', 'Disposition': '', 'Priority': '', 'EventNumberFilterOption': 'IsExactly', 'EventNumber': '', 'StreetNumberFilterOption': 'IsExactly', 'StreetNumber': '', 'StreetNameFilterOption': 'IsExactly', 'StreetName': '', 'CaseNumberFilterOption': 'IsExactly', 'CaseNumber': ''}

    page = requests.post(url, data=formdata)

    soup = bs4.BeautifulSoup(page.content, 'lxml')

    table = soup.find(name='table', attrs={'id':'calls'})
    res = res.append(table_to_df(table))
    res.to_csv(os.path.join(os.path.join("police_calls_2020.csv")), index=None, sep=';', encoding='cp1252')
    time.sleep(10)
    date += datetime.timedelta(days=1)

#print(result)
