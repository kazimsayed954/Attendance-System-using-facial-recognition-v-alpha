# Import OpenCV2 for image processing

import cv2
import os
import csv
from tkinter import *
import tkinter.messagebox


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
def exit():
    root.destroy()

def dataset_cap():
    Id=t1.get()
    Id=int(Id)
    name=t2.get()
    name=str(name)
    row = [Id, name]
    with open('StudentDetails.csv', 'a+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()

    #name = input('enter your name')
    # Start capturing video
    # vid_cam = cv2.VideoCapture("faceDetection.mp4")
    # vid_cam = cv2.VideoCapture(0)
    vid_cam = cv2.VideoCapture("faceDetection.mp4")
    # Detect object in video stream using Haarcascade Frontal Face
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Initialize sample face image
    count = 0

    assure_path_exists("dataset/")

    # Start looping
    while (True):

        # Capture video frame
        _, image_frame = vid_cam.read()

        # Convert frame to grayscale
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

        # Detect frames of different sizes, list of faces rectangles
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        # Loops for each faces
        for (x, y, w, h) in faces:
            # Crop the image frame into rectangle
            cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Increment sample face image
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/Student." + str(Id) + '.' + str(name) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

            # Display the video frame, with bounded rectangle on the person's face
            cv2.imshow('frame', image_frame)

        # To stop taking video, press 'q' for at least 100ms
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

        # If image taken reach 100, stop taking video
        elif count >= 30:
            print("Successfully Captured")
            Label(root, text="Successfully Captured", fg="black",bg="orange", font='times 20').place(x=180, y=280)
            break

    # Stop video
    vid_cam.release()

    # Close all started windows
    cv2.destroyAllWindows()



root = Tk()

root.geometry('600x400')
root.configure(background="orange")

root.title('Dataset Capture')

number1 = StringVar()
number2 = StringVar()



labelResult = Label(root)

labelResult.grid(row=7, column=2)
l1 = Label(root, text="  ID :", font='times 15', fg='black', bg='orange')
l2 = Label(root, text="  Name :", font='times 15', fg='black', bg='orange')
t1 = Entry(root, bg='grey', fg='white', font='times 15')
t2 = Entry(root, bg='grey', fg='white', font='times 15')
t1.place(x=200, y=40)
t2.place(x=200, y=75)
l1.place(x=70,y=40)
l2.place(x=70,y=75)
bexit=Button(root, text="Exit", font=('times new roman', 20), bg="black", fg="white", command=exit)
bcap = Button(root, text="capture",font=('times new roman', 20),bg="black",fg="white",command=dataset_cap)
bcap.place(x=160 ,y=180)
bexit.place(x=360,y=180)
root.mainloop()