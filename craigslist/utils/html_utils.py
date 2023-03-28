from bs4 import BeautifulSoup as Soup
import os

data_dict = {}
data_dict['data'] = {}
data = data_dict['data']

insufficient_data_count = 0

def create_response_dict(html):
    search_results = _get_search_results(html)
    for i in range(len(search_results)):
        # Create result entry for dictionary        
        this_key = f'result_{i}'    
        data[this_key] = {}
        result = data[this_key]
        try:
            # Parsing soup tag
            result_tag = search_results[i].div
            
            result['title'] = result_tag.find(name='a', class_='titlestring').text
            result['link'] = result_tag.find(name='a', class_='titlestring')['href']
            result['price'] = result_tag.find(name='span', class_='priceinfo').text
            # TODO need to clean up image fetch, add more available data
            # result['image'] = result_tag.img['src']
        except:
            del data[this_key]
            global insufficient_data_count
            insufficient_data_count += 1
            continue

    data_dict['count'] = len(data)
    data_dict['results_found'] = bool(len(data))
    data_dict['incomplete_results'] = insufficient_data_count
    insufficient_data_count = 0
    return data_dict

def _get_search_results(html):
    soup = Soup(html)
    return soup.find_all(name='li', class_='cl-search-result')
