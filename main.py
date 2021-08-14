import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pathlib
import logging
from webdriver_manager.firefox import GeckoDriverManager


def view_staff_file(tds, count, file_path, group, group_no, soup):
    for tr in tds:
        if count == 0:
            try:
                with file_path.open(mode="a") as file:
                    file.write(f"{sezon},{wyscig}.{dane},{group} - {group_no},")
            except OSError:
                logging.error("Error")
            soup.find("tr")
        soup.find("tr")
        if count > 1:
            try:
                with file_path.open(mode="a", encoding="utf-8") as file:
                    file.write(tr.text.strip().replace(".", "").
                               replace("$", ""))
            except OSError:
                logging.error("Error")
            if count != 11:
                try:
                    with file_path.open(mode="a", encoding="utf-8") as file:
                        file.write(",")
                except OSError:
                    logging.error("Error")
        count += 1
        if count == 12:
            count = 0
            try:
                with file_path.open(mode="a") as file:
                    file.write("\n")
            except OSError:
                logging.error("Error")
    group_no += 1


def best_cars():
    lvl = 0
    file_path = pathlib.Path("BestCars.csv")
    try:
        with file_path.open(mode="w") as file:
            file.write(f"Sezon,Wyścig,Poz.,Nazwisko,Grupa,lvl\n")
    except OSError:
        logging.error("Error")
    url = "https://gpro.net/pl/Stats.asp?type=bestcars&Page=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    max_page = soup.find_all("u")
    max_page_number = None
    for u in max_page:
        max_page_number = u
    max_pageno = int(max_page_number.text.strip()) + 1
    count = 0
    countall = 0
    for page_no in range(1, max_pageno):
        url = "https://gpro.net/pl/Stats.asp?typ" \
              "e=bestcars&Page={}".format(page_no)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        tbs = soup.find(id="Table16")
        tds = tbs.find_all("td")
        for tr in tds:
            if countall < 4:
                countall += 1
                continue
            tbs.find("tr")
            if count == 0:
                # print(season + '\t')
                count += 1
                try:
                    with file_path.open(mode="a") as file:
                        file.write(f"{sezon},")
                except OSError:
                    logging.error("Error")
            if count == 1:
                # print(race + '\t')
                count += 1
                try:
                    with file_path.open(mode="a") as file:
                        file.write(f"{wyscig}.{dane},")
                except OSError:
                    logging.error("Error")
            if count <= 5:
                try:
                    with file_path.open(mode="a", encoding="utf-8") as file:
                        file.write(tr.text.strip())
                        if count != 4:
                            file.write(",")
                except OSError:
                    logging.error("Error")
            if count == 6:
                tr.find_all("img")
                for _ in tr:
                    lvl += 1
                lvl -= 2
                try:
                    with file_path.open(mode="a") as file:
                        file.write(str(lvl))
                except OSError:
                    logging.error("Error")
                lvl = 0
            count += 1
            countall += 1
            if count == 7:
                try:
                    with file_path.open(mode="a") as file:
                        file.write("\n")
                except OSError:
                    logging.error("Error")
                count = 0
        print(f"Pobieranie najlepszych bolidów str {page_no}/{max_pageno - 1}")
        page_no += 1
        countall = 0


