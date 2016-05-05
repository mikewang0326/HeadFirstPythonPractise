import os


# def sanitize(time_string):
#     if ("-" in time_string):
#         splitter = '-'
#         (mins, seconds) = time_string.split(splitter)
#         return mins + "." + seconds
#     elif (':' in time_string):
#         splitter = ":"
#         (mins, seconds) = time_string.split(splitter)
#         return mins + "." + seconds
#     else:
#         return time_string


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_time=[]):
        list.__init__([])
        self.name = a_name
        self.dob=a_dob
        self.extend(a_time)

    def sanitize(self, time_string):
        if ("-" in time_string):
            splitter = '-'
            (mins, seconds) = time_string.split(splitter)
            return mins + "." + seconds
        elif (':' in time_string):
            splitter = ":"
            (mins, seconds) = time_string.split(splitter)
            return mins + "." + seconds
        else:
            return time_string

    def top3(self):
        return (sorted(set([self.sanitize(t) for t in self]))[0:3])


vera = AthleteList('vera vi')
vera.append('1.31')
print(vera.top3())

vera.extend(['3.4', '7.4', '3.4'])
print(vera.top3())