import string
import time
import speech_recognition as sr
import random
import pafy
import vlc
from datetime import datetime, timedelta
from googlesearch import search
def recognise():
        r = sr.Recognizer()                
        with sr.Microphone() as source:     
            print("Speak Anything :")
            audio = r.listen(source)        
            try:
                text = r.recognize_google(audio)    
                return(format(text))
            except:
                print("Sorry could not recognize your voice") 
def randomm():
    r=random.choice(string.ascii_letters)
    print(r)
    return(r)
    
def first_char(st):
    li=list(st.split())
    first_char=li[0][0]
    return(first_char)

def last_char(st):
    li=list(st.split())
    last_element=li[len(li)-1]
    last_char=last_element[len(last_element)-1]
    return(last_char)

def play_song(song):   
   
        query=song+('song')
        for url in search(query, tld="com", num=1, stop=1, pause=2): 
            video = pafy.new(url)
            best = video.getbest()
            playurl = best.url
            Instance = vlc.Instance()                
            player = Instance.media_player_new()
            Media = Instance.media_new(playurl)

            Media.get_mrl()
            player.set_media(Media)
            player.play()
            time.sleep(20)
            player.stop()        
            
def song_last_ch(last):

        li1=list(last.split())
        last_element1=li1[len(li1)-1]
        song_last_char=last_element1[len(last_element1)-1]    
        
        return(song_last_char)

if __name__ == "__main__":
    i=3
    songs_sung=[]
    randomn=randomm()
    st=recognise()
    while i>2:
       
        if first_char(st)==randomn:            
            i=i-1            
            li=("Aankh Marey","Coca Cola","Apna Time Aayega","Swag Se Swagat","Gali Gali","Tere Bin","Kamariya","Dil Diyaan Gallan","Bom Diggy Diggy","Mile Ho Tum","Dilbar","Chamma Chamma","Dil Chori","Proper Patola","Tareefan","High Rated Gabru","Zingaat","Tere Naal Nachna","Cheez badi","Dekhte Dekhte","Badri KI Dulhania","Mungda","Daaru Wargi","Mere Gully Main","Khalibali","Dil Meri Na Sune","Galti Se mistake","Kala Chashma","Heeriye","Nashe Si Chadh Gayi","Laila Main Laila","Husn Parcham","Milegi Milegi","Main Tera Boyfriend","Patola","Paniyo Sa","Chogada","Morni Banke","Ek Ladki Ko Dekha Toh Aisa Lga","Mere Naam Tu","Chhote Chhote Peg","Ding Dang","Ghoomar","Pallo Latke","Aao Kabhi Haveli Pe","Cham Cham","Issaqbaazi","Tera Yaar Hoon Main","The Humma Song","Bhare Bazaar","Poster Lagwa Do","Dholida","Mantoiyat","Doori","Maine Tujhko Dekha","The Breakup Song","Bole Chudiyan","Zaalima","Prem Ratan Dhan Paayo","Gerua","Mere Rashke Qamar","Mera Intkam Dekhegi","Nazam Nazam","Ban Ja Rani","Namo Namo","Baarish","Pal","This Party Is Over Now","Kar Gayi Chull","Dilbaro","Sanam Re","Ae Dil Hai Mushkil","Ek Do Teen Song","Sanu Ek Pal Chain","Tera Hua","Akh Lad jaaye","Nachange Saari Raat","Pehli Baar","Chittiyaan Kalaiyaan","Hua Hain Aaj Pehli Baar","BIllionaire","Qaafirana","Sweetheart","Bulleya","Musafir","Aashiq Bnaya Aapne","Tu Hi Re","Dekha Hai Pehli Baar","Kar Har Maidaan Fateh","Humsafar","Rangtaari","Tera Fitoor","Jaan Nisaar","Deewani Mastani","Chalti Hai Kya 9 Se 12","O Saathi","Udi Udi Jaaye","Tum Mere Ho","Binte Dil","Kamariya","Suit Suit","Tu Hi Hai","Gud Naal Ishq Mitha","Naino ne Bandhi","Oonchi Hai Building","Hatt ja Tau","Chhod Diya","Nasha","Maiya Yashoda","Chitthi Aai Hai","Sweety Tera Drama")
            match = [idx for idx in li if idx.lower().startswith(last_char(st).lower())]

            for i in range(len(match)):
                if match[i] not in songs_sung:
                    print(match[i])
                    songs_sung.append(match[i])
                    play_song(match[i])
            

                    print('start song with: '+song_last_ch(match[i]))
                    break
                else:
                    continue
        
        else:
            i=i-1
            print('not correct')

#          else:
#             while True:
#                 print('wrong song, sing again')

#                 if first_char()==randomm():
#                     break
#                 else:
#                     continue
        
