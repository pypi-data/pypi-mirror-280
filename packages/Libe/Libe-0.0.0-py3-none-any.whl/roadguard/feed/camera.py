import os
import sys
import cv2
import time
import base64

from roadguard.feed import parameter


def add_mosaic(frame, x, y, w, h, factor=parameter.mosaic_factor):
    """Apply a mosaic to a region of the frame."""
    roi = frame[y:y + h, x:x + w]
    roi = cv2.resize(roi, (w // factor, h // factor),
                     interpolation=cv2.INTER_LINEAR)
    roi = cv2.resize(roi, (w, h),
                     interpolation=cv2.INTER_NEAREST)
    frame[y:y + h, x:x + w] = roi
    return frame


def frame_to_base64(frame):
    """Convert a frame to a base64 string."""
    _, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(buffer).decode('utf-8')


class SuppressOpenCVErrors:
    """
    A context manager to suppress OpenCV related errors by
    redirecting stderr at the OS level.
    """

    def __enter__(self):
        self.err_fd = sys.stderr.fileno()
        self.saved_err_fd = os.dup(self.err_fd)
        self.devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(self.devnull, self.err_fd)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.dup2(self.saved_err_fd, self.err_fd)
        os.close(self.saved_err_fd)
        os.close(self.devnull)


def find_working_camera_index(end_index=parameter.max_camera_index):
    """
    Find the index of the first working external camera,
    starting from a given index and moving downwards, while silently
    ignoring any missing or inaccessible cameras.
    """
    for index in range(0, end_index):
        with SuppressOpenCVErrors():
            cap = cv2.VideoCapture(index)
        if cap.isOpened():
            ret, _ = cap.read()
            cap.release()
            if ret:
                return index
        if cap.isOpened():
            cap.release()
    return None


def stream(frame_buffer,
           target_fps=parameter.target_fps,
           display=False, camera_index=None):
    camera_index = camera_index or find_working_camera_index()
    if camera_index is None:
        raise ValueError('No working camera found.')

    cap = cv2.VideoCapture(camera_index)
    # Calculate the interval between frames for the target frame rate
    frame_interval = 1 / target_fps
    last_capture_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_time = time.time()
        if current_time - last_capture_time >= frame_interval:
            last_capture_time = current_time
            frame_buffer.put(frame)

            # Display the resulting frame
            if display:
                cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    if display:
        cv2.destroyAllWindows()


def capture(
        frame_buffer,
        lookback_duration=parameter.lookback_duration,
        lookahead_duration=parameter.lookahead_duration,
        display=False):
    """
    Capture and preprocess the frames in the frame buffer by
    detecting faces and license plates and applying a mosaic to them.

    Returns a list of base64 encoded frames.
    """
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
    )
    plate_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_license_plate_rus_16stages.xml'
    )

    base64_frames = []
    current = time.time()
    start = current - lookback_duration
    end = current + lookahead_duration

    for frame in frame_buffer.get_range(start, end):
        print(f'Processing frame {len(base64_frames)}')
        # Detect faces and plates
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        plates = plate_cascade.detectMultiScale(frame, 1.3, 5)

        mosaic_frame = frame
        if len(faces) > 0 or len(plates) > 0:
            mosaic_frame = frame.copy()

        # Apply mosaic to faces and plates
        for (x, y, w, h) in faces:
            mosaic_frame = add_mosaic(mosaic_frame, x, y, w, h)
        for (x, y, w, h) in plates:
            mosaic_frame = add_mosaic(mosaic_frame, x, y, w, h)

        # Encode the frame to base64
        base64_frame = frame_to_base64(mosaic_frame)
        base64_frames.append(base64_frame)

        # Display the resulting frame
        if display:
            cv2.imshow('Video', mosaic_frame)

    return base64_frames


def test():
    from roadguard.core.struct import TimeIndexedQueue
    frame_buffer = TimeIndexedQueue()
    stream(frame_buffer, display=True)
    base64_encoded_frames = capture(frame_buffer, 5)
    print(len(base64_encoded_frames))


if __name__ == "__main__":
    test()