def view_staff():

    group = "Rookie"
    file_path = pathlib.Path("ViewStaff.csv")
    try:
        with file_path.open(mode="w") as file:
            file.write('Sezon,Wyścig,Grupa,'
                       'Nazwisko menadżera,Nazwisko '
                       'kierowcy,OW,Pensja,Długość,Nazwisko dyr te'
                       'chnicznego,OW,'
                       'Pensja,Długość,OW Personelu\n')
    except OSError:
        logging.error("Error")
    for group_no in range(1, 151):
        url = str(f"https://gpro.net/pl/ViewStaff.asp?group={group} "
                  f"- {group_no}")
        page = requests.get(url)
        print(f"Pobieranie strony {url}")

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        view_staff_file(tds, count, file_path, group, group_no, soup)
    group = "Amateur"
    for group_no in range(1, 81):
        url = "https://gpro.net/pl/ViewStaff.asp?group={} - {}"\
            .format(group, group_no)
        page = requests.get(url)
        print(f"Pobieranie strony {url}")

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        view_staff_file(tds, count, file_path, group, group_no, soup)
    group = "Pro"
    for group_no in range(1, 26):
        url = "https://gpro.net/pl/ViewStaff.asp?group={} - {}"\
            .format(group, group_no)
        page = requests.get(url)
        print(f"Pobieranie strony {url}")

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        view_staff_file(tds, count, file_path, group, group_no, soup)
    group = "Master"
    for group_no in range(1, 6):
        url = "https://gpro.net/pl/ViewStaff.asp?group={} - {}"\
            .format(group, group_no)
        page = requests.get(url)
        print(f"Pobieranie strony {url}")

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        view_staff_file(tds, count, file_path, group, group_no, soup)
    group = "Elite"
    for group_no in range(1, 2):
        url = "https://gpro.net/pl/ViewStaff.asp?group={} - {}"\
            .format(group, group_no)
        page = requests.get(url)
        print(f"Pobieranie strony {url}")

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        view_staff_file(tds, count, file_path, group, group_no, soup)


def rich():
    file_path = pathlib.Path("Rich.csv")
    try:
        with file_path.open(mode="w") as file:
            file.write(f"Sezon,Wyścig,Poz.,Nazwisko,Grupa,Budżet\n")
    except OSError:
        logging.error("Error")
    url = "https://gpro.net/pl/Stats.asp?type=richmanagers&Page=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    max_page = soup.find_all("u")
    for u in max_page:
        max_page_number = u
    max_pageno = int(max_page_number.text.strip()) + 1
    count = 0
    countall = 0
    for page_no in range(1, max_pageno):
        url = str(f"""
                https://gpro.net/pl/Stats.asp?type=richmanagers&Page={page_no}
                """)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        tbs = soup.find(id="Table16")
        tds = tbs.find_all("td")
        for tr in tds:
            if countall < 4:
                countall += 1
                continue
            if count == 0:
                try:
                    with file_path.open(mode="a") as file:
                        file.write(
                            f"{sezon},{wyscig}.{dane},")
                except OSError:
                    logging.error("Error")
            tbs.find("tr")
            if count == 3:
                try:
                    with file_path.open(mode="a") as file:
                        file.write(tr.text.strip().replace(".", "").
                                   replace("$", ""))
                except OSError:
                    logging.error("Error")
            else:
                try:
                    with file_path.open(mode="a") as file:
                        file.write(tr.text.strip())
                except OSError:
                    logging.error("Error")
            if count != 3:
                try:
                    with file_path.open(mode="a") as file:
                        file.write(",")
                except OSError:
                    logging.error("Error")
            count += 1
            countall += 1
            if count == 4:
                try:
                    with file_path.open(mode="a") as file:
                        file.write("\n")
                except OSError:
                    logging.error("Error")
                count = 0
        print(f"Pobieranie budżetów str {page_no}/{max_pageno - 1}")
        page_no += 1
        countall = 0


def expenses():
    file_path = pathlib.Path("Expenses.csv")
    try:
        with file_path.open(mode="w") as file:
            file.write(f"Sezon,Wyścig,Poz.,Nazwisko,Grupa,Budżet\n")
    except OSError:
        logging.error("Error")
    url = "https://gpro.net/pl/Stats.asp?type=mostcost&Page=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    max_page = soup.find_all("u")
    for u in max_page:
        max_page_number = u
    max_pageno = int(max_page_number.text.strip()) + 1
    count = 0
    countall = 0
    for page_no in range(1, max_pageno):
        url = str(f"""
                    https://gpro.net/pl/Stats.asp?type=mostcost&Page={page_no}
                    """)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        tbs = soup.find(id="Table16")
        tds = tbs.find_all("td")
        for tr in tds:
            if countall < 4:
                countall += 1
                continue
            if count == 0:
                try:
                    with file_path.open(mode="a") as file:
                        file.write(
                            f"{sezon},{wyscig}.{dane},")
                except OSError:
                    logging.error("Error")
            tbs.find("tr")
            if count == 3:
                try:
                    with file_path.open(mode="a") as file:
                        file.write(tr.text.strip().replace(".", "").
                                   replace("$", ""))
                except OSError:
                    logging.error("Error")
            else:
                try:
                    with file_path.open(mode="a") as file:
                        file.write(tr.text.strip())
                except OSError:
                    logging.error("Error")
            if count != 3:
                try:
                    with file_path.open(mode="a") as file:
                        file.write(",")
                except OSError:
                    logging.error("Error")
            count += 1
            countall += 1
            if count == 4:
                try:
                    with file_path.open(mode="a") as file:
                        file.write("\n")
                except OSError:
                    logging.error("Error")
                count = 0
        print(f"Pobieranie wydatków str {page_no}/{max_pageno - 1}")
        page_no += 1
        countall = 0


