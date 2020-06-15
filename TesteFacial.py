import cv2

cascade_path = 'haarcascade_frontalface_default.xml'

for i in range(10):
    print(i)
    image_path = 'Maicon' + str(i+1) + '.jpeg'

    clf = cv2.CascadeClassifier(cascade_path)
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = clf.detectMultiScale(gray, 1.3, 10)

    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow('resultado', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

exit(0)
