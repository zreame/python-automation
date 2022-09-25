import requests
from bs4 import BeautifulSoup

f= open("inventory.txt", "w")

base_url= "https://scrapingclub.com/exercise/list_basic/"
urls= []
response= requests.get(base_url)
soup= BeautifulSoup(response.text, "lxml")

pages = soup.find("ul", class_= "pagination")
links = pages.find_all("a", class_= "page-link")

for link in links :
    url = link["href"] if link.text.isdigit() else None
    if url :
        urls.append(url)

# print(urls)

def scrapies(ind_url, count) :
    full_url = base_url + urls[ind_url]
    response= requests.get(full_url)
    soup= BeautifulSoup(response.text, "lxml")
    
    items= soup.find_all("div", class_= "col-lg-4 col-md-6 mb-4")
    
    for item in items :
        count += 1
        name = item.find("h4").find("a").text
        price = item.find("h5").text
        f.write(f"{count}. {name}: {price}\n")

    ind_url += 1

    if ind_url < len(urls) :
        scrapies(ind_url, count)
    else :
        f.close()
        print("Completed.")

scrapies(0, 0)

