import os
import cv2
import face_recognition
import pickle

def encodegenerator():

    # Importing student images
    folderModePath = 'images'
    pathList = os.listdir(folderModePath)
    imgList = []
    studentIds = []
    for path in pathList:
        imgList.append(cv2.imread(os.path.join(folderModePath, path)))
        studentIds.append(os.path.splitext(path)[0])
    print(studentIds)

    def findEncodings(imagesList):
        encodeList = []
        for img in imagesList:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)

        return encodeList

    print("Encoding Started ....")
    encodeListKnown = findEncodings(imgList)
    encodeListKnownWithIds = [encodeListKnown, studentIds]
    print(encodeListKnownWithIds)
    print("Encoding Complete")


    # Load the encoding file
    file = open('FaceEncodeFile.p', 'wb')
    pickle.dump(encodeListKnownWithIds, file)
    file.close()
    print("Encoding File Saved")

encodegenerator()