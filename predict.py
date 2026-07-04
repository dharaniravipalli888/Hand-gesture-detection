from ultralytics import YOLO

# Load trained model
model = YOLO(r"runs\classify\runs\hand_gesture\weights\best.pt")

# Test on a single image
results = model.predict(
    source=r"C:\Users\tarun\Music\hand_gesture_detection\data_set\03_thumbs-up\03_thumbs-up_0.jpg",   # Replace with your image
    show=True,
    save=True
)

result = results[0]

class_id = result.probs.top1
confidence = result.probs.top1conf.item()

print("Predicted Class :", model.names[class_id])
print("Confidence      :", round(confidence * 100, 2), "%")