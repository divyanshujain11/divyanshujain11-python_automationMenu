import os
import pywhatkit as pwk
from twilio.rest import Client
import cv2
import tkinter as tk
import pyttsx3
from cvzone.HandTrackingModule import HandDetector
import random
import time
import boto3

# Function to launch various GUI applications using the os module
def notepad():
    os.system("notepad")
def calculator():
    os.system("calc")
def vsCode():
    os.system("code")
def chrome():
    os.system("start chrome")
def explorer():
    os.system("explorer")

# Function to send a Gmail using pywhatkit
def send_gmail():
    sender_mail = "albelaraja23@gmail.com"
    subject = "this is test mail:\n"
    message = "hello biro:\n"
    receiver_mail = "jaind3010@gmail.com: "
    pwk.send_mail(sender_mail, 'vhfcvgxtvzelzxqs', subject, message, receiver_mail)
    

# Function to send an SMS using Twilio
def send_sms():
    account_sid = "AC534efd897816939a7dedaaca73bbd5f4"
    auth_token = "bdebc42d8f9d6775da1b0eaaa05c4692"
    client = Client(account_sid, auth_token)
    client.messages.create(to="+918107996387", from_="+17693009632", body="hello, we are from team 9")

# Function to send a WhatsApp message using pywhatkit
def send_whatsapp():
    pwk.sendwhatmsg_instantly("+918107996387", "hello, how are you")

# Function to get live location using pygeotools
def get_live_location():
    import json
    from urllib.request import urlopen
    urlopen("http://ipinfo.io/json")
    data = json.load(urlopen("http://ipinfo.io/json"))
    lat = data['loc'].split(',')[0]
    lon = data['loc'].split(',')[1]

    print(lat, lon)
# Function to click a picture using OpenCV
def click_picture():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    if ret:
        cv2.imshow("Captured Image", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    camera.release()
    
 #program to communicte with deaf and dumb people
def deaf_people_help():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  
    engine.setProperty("volume", 1.0)
    cap=cv2.VideoCapture(0)
    model=HandDetector()
    while True:
        status,photo=cap.read()
        cv2.imshow("pic1",photo)
        if cv2.waitKey(10)==13:
            break

        hand=model.findHands(photo,draw=False)
        if hand:
            handPhoto=hand[0]
#       print(handPhoto)
            fingerlist=model.fingersUp(handPhoto)        
            if fingerlist==[0,1,1,1,1]:
                engine.say("namaste")
                engine.runAndWait()
                print("namaste")
                time.sleep(2)
            elif fingerlist==[1,0,0,0,0]:
                engine.say("Good job")
                engine.runAndWait()
                print("Good job")
                time.sleep(2)
            elif fingerlist==[0,1,1,0,0]:
                engine.say("Pleasure meeting with you")
                engine.runAndWait()
                print("Pleasure meeting with you")
                time.sleep(2)
            elif fingerlist==[0,1,1,0,0]:
                engine.say("Perfect")
                engine.runAndWait()
                print("Perfect")
                time.sleep(2)
            elif fingerlist==[1,1,0,0,1]:
                engine.say("I love Vimal Sir")
                engine.runAndWait()
                print("I love Vimal Sir")
                time.sleep(2)
            elif fingerlist==[0,0,0,0,0]:
                engine.say("Sorry")
                engine.runAndWait()
                print("Sorry")
                time.sleep(2)
            elif fingerlist==[0,1,0,0,0]:
                engine.say("Help")
                engine.runAndWait()
                print("Help")
                time.sleep(2)
            else:
                print("dont support")
                time.sleep(2)
        


  
    cv2.destroyAllWindows()
    cap.release()

# Function to launch EC2 instances using Boto3 (requires AWS setup)
def launch_ec2_instance():
    import boto3
    ec2 = boto3.client('ec2')
    ec2.run_instances(ImageId="ami-0ded8326293d3201b",
                  InstanceType="t2.micro",MaxCount=1,
                  MinCount=1)
def launch_s3_bucket():
    s3_client = boto3.client('s3')
    s3_client.create_bucket(
            Bucket="amitgywgifywqgfi7qwgdgsdhf",
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'
            })
def playing_with_pixels():
    image3=cv2.imread("blank.jpg")
    photo1_resized = cv2.resize(image3, (700, 500))
    print(photo1_resized.shape)
#start
    photo1_resized[0:1,:,] = [0]
#road
    photo1_resized[400:500,:,] = [0]
#road white strip
    for x in range(0,700,100):photo1_resized[440:460,x:x+50,]=[255]
#poll
    photo1_resized[250:400,20:22]=[0]
    photo1_resized[250:252,3:40]=[0]
    photo1_resized[247:253,0:6]=[0,0,255]
    photo1_resized[247:253,37:43]=[0,0,255]
