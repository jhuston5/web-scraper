import requests
from bs4 import BeautifulSoup

# URL = 'https://testing-www.codefellows.org/courses/code-400/'
URL = 'https://en.wikipedia.org/wiki/European_Union'

def get_citations_needed_count(URL):

    page =requests.get(URL) 
    # print(page.content)
   
    soup = BeautifulSoup(page.content, 'html.parser') 
    # print(soup) 

    results = soup.find(class_="mw-parser-output")
    # print(results.prettify) 

    a_tags = soup.find_all('a') 
    # print(a_tags)
    
    citations = [a for a in a_tags if 'citation needed' in a.text]
    print(citations) 

    citation_count = 0 
    for i in citations: 
        citation_count += 1 
    # print(f"this is citation count: {citation_count}")
    return citation_count 


def get_citations_needed_string(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(class_="mw-parser-output")

    search = results.findAll("p")

    output_text = ''

    a_tags = soup.findAll('a')
    citations = [a for a in a_tags if 'citation needed' in a.text]
    for citation in citations:
        output_text += (citation.find_parent('p').text)
    return output_text

if __name__ == '__main__': 
    
    URL = 'https://en.wikipedia.org/wiki/European_Union' 
    print(get_citations_needed_count(URL)) 
    print(get_citations_needed_string(URL)) 