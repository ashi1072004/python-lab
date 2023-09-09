"""
Expected output:
23:59:59
00:00:00
23:59:59
"""
class Timer:
    def __init__(self, hours, minutes, seconds):
        self.__hh = hours
        self.__mm = minutes
        self.__ss = seconds

    def __str__(self):
        format_str(self.__hh, self.__mm, self.__ss)
        return f'{self.__hh}:{self.__mm}:{self.__ss}'

    def next_second(self):
        self.__ss += 1
        if self.__ss > 59:
            self.__ss -= 60
            self.__mm += 1
        if self.__mm > 59:
            self.__mm -= 60
            self.__hh += 1
        if self.__hh > 23:
            self.__hh -= 24

    def prev_second(self):
        self.__ss -= 1
        if self.__ss < 0:
            self.__ss += 59
            self.__mm -= 1
        if self.__mm < 0:
            self.__mm += 59
            self.__hh -= 1
        if self.__hh < 0:
            self.__hh += 23


def format_str(hours, minutes, seconds):
    if hours < 10:
        hours = '0' + str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if seconds < 10:
        seconds = '0' + str(seconds)

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
