#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use getEmotionalReaction Method"""

import qi
import argparse
import sys
import time
import webbrowser


def main(session):
    moodService = session.service("ALMood")

    numSuggestions = 1
    movieList = []
    movieDB = []
    rating = 0

    class Pepper:
        tablet = None
        textToSpeech = None
        ba_service = None
        motion_service = None
        moodService = None

        def __init__(self):
            self.textToSpeech = session.service("ALTextToSpeech")
            self.tablet = session.service("ALTabletService")
            # Basic Awareness dient zum Fokussieren
            self.ba_service = session.service("ALBasicAwareness")
            self.motion_service = session.service("ALMotion")
            self.moodService = session.service("ALMood")

        def activateUser(self):
            self.tablet.showWebview(
                "https://i.ibb.co/XDJYQgw/CFED5845-9-ECE-44-FF-B855-1-A6210978-CE7.jpg")
            time.sleep(2)
            self.textToSpeech.say("Stelle dich vor mich, und schaue mich an.")

            time.sleep(3)

        def start(self):
            self.textToSpeech.say("Starte")
            ba_service.setEnabled(True)
            motion_service.wakeUp()

        def say(self, text=""):
            self.textToSpeech.say(text)

        def openURL(self, url="https://127.0.0.1"):
            self.tablet.showWebview(url)

        def getEmotion(self):
            return self.moodService.getEmotionalReaction()

        def focusUser(self):
            self.ba_service.setEnabled(True)

        def unfocusUser(self):
            self.ba_service.setEnabled(False)

    class Movie:
        def __init__(self, titel="", link="", emotion="", rating=0.0):
            self.titel = titel
            self.link = link
            self.emotion = emotion
            self.rating = rating

    # Filmvorschläge  erstellen

    harryPotter = Movie("Harry Potter",
                        "https://www.tagesspiegel.de/images/heprodimagesfotos8412019062210wi6_359_1_20190621150050946-jpg/24481576/3-format43.jpg")
    rushHour = Movie("Rush Hour",
                     "https://i3-img.kabeleins.de/pis/ezone/29e4qgELB38wdEB-ZftIYFPQSp-HxjRVj8ghGONpO6WKv8N5ookTKLFQzHOkL518VwTpbFVddOIjbc3JVo2-7R7fmvTtzGMvFWlVp4gynw/profile:mag-996x562")
    titanic = Movie("Titanic",
                    "https://scontent-frt3-2.xx.fbcdn.net/v/t1.0-9/117357203_3544561898896579_7992014078248731844_n.jpg?_nc_cat=101&ccb=2&_nc_sid=6e5ad9&_nc_ohc=GQf5LgtVedMAX9YlSjZ&_nc_ht=scontent-frt3-2.xx&oh=d49e1eae9ad11a9565aa2ada781bafac&oe=5FE8087B")

    movieList.append(harryPotter)
    movieList.append(rushHour)
    movieList.append(titanic)

    # MovieDb erstellen

    movie1 = Movie("Terminator",
                   "https://images.hdqwalls.com/download/arnold-schwarzenegger-terminator-1280x800.jpg","", 2.0)
    movie2 = Movie("Borat",
                   "https://images.wallpapersden.com/image/download/sacha-baron-cohen-as-borat-sagdiyev_bGdubmaUmZqaraWkpJRmZ21lrW1lZQ.jpg",
                   4.0)
    movie3 = Movie("König der Löwen",
                   "https://s1.1zoom.me/big0/806/313029-Sepik.jpg", "", 1.0)

    # Objekte
    movieDB.append(movie1)
    movieDB.append(movie2)
    movieDB.append(movie3)

    # eigentlicher Programmablauf
    Pepper = Pepper()
    Pepper.activateUser()

    for movie in movieList:
        Pepper.focusUser()

        Pepper.openURL(movie.link)
        time.sleep(1)

        Pepper.say("Folgender Filmvorschlag :" + movie.titel)
        Pepper.say("Skenne deine Emotion")

        emotion = Pepper.getEmotion()
        if emotion == "unknown":
            movie.emotion = "nicht eindeutig"

        if emotion == "positive":
            rating = rating + 4
            movie.emotion = emotion
        if emotion == "neutral":
            rating = rating + 2
            movie.emotion = emotion
        if emotion == "negative":
            rating = rating + 1
            movie.emotion = emotion

        Pepper.say("Erledigt!")
        Pepper.unfocusUser()

    rating = rating / len(movieList)
    print ("erreichtes Rating: " + str(rating))
    Pepper.say("Deine Auswahl ")
    for movie in movieList:
        Pepper.say("Deine Reaktion zum Film " + movie.titel + " ist" + movie.emotion)

    if rating == 0.0:
        Pepper.say("Dein Filmgeschmack ist nichts halbes und nichts ganzes.")
    else:
        for movie in movieDB:
            if movie.rating >= rating:
                Pepper.openURL(movie.link)
                Pepper.say("Der Film " + movie.titel + " könnte dir ebenfalls gefallen.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="10.27.1.101",
                        help="Robot IP address. On robot or Local Naoqi: use '10.27.1.101'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
                                                                                              "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
