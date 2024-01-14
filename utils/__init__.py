import cv2
import numpy as np

kernel = np.ones((3,3))

def getContours(frame):
    video_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    video_blure = cv2.GaussianBlur(video_gray, (5,5), 1)
    video_canny = cv2.Canny(video_blure, 20,100)
    video_dilate = cv2.dilate(video_canny, kernel, iterations=1)
    video_eros = cv2.erode(video_dilate, kernel, iterations=1)
    # close = cv2.morphologyEx(video_eros, cv2.MORPH_CLOSE, kernel, iterations=3)

    con, hiera = cv2.findContours(video_eros, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return con

def count_coin(frame, con):
    count = 0
    _10_bath = 0
    _5_bath = 0
    _2_bath = 0
    _1_bath = 0
    _50satang_bath = 0
    _25satang_bath = 0
    total = 0

    for cnt in con:
        area = cv2.contourArea(cnt)         
        if area >= 2000 and area < 6000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            circle = True if len(approx) == 8 else False
            if circle:
                cv2.drawContours(frame, cnt, -1, (0, 255, 0), 2)
                count += 1
                if area >= 5200 and area <= 5900:
                    _10_bath += 1
                elif area >= 4400 and area <= 5199:
                    _5_bath += 1
                elif area >= 3100 and area <= 3399:
                    _1_bath += 1
                elif area >= 2500 and area <= 3099:
                    _50satang_bath += 1
                elif area >= 2000 and area <= 2499:
                    _25satang_bath += 1
                total = _10_bath *10 + _5_bath*5 + _1_bath + _50satang_bath*0.5 + _25satang_bath*0.25
                print(len(approx),area)

    cv2.putText(frame, f'{count} coin', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(frame, f'10 Bath: {_10_bath} coin', (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(frame, f'5 Bath: {_5_bath} coin', (30, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(frame, f'2 Bath: {_2_bath} coin', (30, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(frame, f'1 Bath: {_1_bath} coin', (30, 210), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(frame, f'0.5 Bath: {_50satang_bath} coin', (30, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(frame, f'0.25 Bath: {_25satang_bath} coin', (30, 290), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(frame, f'total : {total} Bath', (30, 330), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
