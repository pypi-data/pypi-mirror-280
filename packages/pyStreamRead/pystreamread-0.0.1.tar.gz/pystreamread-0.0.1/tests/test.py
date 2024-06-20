import add_path

import cv2

from stream import VideoStream


def test_read_stream():
    video_stream = VideoStream(
        "rtsp://192.168.0.205:554/H264?W=1280&H=960&BR=2000000&FPS=30")

    while True:
        ok, frame = video_stream.stream_read()
        if not ok:
            continue

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


test_read_stream()