#building structure
    photo1_resized[100:400,50:250]=[0,255,255]#BRG
#building window
    for x in range(120,400,60):photo1_resized[x:x+30,65:130]=[36,x+28,237]
    for x in range(120,400,60):photo1_resized[x:x+30,155:230]=[36,x+28,237]

#person
    photo1_resized[390:400,270:271]=[0]
    photo1_resized[390:400,274:275]=[0]

    photo1_resized[389:390,266:278]=[0]

    photo1_resized[380:390,265:266]=[0]
    photo1_resized[380:390,277:278]=[0]

    photo1_resized[385:386,260:265]=[0]
    photo1_resized[385:386,277:282]=[0]

    photo1_resized[379:380,266:278]=[0]

    photo1_resized[373:379,270:271]=[0]
    photo1_resized[373:379,274:275]=[0]

    photo1_resized[372:373,270:274]=[0]

    photo1_resized[375:378,273:274]=[36,28,237]

#poll
    photo1_resized[250:400,300:302]=[0]
    photo1_resized[250:252,280:320]=[0]
    photo1_resized[247:253,277:283]=[0,0,255]
    photo1_resized[247:253,317:323]=[0,0,255]

#glass building
    photo1_resized[150:400,350:600]=[234,217,153]#BRG
    for x in range(370,590,30):
        photo1_resized[150:400,x:x+1]=[0]
    for x in range(180,400,30):
        photo1_resized[x:x+1,350:600]=[0]
#poll
    photo1_resized[250:400,650:652]=[0]
    photo1_resized[250:252,630:670]=[0]
    photo1_resized[247:253,627:633]=[0,0,255]
    photo1_resized[247:253,667:673]=[0,0,255]


    cv2.imshow("divu",photo1_resized)
    cv2.waitKey()
    cv2.destroyAllWindows()


def main():
    global root, result_label

    root = tk.Tk()

    root.title("Menu of Team 9")
    root.minsize(700,300)
    root.configure(bg="#ADD8E6")
    label = tk.Label(root, text="Menu", font= ("blue", 30))
    label.pack()
    
    button_style_1 = {
        "font": ("Helvetica", 10), "width": 15         
    }
    
    button_style_2 = {
       "font": ("Helvetica", 10), "width": 30,         
    }
    
    button_style_3 = {
        "font": ("Helvetica", 10), "width": 30         
    }
    
    button_style_4 = {
        "font": ("Helvetica", 10), "width": 30       
    }
    button_style_5 = {
        "font": ("Helvetica", 10), "width": 30         
    }
    button_style_6 = {
        "font": ("Helvetica", 10), "width": 30        
    } 
    button_style_7 = {
        "font": ("Helvetica", 10), "width": 30         
    } 
    button_style_8 = {
        "font": ("Helvetica", 10), "width": 30         
    }   
    button = tk.Button(root, text="calculator", command=calculator,**button_style_1)
    button.pack(pady=10)
    button = tk.Button(root, text="VS Code", command=vsCode,**button_style_1)
    button.pack(pady=10)
    button = tk.Button(root, text="Explorer", command=explorer,**button_style_1)
    button.pack(pady=10)
    button = tk.Button(root, text="Notepad", command=notepad,**button_style_1)
    button.pack(pady=10)
    button = tk.Button(root, text="Google Chrome", command=chrome,**button_style_1)
    button.pack(pady=10)
    
    button1 = tk.Button(root, text="send mail to jaind3010@gmail.com", command=send_gmail, **button_style_2)
    button1.pack(pady=10)
    
    button2 = tk.Button(root, text="send sms", command=send_sms, **button_style_3)
    button2.pack(pady=10)
    
    button3 = tk.Button(root, text="send whatsapp message", command=send_whatsapp, **button_style_4)
    button3.pack(pady=10)
    button4 = tk.Button(root, text="want live location", command=get_live_location, **button_style_5)
    button4.pack(pady=10)
    button5 = tk.Button(root, text="want to click picture", command=click_picture, **button_style_6)
    button5.pack(pady=10)
    button6 = tk.Button(root, text="want to talk with deaf people", command=deaf_people_help, **button_style_7)
    button6.pack(pady=10)
    button7 = tk.Button(root, text="want to launch ec2 instance", command=launch_ec2_instance, **button_style_8)
    button7.pack(pady=10)
    button8 = tk.Button(root, text="want to launch s3 bucket", command=launch_s3_bucket, **button_style_8)
    button8.pack(pady=10)
    button8 = tk.Button(root, text="play with pixels", command=playing_with_pixels, **button_style_8)
    button8.pack(pady=10)
    


    result_label = tk.Label(root, text="", fg="red")
    result_label.pack()

    root.mainloop()


main()
