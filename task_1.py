class Date:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        _sep = self.data[2]
        day = int(self.data.split(_sep)[0])
        month = int(self.data.split(_sep)[1])
        year = int(self.data.split(_sep)[2])
        if month > 12:
            return f"Only 12 month"
        elif day > 28 and month == 2 and year != [2000, 2004, 2008, 2012, 2016, 2020, 2024]:
            return f"Only 28 days"
        elif day > 30 and month == [4, 6, 9, 11]:
            return f"Only 30 days"
        elif day > 31 and month == [1, 3, 5, 7, 8, 10, 12]:
            return f"Only 31 days"
        else:
            return f"{day} {type(day)}\n{month} {type(month)}\n{year} {type(year)}"


res = Date("23.01.2001")
print(res.get_data())
res = Date("29-02-2001")
print(res.get_data())
res = Date("32/14/2001")
print(res.get_data())
