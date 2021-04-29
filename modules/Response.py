import requests
import os

def develope(chat_id,text):
    send_message(chat_id,"Please wait your files are generating....")
    os.system('python animation_segment_1.py "' + text +'"')
    send_message(chat_id,"Data has been extracted from the text.")

    #### code to automate rendering
    send_message(chat_id,"Your Video is queued for manual rendering...........\n(Automatic rendering is not available.)")
    x = input("Please Render manually!")
    #### code to automate rendering

    send_message(chat_id,"Rendering completed.\n Your video is generating.....")
    os.system("python PostProcesing.py")
    #### code to generate voice
    #### code to generate voice

    #### code to merge sound and video
    #### code to merge sound and video

    if "Out.mp4" in os.listdir("Final/"):
        return True
    else:
        return False

def send_message(chat_id,message):
    Baseurl = "https://api.telegram.org/bot1628016853:AAEyFvb-PmsbUEp4kcAveWtPiFjn_I6wvKE/sendMessage"
    Baseheader = {
        "chat_id":str(chat_id),
        'text':message
    }
    response = requests.get(Baseurl,params=Baseheader)

def send_file(chat_id):
    Baseurl = "https://api.telegram.org/bot1628016853:AAEyFvb-PmsbUEp4kcAveWtPiFjn_I6wvKE/"
    Baseheader = {
        "chat_id":str(chat_id)
    }
    response = requests.get(Baseurl+'sendVideo',params=Baseheader,files={"video":open("Final/Out.mp4",'rb')})
    if response.status_code == 200:
        return True
    else:
        return False
