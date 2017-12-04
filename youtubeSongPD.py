import urllib.request
from bs4 import BeautifulSoup
from googleSearch import searchInBrowser
from selenium import driver


def play(str):
    textToSearch = str
    query = urllib.request.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,'html.parser')
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        link1 = 'https://www.youtube.com' + vid['href']
        linkD = 'https://www.ssyoutube.com' + vid['href']
        break
    searchInBrowser(link1)
    ask_dwnld = input("Should I download the song?")
    if "yes" in ask_dwnld.lower():
        download(linkD)


def download(str):
    searchInBrowser(str)
    driver.find_element_by_css_selector('.link.link-download.subname ga_track_events.download-icon').click()
    print("The Downloading is started! Sir")