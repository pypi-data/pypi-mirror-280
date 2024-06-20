import ffmpeg
import numpy as np
import cv2


from .log import logger


class VideoStream:
    def __init__(self, url, logger=logger, ffmpeg_log_level="quiet") -> None:
        self._logger = logger
        args = {
            "rtsp_transport": "tcp",
            "fflags": "nobuffer",
            "flags": "low_delay",
            "loglevel": ffmpeg_log_level
        }

        probe = ffmpeg.probe(url)
        cap_info = next(
            x for x in probe['streams']
            if x['codec_type'] == 'video'
        )

        fram_rate = str(cap_info['r_frame_rate'])
        self._logger.info(f"fps: {fram_rate}")

        self._width = cap_info['width']  # get video stream width
        self._height = cap_info['height']  # get video stream height

        up, down = fram_rate.split('/')
        fps = eval(up) / eval(down)
        self._logger.info(f"fps: {fps}")

        self._proc = (
            ffmpeg
            .input(url, **args)
            .output('pipe:', format='rawvideo', pix_fmt='rgb24')
            .overwrite_output()
            .run_async(pipe_stdout=True)
        )

    def stream_read(self):
        # while True:
        in_bytes = self._proc.stdout.read(
            self._width * self._height * 3)     # read image
        if not in_bytes:
            return False, None

        # transfor to ndarray
        in_frame = (
            np.frombuffer(in_bytes, np.uint8).reshape(
                [self._height, self._width, 3])
        )

        frame = cv2.cvtColor(in_frame, cv2.COLOR_RGB2BGR)  # change to BGR
        return True, frame

    def close(self):
        self._proc.kill()             # close
