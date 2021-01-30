import speech_recognition as sr
import pyttsx3
import time

from gtts import gTTS #google text to Speech
import os
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        wake=" English  or malayalam"
        language='ml'
        output=gTTS(text=wake,lang=language,slow=False)
        output.save("output.mp3")
        os.system("start output.mp3") 
      
        time.sleep(3) #adding a delay
        print("say")
        audio = r.listen(source) 
        
        print("You have said \n" + r.recognize_google(audio))   
        num=(r.recognize_google(audio)) 
        if(num=="Malayalam"):
            oo="PNR number parayukaa"
            language='ml'
            output=gTTS(text=oo,lang=language,slow=False)             
            output.save("output.mp3")
            print(output)
            os.system("start output.mp3")
            language='ml'
            time.sleep(3) #adding a delay
            print("say") 
            audio = r.listen(source)                         
            print("Recognizing Now ... ")
            # recognize speech using google
            try:
                language='ml'
                print("You have said \n" + r.recognize_google(audio,language="ml-IN"))
                xxx=r.recognize_google(audio,language="ml-IN")         
                numb=xxx.replace(" ","")   
                numb=int(numb)         
                print(numb)   
                if numb == 12345:
                    xx="Rajadhani Express"
                    language='ml'
                    output=gTTS(text=xx,lang=language,slow=False)
                    output.save("output.mp3")
                    
                    os.system("start output.mp3")                
                else:
                    oo="Try Again"
                    language='ml'
                    output=gTTS(text=oo,lang=language,slow=False)             
                    output.save("output.mp3")
                    print(output)
                    os.system("start output.mp3")          
                                                                                           
            except Exception as e:
                print("Error :  " + str(e)) 
                        
        else:
            oo="Say your PNR Number"
            language='en'
            output=gTTS(text=oo,lang=language,slow=False)             
            output.save("output.mp3")
            print(output)
            os.system("start output.mp3")
            language='ml'
            time.sleep(3) #adding a delay
            print("say") 
            audio = r.listen(source)                         
            print("Recognizing Now ... ")
            # recognize speech using google
            try:
                language='ml'
                print("You have said \n" + r.recognize_google(audio))
                xox=r.recognize_google(audio)         
                numba=xox.replace(" ","")   
                numba=int(numba)         
                print(numba)   
                if numba == 12345:
                    xx="Rajadhani Express"
                    language='en'
                    output=gTTS(text=xx,lang=language,slow=False)
                    output.save("output.mp3")
                    
                    os.system("start output.mp3")                
                else:
                    oo="Try Again"
                    language='ml'
                    output=gTTS(text=oo,lang=language,slow=False)             
                    output.save("output.mp3")
                    print(output)
                    os.system("start output.mp3")          
                                                                                           
            except Exception as e:
                print("Error :  " + str(e))                 
            
if __name__ == "__main__":
    main()