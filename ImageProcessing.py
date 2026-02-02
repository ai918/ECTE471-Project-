import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Webcam setup
vid = cv2.VideoCapture(0)

# Color detection
def capture_color():
    _, frame = vid.read()
    cv2.imshow("Camera View", frame)

    b = frame[:, :, :1]
    g = frame[:, :, 1:2]
    r = frame[:, :, 2:]

    if np.mean(b) > np.mean(g) and np.mean(b) > np.mean(r):
        return "blue"
    elif np.mean(g) > np.mean(r):
        return "green"
    else:
        return "red"


# Text detection
def detect_text():
    _, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return text.strip()

# Decision logic
def decide_action(color, text):
    if color == "blue":
    #and text == "DXB":
        return "C1_FAST"
    elif color == "blue":
    #and text == "SHJ":
        return "C2_FAST"
    elif color == "green":
    #and text == "DXB":
        return "C1_SLOW"
    elif color == "green":
    #and text == "SHJ":
        return "C2_SLOW"
    elif color == "red":
        return "DROP"
    else:
        return "ROTATE"

# Main execution
print("Press 'q' to capture block")

while True:
    _, frame = vid.read()
    cv2.imshow("Camera View", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        color = capture_color()
        text = detect_text()
        action = decide_action(color, text)

        print("Detected color:", color)
        print("Detected text:", text)
        print("Selected action:", action)
        break

vid.release()
cv2.destroyAllWindows()
