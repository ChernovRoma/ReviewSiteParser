import requests
import random
from urls import *
from bs4 import BeautifulSoup



def get_request(url):
    user_agents_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    ]
    request = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
    return request


def parse_softwareadvise():
    text = []
    r = get_request(urls["softwareadvice"])
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all("div", class_="product-details")
    for block in data:
        name = block.find("h3").text
        text.append(name)
    return text


def parse_sourceforge():
    text = []
    url = urls["sourceforge"]
    counter = 1
    for _ in range(1,100):
        full_url = url + str(counter)
        # if get_request(full_url).status_code == 404:
        #     break
        r = get_request(full_url)
        soup = BeautifulSoup(r.text, "html.parser")
        data = soup.find_all("div", class_="title-subtitle-wrapper")
        for block in data:
            name = block.find("h3").text
            text.append(name)
        counter += 1
    return text


def parse_trustpilot():
    text = []
    url = urls["trustpilot"]
    counter = 1
    while True:
        full_url = url + str(counter)
        if get_request(full_url).status_code == 404:
            break
        r = get_request(full_url)
        soup = BeautifulSoup(r.text, "html.parser")
        data = soup.find_all("div", class_="styles_businessUnitMain__PuwB7")
        for block in data:
            name = block.find("p").text
            text.append(name)
        counter += 1
    return text

# r = get_request("https://sourceforge.net/software/marketing/?page=999")
# print(get_request("https://sourceforge.net/software/marketing/?page=261").status_code)