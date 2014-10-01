import sys
import pyaudio
import wave
import os
import fcntl
import time

def main():
    sound_cues = open('sound_cues').read().splitlines()
    light_cues = open('light_cues').read().splitlines()
    play_names = open('play_names').read().splitlines()
    plays = []

    for idx in range(len(play_names)):
        plays.append( {'name': play_names[idx], 'sound': sound_cues[idx], 'lights': light_cues[idx]} )

    while(True):
        for play in plays:
            print play['name']
        print
        print
        play_num = raw_input("Enter a play number: ")
        play = plays[int(play_num) - 1]
        print
        print play['name']
        print
        print '***************************************************'
        print 'LIGHTS NOTES:'
        print play['lights']
        print
        print '***************************************************'
        print 'SOUND NOTES:'
        print play['sound']
        print
        print '***************************************************'

        audio = "sounds/" + play_num + ".wav"
        if (os.path.isfile(audio)):
            raw_input("Press Enter to start sound...")
            wf = wave.open(audio)
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output=True)

            data = wf.readframes(1024)
            print
            print "Press Command-C to stop audio..."
            print
            try:
                while data != '':
                    stream.write(data)
                    data = wf.readframes(1024)
            except KeyboardInterrupt:
                pass
                print
            stream.stop_stream()
            stream.close()
            p.terminate
        else:
            print "Wait for curtain...(command-c)"
            print
            try:
                while True:
                    pass
            except KeyboardInterrupt:
                pass
                print
            print "NO AUDIO"
            print

        print
        print
        print
        print
        print
        print
        print
        print
        print
        print

if __name__ == "__main__":
    main()

