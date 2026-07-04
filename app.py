from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from ultralytics import YOLO
import cv2
import time

from action_controller import perform_action

# -------------------------------
# FastAPI Initialization
# -------------------------------
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# -------------------------------
# Load Trained YOLO Model
# -------------------------------
model = YOLO(r"runs\classify\runs\hand_gesture\weights\best.pt")

# Webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Unable to open webcam")

# -------------------------------
# Cooldown Variables
# -------------------------------
last_action = ""
last_time = 0
cooldown = 1.5      # seconds

# -------------------------------
# Home Page
# -------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# -------------------------------
# Webcam Generator
# -------------------------------
def generate_frames():

    global last_action
    global last_time

    while True:

        success, frame = camera.read()

        if not success:
            break

        # --------------------------
        # YOLO Prediction
        # --------------------------
        results = model(frame, verbose=False)

        result = results[0]

        if result.probs is not None:

            class_id = result.probs.top1

            confidence = float(result.probs.top1conf)

            label = model.names[class_id]

            # ----------------------
            # Draw Prediction
            # ----------------------
            cv2.putText(
                frame,
                f"{label} ({confidence:.2f})",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # ----------------------
            # Perform Action
            # ----------------------
            current_time = time.time()

            if confidence > 0.80:

                if (
                    label != last_action
                    or current_time - last_time > cooldown
                ):

                    perform_action(label)

                    last_action = label
                    last_time = current_time

        # --------------------------
        # Encode Frame
        # --------------------------
        ret, buffer = cv2.imencode(".jpg", frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )


# -------------------------------
# Video Feed
# -------------------------------
@app.get("/video")
def video_feed():

    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


# -------------------------------
# Shutdown Webcam
# -------------------------------
@app.on_event("shutdown")
def shutdown():

    camera.release()
    cv2.destroyAllWindows()