from web_scraper.scraping import *



def test_get_citation_count(): 
    URL = 'https://en.wikipedia.org/wiki/European_Union' 
    assert get_citations_needed_count(URL) == 3 

def test_get_citation_needed_report(): 
        text = get_citations_needed_string('https://en.wikipedia.org/wiki/European_Union') 
        expected = "It also led directly to the founding of the Council of Europe in 1949, the first great effort to bring the nations of Europe together, initially ten of them. The council focused primarily on values—human rights and democracy—rather than on economic or trade issues, and was always envisaged as a forum where sovereign governments could choose to work together, with no supra-national authority. It raised great hopes of further European integration, and there were fevered debates in the two years that followed as to how this could be achieved.[citation needed]" in text
        assert expected == True
