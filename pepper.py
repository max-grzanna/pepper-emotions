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

    class Pepper:
        tablet = None
        textToSpeech = None
        ba_service = None
        motion_service = None

        def __init__(self):
            self.textToSpeech = session.service("ALTextToSpeech")
            self.tablet = session.service("ALTabletService")
            # Basic Awareness dient zum Fokussieren
            self.ba_service = session.service("ALBasicAwareness")
            self.motion_service = session.service("ALMotion")


        def activateUser(self):
            self.textToSpeech.say("Stelle dich vor mich, und schaue mich an.")
            time.sleep(3)
            self.tablet.showWebview(
                "https://www.tagesspiegel.de/images/heprodimagesfotos8412019062210wi6_359_1_20190621150050946-jpg/24481576/3-format43.jpg")

        def start(self):
            self.textToSpeech.say("Starte")
            ba_service.setEnabled(True)
            motion_service.wakeUp()


    class Movie:
        def __init__(self, titel="", link="", emotion=""):
            self.titel = titel
            self.link = link
            self.emotion = emotion

    harryPotter = Movie("Harry Potter", "https://www.google.com")
    rushHour = Movie("Rush Hour", "https://www.google.com")
    titanic = Movie("Titanic", "https://www.google.com")

    #Objekte
    movieList.append(harryPotter)
    movieList.append(rushHour)
    movieList.append(titanic)

    Pepper = Pepper()
    Pepper.activateUser()




'''
    motion_service.wakeUp()
    tts.say("Starte")
    ba_service.setEnabled(True)
    tts.say("Schaue mich an und zeige mir anhand deiner Emotion wie du diesen Film findest?")
    time.sleep(3)
    tablet.showWebview(
        "https://www.tagesspiegel.de/images/heprodimagesfotos8412019062210wi6_359_1_20190621150050946-jpg/24481576/3-format43.jpg")

    moodService.subscribe("Tutorial_RecordMood", "Active")
    # The preloading of all ALMood extractors may take up to 2 secondes:
    time.sleep(3)

    # The robot tries to provocate an emotion by greeting you

    # The robot will try to analysis your reaction during the next 3 seconds
    print moodService.getEmotionalReaction()

    moodService.unsubscribe("Tutorial_RecordMood")
    tts.say("Okay danke!")
    tts.say(("Deine Reaktion ist" + moodService.getEmotionalReaction()))
    ba_service.setEnabled(False)

    # motion_service.rest()
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="10.27.1.105",
                        help="Robot IP address. On robot or Local Naoqi: use '10.27.1.105'.")
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
