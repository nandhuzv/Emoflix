from tkinter import *   
#from tkinter.ttk import *
from PIL import ImageTk, Image
import cv2
from cv2 import LINE_4
from deepface import DeepFace
import webbrowser
import time

def emod():
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot Open Webcam")

    start_time = time.time()  # Start time for emotion analysis

    while True:
        ret, frame = cap.read()
        result = DeepFace.analyze(frame, actions=['emotion'])

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_PLAIN

        cv2.putText(frame, result[0]['dominant_emotion'], (x - 5, y - 10), font, 1, (0, 255, 0), 2, cv2.LINE_4)
        cv2.imshow('Demo Video', frame)

        elapsed_time = time.time() - start_time  # Elapsed time since emotion analysis started

        if elapsed_time >= 5:  # Check if 5 seconds have elapsed
            if result[0]['dominant_emotion'] == 'neutral':
                webbrowser.open('https://www.google.com/')
                break

            if result[0]['dominant_emotion'] == 'happy':
                webbrowser.open('https://www.google.com/')
                break

            if result[0]['dominant_emotion'] == 'sad':
                webbrowser.open('https://www.google.com/')
                break

            if result[0]['dominant_emotion'] == 'angry':
                webbrowser.open('https://www.google.com/')
                break

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# create a tkinter window
root = Tk()  

# Give title to your GUI app
root.title("Emoflix")
 
# Open window having dimension 1280x720
root.geometry('1280x720')

#set window color
root['bg'] = '#272E2E'

# Creating a photoimage object to use image
photo = PhotoImage(file = r"E:\Emoflix\Untitled-4.png")


# Create a Button
btn = Button(root, text = 'Click Me !', image = photo, borderwidth=0, bg='#272E2E', command = emod)

# Set the position of button on the top of window.  
btn.pack()   
btn.place(x=480, y=300)

#Create a canvas
canvas= Canvas(root, width= 300, height= 205)

canvas['bg'] = '#272E2E'
canvas.pack()
canvas.place(x=480, y=80)

#Load an image in the script
img= (Image.open("emoflix_logo.jpg"))

#Resize the Image using resize method
resized_image= img.resize((300,205), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)

root.mainloop()
