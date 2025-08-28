import requests
from bs4 import BeautifulSoup

folder_name = "data/"
file_name = folder_name + "links_to_scrape.txt"

with open(file_name) as file:
    while line := file.readline():
        r = requests.get(line.rstrip())
        soup = BeautifulSoup(r.text, 'lxml')
        #print(soup)
        print(soup.find("span", class_="bio-module__first-name").get_text().strip())
        print(soup.find("p", class_="type-20-24 bio-module__profession").get_text().strip())

        module_person = soup.find("div", class_="bio-module__person-attributes").get_text().strip()

        print(module_person)
        # take the birthday

        # take the Nacimiento

        break 
