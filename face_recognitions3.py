import cv2
import time

def recognizer():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('D://Created Programs/Face_Detection/trainer/trainer.yml')
    cascadePath = "D:\Created Programs\Face_Detection\.venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
    # faceCascade = cv2.CascadeClassifier(cascadePath)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Initiate id counter
    id = 0
    # Names related to ids: example ==> Marcelo: id=1, etc
    names = ['None', 'Aegon']
    # Initialize and start real-time video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # Set video width
    cam.set(4, 480)  # Set video height
    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    start_time = time.time()
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)  # Flip vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # If confidence is less than 70 ==> "0": perfect match
            if confidence < 70:
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(
                img,
                str(id),
                (x + 5, y - 5),
                font,
                1,
                (255, 255, 255),
                2
            )
            cv2.putText(
                img,
                str(confidence),
                (x + 5, y + h - 5),
                font,
                1,
                (255, 255, 0),
                1
            )

        elapsed_time = time.time() - start_time
        if elapsed_time >= 2:
            break

    cam.release()
    cv2.destroyAllWindows()

    if id == 'Aegon':
        return True
    elif id == 0:
        return False
