from bs4 import BeautifulSoup as Soup

def create_response_dict(html):
    soup = Soup(html)
    results_list = soup.find("ul", id="search-results")
    list_results = results_list.findChildren("li", recursive=False)
    print(results_list)
