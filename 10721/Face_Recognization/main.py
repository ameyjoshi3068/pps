import cv2
import os
import face_recognition

# Load the input image and convert it to grayscale
image = cv2.imread("input.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the face detector and detect faces in the image
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Create an empty list to store the names of the attendees
attendees = []

# Load the known face encodings and names
known_face_encodings = []
known_face_names = []
for file in os.listdir("known_faces"):
    name, extension = file.split(".")
    known_face_names.append(name)
    image = face_recognition.load_image_file("known_faces/" + file)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)

# Iterate over the detected faces
for (x, y, w, h) in faces:
    # Convert the face coordinates to a NumPy array
    face_encoding = face_recognition.face_encodings(image, [(y, x+w, y+h, x)])[0]

    # Compare the face encoding to the known face encodings
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    # If a match is found, append the name of the attendee to the list
    if True in matches:
        index = matches.index(True)
        attendees.append(known_face_names[index])

# Print the list of attendees
print(attendees)
print("Completed")
