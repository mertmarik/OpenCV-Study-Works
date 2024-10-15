import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    edges = cv2.Canny(frame, 100, 110)
    cv2.imshow("Kenar", edges)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cap.destroyAllWindows()