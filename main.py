import cv2
import numpy as np
import utils

paht = "video/"
filename = "Coin2.mp4"

# cap = cv2.VideoCapture(paht+filename)
cap = cv2.VideoCapture(0)

# setting video writer
# fourcc = cv2.VideoWriter_fourcc(*'MP42')
# out = cv2.VideoWriter('output.mp4', fourcc, 20, (600,600))

while cap.isOpened():
    chk, frame = cap.read()
    if chk:
        # resize
        frame = cv2.resize(frame, (600, 600))
        
        # get contours
        con = utils.getContours(frame)

        # count coin
        utils.count_coin(frame,con)
        
        # write video
        # out.write(frame)
        cv2.imshow('Output', frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
# out.release()
cv2.destroyAllWindows()