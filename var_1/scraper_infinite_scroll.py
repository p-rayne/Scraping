from requests import Session
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv


headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
base_url = "https://scrapingclub.com/exercise/list_infinite_scroll/"


def get_data(base_url):
    s = Session()
    s.headers.update(headers)

    count = 1
    pagination = 1
    while True:
        if count > 1:
            url = base_url + "?page=" + str(count)
        else:
            url = base_url

        response = s.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        if count == 1:
            pagination = int(
                soup.find("ul", class_="pagination invisible")
                .find_all("li", class_="page-item")[-2]
                .text
            )

        cards = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

        for card in cards:
            name = card.find("h4", class_="card-title").text.strip()
            price = card.find("h5").text.strip()
            img_url = "https://scrapingclub.com" + card.find(
                "img", class_="card-img-top img-fluid"
            ).get("src")
            with open("var_1/products.csv", "a", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow((name, price, img_url))

        sleep(randint(1, 5))
        if count == pagination:
            break
        else:
            count += 1


def main():
    with open("var_1/products.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("Имя", "Цена", "Фото"))

    get_data(base_url)


if __name__ == "__main__":
    main()
