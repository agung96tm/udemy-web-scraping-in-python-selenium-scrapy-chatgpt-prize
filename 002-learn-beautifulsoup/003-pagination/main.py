import requests
from bs4 import BeautifulSoup

base_website = "https://subslikescript.com"
website = f"{base_website}/movies_letter-Z"
result = requests.get(website)
soup = BeautifulSoup(result.text, "lxml")

pagination = soup.find("ul", class_="pagination")
pages = soup.find_all("li", class_="page-item")
last_page = pages[-2].text

links = []
for page in list(range(1, int(last_page) + 1))[:2]:
    result = requests.get(f"{website}?page={page}")
    soup = BeautifulSoup(result.text, "lxml")

    box = soup.find("article", class_="main-article")
    for link in box.find_all("a", href=True):
        links.append(link["href"])

for link in links:
    try:
        website = f"{base_website}/{link}"
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, "lxml")

        box = soup.find("article", class_="main-article")

        title = box.find("h1").get_text()
        transcript = box.find("div", class_="full-script").get_text(strip=True, separator=" ")

        with open(f"{title}.txt", "w") as file:
          file.write(transcript)

    except Exception as e:
        print("--- Link not working ---")
        print(link)
