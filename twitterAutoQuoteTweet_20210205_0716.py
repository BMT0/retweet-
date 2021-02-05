import keyboard
import time
import random

# twitter hot keys -> https://venturebeat.com/2014/11/30/how-to-use-twitter-with-keyboard-shortcuts/

"""
1. open twitter in broswer
2. set targeted location. search #HearTheVoiceOfMyanmar
3. run the program
4. select twitter page (windows active)
"""

messageList = ["OUR VOTES MATTER",
               "We're fighting for justice.",
               "The human heart is the first home of democracy ~ TERRY TEMPEST WILLIAMS",
               "What is happening in Myanmar.",
               "Fighting for DEMOCRACY. Keep on going.",
               "Make our collective voice louder.",
               "In a democracy, force should never seek to overrule the will of the people. ~ @JoeBiden "]

print("Please select the twitter page..")
time.sleep(5)
print("Starting retweet now..")
while True:
    keyboard.send('j')  # selecting the next tweet
    time.sleep(1)
    keyboard.send('l')  # like the tweet
    time.sleep(1)
    keyboard.send('t')  # retweet
    time.sleep(1)
    keyboard.send('down')  # select "Quote Tweet"
    time.sleep(1)
    keyboard.send('enter')
    time.sleep(1)
    keyboard.write(random.choice(messageList))  # single line short message
    time.sleep(1)
    keyboard.send('enter')
    keyboard.send('enter')
    time.sleep(1)
    keyboard.write('#HearTheVoiceOfMyanmar ')  # 1st hashtag line follow by "space"
    time.sleep(1)
    keyboard.send('enter')
    time.sleep(1)
    keyboard.write('#RespectOurVotes ')  # 2nd hashtag line follow by "space"
    print("Check if Hashtags are correct..")
    time.sleep(5)
    keyboard.send('ctrl+enter')
    waitForNext = random.randint(15, 30)
    print("Waiting for %d seconds.." % waitForNext)
    time.sleep(waitForNext)
