# Selenium-Automation
Web Automation through Selenium in python with the help of geckodriver in Firefox

This Repo works on automating tasks using selenium:

### `githubThrough.py`

It provides 2 methods to work on 

1. **incognito(username,password)** - It opens the github.com in incognito mode in firefox, and login in the website using the login credentials passed as an argument by user.
like this - 

```
 	firefox_profile = selenium.webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    driver = selenium.webdriver.Firefox(firefox_profile=firefox_profile)
```

2.**normal_mode()** - It opens the github.com using the login credentials already saved in the browser

### `googleSearch.py`

This python file provides a method **searchInBrowser()**, it takes input a string and then search it in google and the firefox window remains opened.

### `youtubeSongPD.py`

It provides 2 method-API to work on - 

1. **play(str)** , it takes a string and search it on youtube and opens the first video in the search and plays it, it subsequently provides an option to download it.

2. **download(str)** ,it downloads the song playing right now.

Both methods leave the firefox window open and the song keep on playing.

> ``` youtubeSongPD file uses 'https://www.ssyoutube.com' + vid['href'] to download the file ```


>Selenium Automation of Opening browsers and entering credentials.
