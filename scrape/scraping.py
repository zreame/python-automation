import requests
from bs4 import BeautifulSoup

start_url = "http://quotes.toscrape.com"
f = open("quotes.txt", "w")

def scrapies(url, count) :

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    tags = soup.find_all("div", class_ = "tags")

    # print(max(len(quotes),len(author)))
    for i in range(len(quotes)) :
        count += 1
        f.write(str(count))
        f.write(f". Quote: {quotes[i].text}\n")
        f.write(f"Author: {authors[i].text}\n")

        quoteTags = tags[i].find_all("a", class_ = "tag")
        if len(quoteTags) > 0 :
            f.write("Tags: ")
            for i in range(len(quoteTags)- 1) :
                f.write(f"{quoteTags[i].text}, ")
            f.write(f"{quoteTags[-1].text}")
            f.write("\n\n")
        else :
            f.write("\n")
    
    next = soup.find("li", class_="next")
    try :
        urlappend = next.find("a")["href"]
        url = start_url + urlappend
        scrapies(url, count)
    except :
        f.write(f"The end, total {count} quotes scraped.")
        f.close()
        print("completed")

scrapies(start_url, 0)



