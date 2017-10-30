# project for KOSS ,IIT Kharagpur (used only for educational purpose)

from bs4 import BeautifulSoup
import requests
import sys
import os


def show_lyrics():
    # taking input of artist and track from user
    artist = input("enter the name of the ARTIST : ")
    artist = artist.lower().replace(" ","-")
    track = input("enter the name of the TRACK : ")
    track = track.lower().replace(" ","-")
    # creating url
    url = 'http://www.metrolyrics.com/' + track + '-lyrics-' + artist + '.html'
    # getting contents of the given url
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    # scrapping lyrics from all the contents of the webpage
    lyrics = soup.find_all("p", {"class":"verse"})
    # printing the lyrics after converting
    for i in lyrics:
        print i.text


def main():
    show_lyrics()


if __name__ == "__main__":
    print("initialising")
    main()
