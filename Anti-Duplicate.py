import subprocess, sys  #Needed to open up the window of the text file
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import urllib
import urllib2

#import requests


def oneWord(word, alist):
    #print(word)
    #print(alist)
    neWord = word.lower()
    if neWord in alist:
        #print("hit")
        return "___"
    if neWord not in alist:
        alist.append(neWord)
        return word

def WordCheck(file):
    sum = 0
    with open(file) as f:
        content = f.readlines()
        for x in content:
            #print(x)
            y = (x.split())
            for word in y:
                if (word != "___"):
                    sum += 1
    #print(sum)
    return sum

def percentDiff(part, whole):
    part = float(part)
    whole = float(whole)
    per = 100*(part/whole)
    per = 100.0 - per
    return per

def openWindow(file):
    opener ="open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, file])


def openURL(url, keyword):
    driver = webdriver.Chrome('/Users/Renzzo/Downloads/chromedriver')
    #driver.implicitily_wait(10)
    driver.get(url)
    print driver.title

    inputElement = driver.find_element_by_name("q")

    inputElement.send_keys(keyword)

    inputElement.submit()

    WebDriverWait(driver, 10).until(EC.title_contains(keyword))
    print driver.title
    kword = driver.find_element_by_partial_link_text('All Star')
    kword.click()
    #WebDriverWait(driver, 10).until(EC.title_contains(keyword))
    WebDriverWait(driver, 10000)
    #driver.quit()

def praseLyrics(title, band):
    url = "https://www.azlyrics.com/lyrics/"
    urlEnd = ".html"
    band = band.replace(" ","")
    band = band.lower()
    title = title.replace(" ","")
    title = title.lower()
    print(band)
    print(title)
    newURL = url + band + "/" + title + urlEnd

    #test = 'https://www.azlyrics.com/lyrics/smashmouth/allstar.html'
    page = urllib2.urlopen(newURL)
    soup = BeautifulSoup(page,"html.parser")
    #name_box = soup.find("div", attrs={"class": None})
    name_box = soup.find_all("div")[21].text
    #print name_box

    lyrics = name_box.split("\n")
    return lyrics


    #name = name_box.text.strip()
    #lyrics = name_box.text
    #print name


def scanLyrics(lyrics, opt):
    if (opt == 1):
        ori = open(Orifile, "w+")
        ori.write("-- BEGINNING OF SONG -- \n")
        for line in lyrics:
            #word = line.split()
            ori.write(line)
            ori.write("\n")

        ori.write("-- END OF SONG -- \n")
        ori.close()

            #for value in word:
                #print value
    if (opt == 2):
        new = open(Newfile, "w+")
        new.write("-- BEGINNING OF SONG -- \n")
        for line in lyrics:
            word = line.split()
            for value in word:
                sti = oneWord(value, wordArray)
                new.write(sti)
                new.write(" ")
            new.write("\n")
        new.write("-- END OF SONG -- \n")
        new.close()

def msgToUser(band_name, song_name, per):
    print("The Song chosen was " + song_title)
    print("Sang by " + band_title)
    print("%.1f%% of the Lyrics was repetitive" % per)

    print("Opening Files....")
    time.sleep(3)



#file1 = "All-Star.txt"
#if (file1 == "All-Star.txt"):
    #print("The Song Chosen is All Star by Smash Mouth")
#file2 = "UpdatedSong.txt"
#w = open(file2, "w+")
#with open(file1) as f:
#  content = f.readlines()
 # for x in content:
#    y = (x.split())
#    w.write("\n");
#    for word in y:
#        str = oneWord(word, wordArray)
#        w.write(str)
#        w.write(" ")
        #print(y.split())
        #print(word)
    #print(x)
#w.close()

#sum1 = WordCheck(file1)
#sum2 = WordCheck(file2)
##openWindow(file2)
#openURL("https://www.azlyrics.com/", "All Star")


Orifile = "Original.txt"
Newfile = "ReMIXED.txt"
wordArray = list()

song_title = raw_input("What Song do you want to mixed up?\n")
type(song_title)

band_title = raw_input("What Band sang that sang?\n")
type(band_title)

lyrics = praseLyrics(song_title, band_title)
scanLyrics(lyrics, 1)
scanLyrics(lyrics, 2)

sum1 = WordCheck(Orifile)
sum2 = WordCheck(Newfile)

totalper = percentDiff(sum2, sum1)

msgToUser(band_title,song_title,totalper)

openWindow(Orifile)
openWindow(Newfile)







    #data.append(x.split())
