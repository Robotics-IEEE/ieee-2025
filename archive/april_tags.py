import cv2
import apriltag
import numpy as np

class AprilTagDetector:
    def __init__(self, camera_params, tag_size, camera_source=0):
        self.camera_params = camera_params  # (fx, fy, cx, cy)
        self.tag_size = tag_size
        self.detector = apriltag.Detector()
        self.camera = cv2.VideoCapture(camera_source)
        
        if not self.camera.isOpened():
            raise RuntimeError("Failed to open camera")
    
    def detect_tags(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        return self.detector.detect(blurred)
    
    def estimate_pose(self, detection):
        pose, error = self.detector.detection_pose(detection, self.camera_params, self.tag_size)
        R, t = pose[:3, :3], pose[:3, 3]
        camera_position = -np.dot(R.T, t)  # Transform to tag's coordinate frame
        return camera_position
    
    def annotate_frame(self, frame, detections):
        for detection in detections:
            center = tuple(map(int, detection.center))
            cv2.drawMarker(frame, center, (0, 255, 0), cv2.MARKER_CROSS, 10, 2)
            cv2.putText(frame, str(detection.tag_id), (center[0]+5, center[1]-5), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            for corner in detection.corners:
                corner = tuple(map(int, corner))
                cv2.circle(frame, corner, 5, (255, 0, 255), -1)
        return frame
    
    def run(self):
        while True:
            ret, frame = self.camera.read()
            if not ret:
                break
            
            detections = self.detect_tags(frame)
            for detection in detections:
                camera_position = self.estimate_pose(detection)
                print(f"Tag {detection.tag_id}: Camera Position {camera_position}")
            
            frame = self.annotate_frame(frame, detections)
            cv2.imshow("AprilTag Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    CAMERA_PARAMS = (1575, 1200, 960, 540)  # Approximate values
    TAG_SIZE = 0.112  # Meters

    detector = AprilTagDetector(CAMERA_PARAMS, TAG_SIZE, "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! appsink")
    detector.run()

