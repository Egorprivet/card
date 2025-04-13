import time

class GameTimer:
    def __init__(self, duration=90):
        self.duration = duration
        self.start_time = None  

    def init_timer(self):
        self.start_time = time.time()

    def get_time_left(self):
        if self.start_time is None:
            return self.duration
        elapsed = time.time() - self.start_time 
        left = int(self.duration - elapsed)  
        return max(0, left)
    def is_finished(self):
        return self.get_time_left() <= 0