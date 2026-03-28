''' Zad 1.1
cv2.imwrite("slike/gray_photo.jpg", gray)
'''

####

''' Zad 1.2
cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), thickness=2)
cv2.circle(img,    (400, 200), 50,          (255, 0, 0), thickness=3)
cv2.line(img,      (0, 0),     (500, 500),  (0, 0, 255), thickness=2)
cv2.putText(img, "Hello!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 255), 2)
'''



### 
''' Zad plava loptica
cv2.createTrackbar("H Min", "Mask",  90, 179, do_nothing) 
cv2.createTrackbar("H Max", "Mask", 130, 179, do_nothing) 
cv2.createTrackbar("S Min", "Mask", 100, 255, do_nothing)  
cv2.createTrackbar("S Max", "Mask", 255, 255, do_nothing)  
cv2.createTrackbar("V Min", "Mask",  50, 255, do_nothing)  
cv2.createTrackbar("V Max", "Mask", 255, 255, do_nothing) 
'''

''' Zad teziste
M = cv2.moments(biggest)
if M["m00"] != 0:
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)  # red center dot
    cv2.putText(frame, f"x: {cx}, y: {cy}, A: {M["m00"]}", (cx + 15, cy - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 255, 255), 2)
'''
