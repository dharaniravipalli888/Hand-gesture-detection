from ultralytics import YOLO

def main():
    # Load YOLO11 Classification model
    model = YOLO("yolo11n-cls.pt")

    # Train on your dataset
    model.train(
        data="data_set",
        epochs=50,
        imgsz=224,
        batch=16,
        project="runs",
        name="hand_gesture",
        device="cpu"   # Use 0 if you have an NVIDIA GPU
    )

    print("Training Completed!")

if __name__ == "__main__":
    main()