import cv2
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

root = tk.Tk()
root.title("Face Detection")
root.geometry("400x600")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)
lbl = Label(frame)
lbl.pack()

text_frame = tk.Frame(root)
text_frame.pack(padx=10, pady=10)
text = Label(text_frame, text="Number of people: 0")
text.pack()

exit_button = tk.Button(root, text="Exit",command=root.quit, height=2, width=10)
exit_button.pack(pady=10)


def show_frame():
    ret, frame = cap.read()

    count = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        if faces is not None:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    text.config(text="Number of people: " + str(count))

    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lbl.imgtk = imgtk
    lbl.configure(image=imgtk)
    lbl.after(10, show_frame)

show_frame()
root.mainloop()

cap.release()
