from bs4 import BeautifulSoup
import requests
import csv
import json

from urllib.request import urlopen

class Scrapper:
    def analyze_tournament(self, tournament_name, seed_link):
        r = requests.get(seed_link)

        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.find_all('tr')

        count=0
        results = []
        for debater in rows:
            #Header
            if count==0:
                columns = debater.find_all('th')
            else:
                columns = debater.find_all('td')

            row = []
            for column in columns:
                row.append(column.get_text().strip())
            results.append(row)

            print(str(count+1) + "/" + str(len(rows)))

            count+=1

        path = "results/" + tournament_name + ".csv"
        self.export_csv(results, path)

    def export_csv(self, results, path):
        with open(path, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in results:
                spamwriter.writerow(row)
