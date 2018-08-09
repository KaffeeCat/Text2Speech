# -*- coding: UTF-8 -*-
# ==============================================================
# File name : text2speech.py
# File purpose : Convert text to speech by TTS
# Author : Wang Kang
# Email : prince.love@live.cn
# Date : 2018/8/2
# ==============================================================

import pyttsx 
# PyTTSx
# How to install : 
#   * pip install pyttsx
# Get property
#   * pro_value = engine.getProperty('pro_name')
# Reference :
#   * http://pyttsx.readthedocs.io/en/latest/engine.html#examples

import threading, time

class Text2Speech:

    # ==========================================================================================================
    # Function name : __init__
    # Function purpose : class construction function
    # ==========================================================================================================
    def __init__(self):

        self.last_spoke_finish_time = time.clock()
        pass

    # ==========================================================================================================
    # Function name : say
    # Function purpose : read text by TTS
    # Function input : 
    #       * text : Text to speak
    #       * rate : Integer speech rate in words per minute
    #       * delay : time-delay for next speech in seconds
    # ==========================================================================================================
    def say(self, text, rate=160, delay=0):

        current_time = time.clock()

        if current_time > self.last_spoke_finish_time:

            # create a thread to play sound
            thread_handle = threading.Thread(target=self.__text2speech_callback__, name='__text2speech_callback__', kwargs={'text': text, 'rate': rate})
            thread_handle.start()
            self.last_spoke_finish_time = time.clock() + len(text) + delay

        pass

    # ==========================================================================================================
    # Function name : __text2speech_callback__
    # Function purpose : text2speech callback
    # Function input : 
    #       * text : Text to speak
    #       * rate : Integer speech rate in words per minute
    # ==========================================================================================================
    def __text2speech_callback__(self, text, rate):

        try:
            # create TTS instance
            engine = pyttsx.init()

            # change speech rate
            engine.setProperty('rate', rate) # TTS default is 200

            #print('ready to say %d words ' %(len(text)))

            # use TTS to say
            engine.say(text)
            engine.runAndWait()
            engine.stop()
            
            #print('ready to say next text')

        except RuntimeError, e:
            pass

        pass

# ==========================
# Main function
# ==========================
if __name__ == '__main__':

    text = u'我在另一个线程中不断的说恭喜发财'
    speech_rate = 200
    
    text2speech = Text2Speech()

    while True:

        text2speech.say(text, speech_rate)

    exit()
