from bs4 import BeautifulSoup as Soup

def create_response_dict(html):
    soup = Soup(html)
    results_list = soup.find("ul", {'id': "search-results"})
    list_results = results_list.findChildren("li", recursive=False)

    for result in list_results: 
        result_decendants = list(result.descendants)
        # result_decendants = [result.name for result in result_decendants if type(result) == bs4.element.Tag]
        f = result.find('img')
        print(f)
        # print(result_decendants)
        # for i in result_decendants:
        #     print (type(i))
        

