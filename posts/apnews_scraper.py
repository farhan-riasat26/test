import requests
from bs4 import BeautifulSoup


# url = "https://apnews.com/entertainment"  # Replace with the URL of the webpage you want to scrape
def external_links(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "Web is not working properly"
        soup = BeautifulSoup(response.text, 'html.parser')

        hrefs = []
        for link in soup.find_all('a', href=True):
            if "article" in link.get('href'):
                hrefs.append(link.get('href'))

        # print(len(hrefs))
        articles = list(set(hrefs))
        return articles
    except requests.exceptions.MissingSchema:
        return "Please provide a valid url with http or https"
    # for i in articles:
    #     # url = "https://apnews.com/entertainment"  # Replace with the URL of the webpage you want to scrape
    #     response = requests.get(i)
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #
    #     hrefs = []
    #     for link in soup.find_all('a', href=True):
    #         if "https://apnews.com" not in link.get('href'):
    #             print(link.get('href'))
