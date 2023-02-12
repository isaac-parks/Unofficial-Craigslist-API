from bs4 import BeautifulSoup as Soup
import os

def create_response_dict(html):
    data_dict = {}
    soup = Soup(html)

    result_row = soup.find_all(name='li', class_='cl-search-result')
    # imgs = result_row[0].find_all('img', recursive=True)
    print(result_row)
    # data_dict['data'] = {}
    # data = data_dict['data']
    # for i in range(len(result_row)):
    #     data[f'result{i + 1}'] = {}
    #     result = data[f'result{i + 1}'] 
    #     result['link'] = result_row[i].a['href']

    #     # open('C:\\Users\\Isaac\\Desktop\\new 2.txt', 'w', encoding='utf-8').write(str(imgs))

        
    #     # img = result_row[i].find('img', recursive=True)
    #     # print(img)


    #     result_info = result_row[i].find('div', class_='result-info')
    #     result['title'] = result_info.h3.text.replace('\n', '')
    #     result['price'] = result_info.find('span', class_='result-meta').span.text

        

    # data_dict['count'] = len(data)
    # data_dict['resultsFound'] = bool(len(data))
    return data_dict