import os
import threading

from roadguard.feed import (
    file, speaker, camera
)
from roadguard.ingest import video
from roadguard.constant import RG_SAMPLE_DATA_PATH
from roadguard.core.struct import FrameBuffer

DEFAULT_VIDEO_PATH = os.path.join(
    RG_SAMPLE_DATA_PATH,
    "didi", "city-5s.mp4"
)


def report():
    frames = file.extract_frame(
        path=DEFAULT_VIDEO_PATH,
        seconds_per_frame=1,
    )

    transcription = video.summarize(frames)

    return transcription


def listen():
    print("RoadGuard is listening...")
    print("Press Ctrl+C to stop listening")

    print("Searching camera...")
    camera_index = camera.find_working_camera_index()
    if camera_index is None:
        raise ValueError('No working camera found.')
    print(f"Using camera of index: {camera_index}")

    def stream():
        print("Streaming video...")
        camera.stream(frame_buffer, camera_index=camera_index)

    def capture_and_summarize():
        print("Processing video...")

        frames = camera.capture(frame_buffer)
        print(f"Captured {len(frames)} frames")
        transcription = video.summarize(frames)

        print(f"Transcription: {transcription}")

    def on_trigger():
        print("Trigger detected!")
        process_thread = threading.Thread(target=capture_and_summarize())
        process_thread.start()

    # Assuming 'speaker.trigger_and_run' sets up
    frame_buffer = FrameBuffer()
    stream_thread = threading.Thread(target=stream)
    stream_thread.start()
    speaker.trigger_and_run(
        func=on_trigger,
    )
