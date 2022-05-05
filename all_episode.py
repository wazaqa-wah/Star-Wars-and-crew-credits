import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import json

#all Star Wars credit webpage codes:
#(1977) 4 Star Wars: tt0076759
#(1980) 5 Empire strikes back: tt0080684
#(1983) 6 Return of the Jedi: tt0086190
#(1999) 1 The Phantom Menace: tt0120915
#(2002) 2 Attack of the Clones: tt0121765
#(2005) 3 Revenge of the Sith: tt0121766
#(2015) 7 The Force Awakens: tt2488496
#(2017) 8 The Last Jedi: tt2527336
#(2019) 9 The Rise of Skywalker: tt2527338



url = "https://www.imdb.com/title/tt2527338/fullcredits/?ref_=tt_cl_sm"

r = requests.get(url)

soup =  BeautifulSoup(r.text,features= "html.parser")

IX_data = []

main_div = soup.find('div',{'id':'main'})

if main_div:

    # look for all the tables in the main div
    tables = main_div.findAll('table')

    # loop through each table
    for table in tables:

        # find all # <tr>
        trs = table.findAll('tr')
        for tr in trs:

            person_data = []

            # so here each tr is a person
            # get the specific cells
            tds = tr.findAll(True, {'class':['name','credit']})

            for td in tds:

                # see if it has a class
                if td.get('class'):
                    class_name = td.get('class')
                    # this always returns it as a list
                    # so get the first element
                    class_name = class_name[0]
                else:
                    # there is no class="xxxx"

                    class_name = None

                # now look inside the td for any <a> link
                # want to save the text inside and if there is a link
                # then that might be useful
                alink = td.find('a')

                if alink:

                    url = alink.get('href')

                else:

                    url = None


                # and last get the text of the element

                text = td.text
                # clean it up
                text = text.strip()

                # add it to our data
                person_data.append({
                    "url": url,
                    "text": text
                })


            # add the person data into the all data
            IX_data.append(person_data)
            #print(person_data)



else:

    print("Error could not find main div")



json.dump(IX_data,open('IX_data.json','w'),indent=2)

