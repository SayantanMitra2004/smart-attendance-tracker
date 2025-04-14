import cv2
import face_recognition
import pickle
import os


def encodeGenerator():

    #import user images as list
    print(os.listdir("."))
    folderPath = os.path.abspath("uploads")
    pathList = os.listdir(folderPath)
    imgList = []
    studentIds = []
    for path in pathList:
        imgList.append(cv2.imread(os.path.join(folderPath,path)))

        studentIds.append(os.path.splitext(path)[0])




    # funtion for encoding
    def findEncodings(imagesList):
        encodeList = []
        for img in imagesList:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList




    #calling encoding funtion
    print("Encoding started..")
    encodeListKnown = findEncodings(imgList)
    encodeListKnownWithIds = [encodeListKnown, studentIds]
    print("Encoding Complete...")



    #saving encoding into a achar file
    file = open("Encodefile.p", 'wb')
    pickle.dump(encodeListKnownWithIds, file)
    file.close()
    print("File saved...")


def removeEncoding(student_id):
    file_path = "Encodefile.p"

    if not os.path.exists(file_path):
        print("Encoded file not found!")
        return False

    with open(file_path, 'rb') as file:
        encodeListKnownWithIds = pickle.load(file)

    encodeListKnown, studentIds = encodeListKnownWithIds

    if student_id in studentIds:
        index = studentIds.index(student_id)
        del studentIds[index]
        del encodeListKnown[index]

        # Save the updated encoding file
        with open(file_path, 'wb') as file:
            pickle.dump([encodeListKnown, studentIds], file)

        print(f"Successfully removed {student_id} from encoded file.")
        return True

    else:
        print(f"Student ID {student_id} not found in encoded file.")
        return False
