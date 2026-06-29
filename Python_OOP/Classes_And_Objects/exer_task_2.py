class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hours = str(self.hours) if self.hours >= 10 else "0" + str(self.hours)
        minutes = str(self.minutes) if self.minutes >= 10 else "0" + str(self.minutes)
        seconds = str(self.seconds) if self.seconds >= 10 else "0" + str(self.seconds)
        return f"{hours}:{minutes}:{seconds}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 0

        return self.get_time()