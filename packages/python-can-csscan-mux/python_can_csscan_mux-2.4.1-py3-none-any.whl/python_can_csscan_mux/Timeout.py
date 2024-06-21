import datetime


class Timeout(object):
    def __init__(self, timeout: float):
        self._initial_time = datetime.datetime.now()
        
        if timeout is None:
            self._timeout = datetime.datetime.max
        elif timeout < 0:
            raise ValueError("Timeout must be positive")
        else:
            self._timeout = self._initial_time + datetime.timedelta(seconds=timeout)
        
        return
    
    def time_left(self) -> float:
        time_left = self._timeout - datetime.datetime.now()
        result = time_left.total_seconds()
        if time_left < datetime.timedelta(0):
            result = 0
        
        return result
    
    def expired(self) -> bool:
        return datetime.datetime.now() > self._timeout
    
    pass
