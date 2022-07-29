import cv2
import uuid
import os
import time


labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
number_imgs = 15
IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')
os.makedirs(IMAGES_PATH, exist_ok=True)
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    os.makedirs(path, exist_ok=True)

for label in labels:
    cap = cv2.VideoCapture("0") #your webcam
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

print ('ok')
   