import cv2

cap = cv2.VideoCapture(0)

while True:   #execute camera multiple times
    ret, frame = cap.read()    #ret check if it is true/false  and frame capture actual image
    if not ret:
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC is pressed while OpenCV window is active → exit loop
        break

cap.release()  #Releases the camera resource
cv2.destroyAllWindows()  #Closes all OpenCV windows
