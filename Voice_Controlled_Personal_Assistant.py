
import speech_recognition as sr
import feedparser
import playsound
import wikipedia
import pyttsx3

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
mic_name = "Microphone (Realtek High Defini"
sample_rate = 44100  # 48000
chunk_size = 512  # 2048
r = sr.Recognizer()

# generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)

# the following loop aims to set the device ID of the mic that
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i

with sr.Microphone(device_index=device_id, sample_rate=sample_rate, chunk_size=chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Say Something")
    # listens for the user's input
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("you said: "),print(text)
        engine = pyttsx3.init()
        engine.say(str(text))
        engine.setProperty('rate', 120)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()


        if text == "news":

            # Function to fetch the rss feed and return the parsed RSS
            def parseRSS(rss_url):
                return feedparser.parse(rss_url)

                # Function grabs the rss feed headlines (titles) and returns them as a list


            def getHeadlines(rss_url):
                headlines = []

                feed = parseRSS(rss_url)
                for newsitem in feed['items']:
                    headlines.append(newsitem['title'])

                return headlines


            # A list to hold all headlines
            allheadlines = []

            # List of RSS feeds that we will fetch and combine
            newsurls = {
                #'apnews': 'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305',
                'googlenews': 'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',
                
            }

            # Iterate over the feed urls
            for key, url in newsurls.items():
                # Call getHeadlines() and combine the returned headlines with allheadlines
                allheadlines.extend(getHeadlines(url))


            # Iterate over the allheadlines list and print each headline
            for hl in allheadlines:
                print(hl)
            engine = pyttsx3.init()
            engine.say(str(allheadlines))
            engine.setProperty('rate', 120)
            engine.setProperty('volume', 0.9)
            engine.runAndWait()
        elif text == "play song":

            playsound.playsound('C:/Users/ADMIN/Desktop/shree-ganesh-ekadantaya-vakratundaya.mp3', True)
        else:
           a=(wikipedia.summary(str(text), sentences=2))
           print(a)
           engine = pyttsx3.init()
           engine.say(a)
           engine.setProperty('rate', 120)
           engine.setProperty('volume', 0.9)
           engine.runAndWait()


            # error occurs when google could not understand what was said

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio please repeat")
        engine = pyttsx3.init()
        engine.say("Google Speech Recognition could not understand audio please repeat")
        engine.setProperty('rate', 120)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


