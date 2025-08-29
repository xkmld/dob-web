import requests
import json
import os
from bs4 import BeautifulSoup

def format_birth_date(the_date):
    the_date = the_date.lstrip()
    the_date = the_date.replace("Enero", "1")
    the_date = the_date.replace("Febrero", "2")
    the_date = the_date.replace("Marzo", "3")
    the_date = the_date.replace("Abril", "4")
    the_date = the_date.replace("Mayo", "5")
    the_date = the_date.replace("Junio", "6")
    the_date = the_date.replace("Julio", "7")
    the_date = the_date.replace("Agosto", "8")
    the_date = the_date.replace("Septiembre", "9")
    the_date = the_date.replace("Octubre", "10")
    the_date = the_date.replace("Noviembre", "11")
    the_date = the_date.replace("Diciembre", "12")
    #print(the_date)
    #print(list(filter(None,the_date.lstrip().split(" "))))
    return list(filter(None,the_date.lstrip().split(" ")))

def scrape_and_save_data():
        soup = BeautifulSoup(r.text, 'lxml')

        #print(soup)

        # name, job, img, birth_adte
        if soup.find("span", class_="bio-module__first-name") is None:
            return
        name = soup.find("span", class_="bio-module__first-name").get_text().strip()
        if soup.find("p", class_="type-20-24 bio-module__profession") is None:
            job = None
        else:
            job = soup.find("p", class_="type-20-24 bio-module__profession").get_text().strip()
        if soup.find("div", class_="profile-pictures-carousel__slide slide-0") is None:
            img = None
        else:
            img = soup.find("div", class_="profile-pictures-carousel__slide slide-0").img['src']

        birth_date = soup.find("div", class_="bio-module__person-attributes").find_next("p").get_text().strip().replace("\n", "").replace('Cumpleaños', '')

        # Birth place
        birth_place =soup.find("div", class_="bio-module__person-attributes").find_next("p").find_next("p").find_next("p").get_text().strip().replace("\n", "").replace("\t", "").rstrip().replace('Lugar de Nacimiento', '').lstrip()
        about = soup.find("div", class_="about-module section-half-bottom-desktop").find_next("p").get_text()
        before_fame = soup.find("div", class_="about-module section-half-bottom-desktop").find_next("p").find_next("p").get_text()
        curiosities = soup.find("div", class_="about-module section-half-bottom-desktop").find_next("p").find_next("p").find_next("p").get_text()
        family_life = soup.find("div", class_="about-module section-half-bottom-desktop").find_next("p").find_next("p").find_next("p").find_next("p").get_text()
        association = soup.find("div", class_="about-module section-half-bottom-desktop").find_next("p").find_next("p").find_next("p").find_next("p").find_next("p").get_text()


        data = {"name": name, "job": job, "img": img, "birth_date": format_birth_date(birth_date), "birth_place": birth_place, "about": about, "before_fame": before_fame, "curiosities": curiosities, "family_life": family_life, "association": association}


        with open(output_folder_name + name.replace(" ", "").lower() + ".json", "w") as f:
            f.write(json.dumps(data))
        print("SCRAPED AND SAVED: " + name)


input_folder_name = "data/"
output_folder_name = "data/scraped/"
file_name = input_folder_name + "links_to_scrape.txt"

if not os.path.exists(output_folder_name):
    os.makedirs(output_folder_name)

with open(file_name) as file:
    while line := file.readline():
        r = requests.get(line.rstrip())
        print("=========================================")
        scrape_and_save_data()
        #print(json.dumps(data))

