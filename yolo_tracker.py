import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

heatmap = np.zeros((500, 500), dtype=np.float32)
restricted_zone = (0.3, 0.3, 0.7, 0.7)  # normalized

def process_frame(frame):
    global heatmap

    results = model(frame)

    people_positions = []
    alert = False

    h, w, _ = frame.shape

    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cx = (x1 + x2)//2
                cy = (y1 + y2)//2

                # NORMALIZED POSITION
                nx = cx / w
                ny = cy / h

                people_positions.append((nx, ny))

                # HEATMAP
                hx = int(nx * 500)
                hy = int(ny * 500)
                heatmap[hy % 500, hx % 500] += 1

                # ZONE CHECK
                rx1, ry1, rx2, ry2 = restricted_zone
                if rx1 < nx < rx2 and ry1 < ny < ry2:
                    alert = True

                # DRAW
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

    return frame, people_positions, alert, heatmap