from bs4 import BeautifulSoup
import requests

class Scrap:
    def scrapRepo(user):
        page = requests.get(f"https://github.com/{user}?tab=stars").text

        data = {}
        counter = 1

        soup = BeautifulSoup(page, "lxml")
        listOfRepo = soup.find("turbo-frame", id="user-starred-repos")
        insideListOfRepo = listOfRepo.find("div", class_="col-lg-12")
        repos = insideListOfRepo.find_all("div", class_="col-12 d-block width-full py-4 border-bottom color-border-muted")
        for repo in repos:
            # Scraping Title
            titleTag = repo.find("h3")
            title = titleTag.find("a").text.strip().replace(" ", "").replace("/"," ").split(" ")[1]

            # Scraping Description
            if repo.find("p", class_="d-inline-block col-9 color-fg-muted pr-4") == None:
                description = "No Description"
            else:
                description = description = repo.find("p", class_="d-inline-block col-9 color-fg-muted pr-4").text.strip()
            
            # Scraping Link of Repos
            linkOfRepo = titleTag.find("a")["href"]

            # Adding all the scraped data to Data Dictionary
            data.update({counter : {
                "repo-title":title, 
                "repo-desc":description,
                "repo-link":"https://github.com"+linkOfRepo
            }})
            counter += 1

        return data