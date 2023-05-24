import requests
import bs4
import lxml
import json


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_count(URL):
    result = requests.get(URL)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    # print(soup)
    citations = soup.find_all("a",title = "Wikipedia:Citation needed")
    return len(citations)

print(get_citations_needed_count(URL))

def get_citations_needed_report(URL):
    result = requests.get(URL)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    report = ""
    for citation in citations:
        passage = citation.find_parent('p').text
        report += passage + '\n'
        # report.append(passage)
    return report

print(get_citations_needed_report(URL))
