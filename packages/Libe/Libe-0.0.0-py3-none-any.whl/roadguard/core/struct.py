import time
import threading
from bisect import bisect_left

from libem.core.struct import Prompt

_ = Prompt

from roadguard.core.rwlock import RWLock
from roadguard.feed import parameter


class FrameBuffer:
    """
    A time-indexed queue that stores frames and supports pruning.
    """

    def __init__(self,
                 prune_high_watermark=parameter.prune_high_watermark,
                 prune_low_watermark=parameter.prune_low_watermark):
        # frames with time index from prune_high_watermark
        # to prune_low_watermark (w.r.t. current time) will be pruned
        self.frames = []
        self.buffer_lock = RWLock()
        self.frame_update_event = threading.Condition()

        self.prune_high_watermark = prune_high_watermark
        self.prune_low_watermark = prune_low_watermark
        self.pruned = False

    def prune(self):
        self.pruned = True
        with self.buffer_lock.w_locked():
            num_frames_before = len(self.frames)
            prune_ts = self.frames[-1][0] - self.prune_low_watermark
            prune_idx = bisect_left(self.frames, (prune_ts,))
            self.frames = self.frames[prune_idx:]
            print(f"frame buffer: pruned "
                  f"{num_frames_before - len(self.frames)} frames!")
        self.pruned = False

    def put(self, item):
        with self.frame_update_event:
            current_ts = time.time()
            self.frames.append((current_ts, item))
            self.frame_update_event.notify_all()

            tail_ts = self.frames[0][0]
            current_watermark = current_ts - tail_ts
            if not self.pruned and \
                    current_watermark > self.prune_high_watermark:
                threading.Thread(target=self.prune).start()

    def get_range(self, start_ts, end_ts):
        with self.frame_update_event, self.buffer_lock.r_locked():
            head_ts = self.frames[-1][0]
            while self.frames and start_ts > head_ts:
                self.frame_update_event.wait()

            last_read_idx = bisect_left(self.frames, (start_ts,))
            end_reached = False
            while self.frames and not end_reached:
                self.frame_update_event.wait()

                head_idx = len(self.frames)
                for i in range(last_read_idx, head_idx):
                    frame_ts = self.frames[i][0]
                    if frame_ts > end_ts:
                        end_reached = True
                        break
                    yield self.frames[i][1]

                last_read_idx = head_idx


class Scene:
    def __init__(self,
                 frames: list,
                 metadata: dict):
        self.frames = frames
        self.metadata = metadata

    def __len__(self):
        return len(self.frames)

    def __getitem__(self, idx):
        return self.frames[idx]

    def __iter__(self):
        return iter(self.frames)

    def __str__(self):
        return f"Scene(frames={len(self.frames)}, metadata={self.metadata})"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((tuple(self.frames), tuple(self.metadata.items())))

    def __contains__(self, item: str):
        raise NotImplementedError