def man_sponsors():
    group = "Rookie"
    season = "83"
    race = "3"
    file = open("ManSponsors.txt", "w")
    file.write("")
    file.close()
    for group_no in range(1, 151):
        url = "https://gpro.net/pl/ManSponsors.asp?group={} - {}" \
            .format(group, group_no)
        page = requests.get(url)
        print(url)

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            if 4 <= count <= 8 or count == 15:
                file = open("ManSponsors.txt", "a")
                file.write(tr.text.strip())
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                file = open("ManSponsors.txt", "a")
                file.write(str(lvl))
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if count == 16:
                # print('')
                count = 0
                file = open("ManSponsors.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1
    group = "Amateur"
    for group_no in range(1, 81):
        url = "https://gpro.net/pl/ManSponsors.asp?group={} - {}" \
            .format(group, group_no)
        page = requests.get(url)
        print(url)

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            if 4 <= count <= 8 or count == 15:
                file = open("ManSponsors.txt", "a")
                file.write(tr.text.strip())
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                file = open("ManSponsors.txt", "a")
                file.write(str(lvl))
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if count == 16:
                # print('')
                count = 0
                file = open("ManSponsors.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1
    group = "Pro"
    for group_no in range(1, 26):
        url = "https://gpro.net/pl/ManSponsors.asp?group={} - {}" \
            .format(group, group_no)
        page = requests.get(url)
        print(url)

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            if 4 <= count <= 8 or count == 15:
                file = open("ManSponsors.txt", "a")
                file.write(tr.text.strip())
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                file = open("ManSponsors.txt", "a")
                file.write(str(lvl))
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if count == 16:
                # print('')
                count = 0
                file = open("ManSponsors.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1
    group = "Master"
    for group_no in range(1, 6):
        url = "https://gpro.net/pl/ManSponsors.asp?group={} - {}" \
            .format(group, group_no)
        page = requests.get(url)
        print(url)

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            if 4 <= count <= 8 or count == 15:
                file = open("ManSponsors.txt", "a")
                file.write(tr.text.strip())
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                file = open("ManSponsors.txt", "a")
                file.write(str(lvl))
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if count == 16:
                # print('')
                count = 0
                file = open("ManSponsors.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1
    group = "Elite"
    for group_no in range(1, 2):
        url = "https://gpro.net/pl/ManSponsors.asp?group={} - {}" \
            .format(group, group_no)
        page = requests.get(url)
        print(url)

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            if 4 <= count <= 8 or count == 15:
                file = open("ManSponsors.txt", "a")
                file.write(tr.text.strip())
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                file = open("ManSponsors.txt", "a")
                file.write(str(lvl))
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if count == 16:
                # print('')
                count = 0
                file = open("ManSponsors.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1


def money_levels():
    group = "Elite"
    group_no = 1
    file_path = pathlib.Path("MoneyLevels.csv")
    try:
        with file_path.open(mode="w") as file:
            file.write("Sezon,Wyścig,Grupa,Nazwisko,Budżet,Poziom samochodu"
                       ",Dopasowanie,Punkty\n")
    except OSError:
        logging.error("Error")
    user = input("User")
    password = input("Pass")
    driver = input("[F] - Firefox, [C] - Chrome")
    if driver == "F":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().
                                   install())
    if driver == "C":
        driver = webdriver.Chrome()
    driver.get("https://gpro.net/pl/Login.asp?Redirect=MoneyLevels.asp")
    driver.find_element_by_name("textLogin").send_keys(user)
    driver.find_element_by_name("textPassword").send_keys(password)
    driver.find_element_by_name("LogonFake").click()
    for group_all in range(1, 262):
        with open('page.html', 'w') as f:
            f.write(driver.page_source)
        p = open('page.html', 'r')
        page = p.read()

        soup = BeautifulSoup(page, "html.parser")
        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                count += 1
                try:
                    with file_path.open(mode="a") as file:
                        file.write(
                            f"{sezon},{wyscig}.{dane},{group} - {group_no},")
                except OSError:
                    logging.error("Error")
            soup.find("tr")
            if count != 1 and count != 4:
                try:
                    with file_path.open(mode="a") as file:
                        file.write(tr.text.strip().replace(".", "").
                                   replace("$", ""))
                except OSError:
                    logging.error("Error")
                if count != 8 and count != 7:
                    try:
                        with file_path.open(mode="a") as file:
                            file.write(",")
                    except OSError:
                        logging.error("Error")
            count += 1
            if count == 9:
                count = 0
                try:
                    with file_path.open(mode="a") as file:
                        file.write("\n")
                except OSError:
                    logging.error("Error")
        group_no += 1
        group_all += 1
        if group_all == 1:
            group = "Master"
            group_no = 1
        if group_all == 6:
            group = "Pro"
            group_no = 1
        if group_all == 31:
            group = "Amateur"
            group_no = 1
        if group_all == 111:
            group = "Rookie"
            group_no = 1
        driver.find_element_by_class_name("next").click()


def analiza():
    user = input("User")
    password = input("Pass")
    driver = webdriver.Chrome()
    driver.get("https://gpro.net/pl/Login.asp?Redirect=RaceAnalysis.asp")
    driver.find_element_by_name("textLogin").send_keys(user)
    driver.find_element_by_name("textPassword").send_keys(password)
    driver.find_element_by_name("LogonFake").click()
    with open('page.html', 'w') as file:
        file.write(driver.page_source)
    p = open('page.html', 'r')
    page = p.read()
    soup = BeautifulSoup(page, "html.parser")
    tds = soup.find_all("td")
    for tr in tds:
        file = open("Analiza.txt", "a")
        soup.find("tr")
        file.write(tr.text.strip())
        file.write('\n')
        file.close()
    file = open("Analiza1.txt", "a")
    file.write(soup.text.strip())
    file.close()


sezon = input("Wpisz nr sezonu")
wyscig = input("Wpisz nr wyscigu")
dane = input("Wpisz moment zapisywania danych [1]"
             " Po rynku\n[2] Po kwalach\n[3] Po resecie"
             "\n[x] inny (wpisz zamiast x)\n:")
konsola = 1
while konsola != "0":
    konsola = input("Wpisz komende\n[1] RichDad\n[2] BestFans\
                    \n[3] Wydatki\n[4] Personel\n[5] MoneyLevels\n"
                    "[6] Sponsorzy menedżerów\n[9] Wszystko bez logowania"
                    "\n[0] Wyjdź\n:")
    if konsola == "1":
        print("uruchamiam funkcje rich")
        rich()
    if konsola == "2":
        print("uruchamiam funkcje bestfans")
        best_cars()
    if konsola == "3":
        print("uruchamiam funkcje wydatki")
        expenses()
    if konsola == "4":
        print("uruchamiam funkcje personel")
        view_staff()
    if konsola == "5":
        print("uruchamiam funkcje moneylevels")
        money_levels()
    if konsola == "6":
        print("uruchamiam funkcje sponsorzymenedzerow")
        man_sponsors()
    if konsola == "7":
        print("uruchamiam funkcje analiza")
        analiza()
    if konsola == "9":
        rich()
        best_cars()
        man_sponsors()
        expenses()
        view_staff()
    else:
        print("Wpisz wlasciwy numer")

print("Koniec programu")
