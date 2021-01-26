# class MyCalendar:
#     def __init__(self):
#         self.timings = []

#     def book(self, start, end):
#         print(self.timings)
#         if len(self.timings) == 0:
#             time_slot = (start, end)
#             self.timings.append(time_slot)
#             return True
#         else:
#             for i in self.timings:
#                 if start in range(i[0], i[1]) or end in range(i[0], i[1]):
#                     return False
#                 else:
#                     time = (start, end)
#                     self.timings.append(time)
#                     return True


class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        for i, j in self.bookings:
            if i < end and j > start:
                return False
        self.bookings.append((start, end))
        return True


myCalendar = MyCalendar()
myCalendar.book(10, 20)
myCalendar.book(15, 25)
myCalendar.book(20, 30)
