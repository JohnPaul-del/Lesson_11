class Date:
    def __init__(self, data):
        self.data = data

    @classmethod
    def get_data(cls, data):
        if data[1].isdigit():
            _sep = data[2]
        else:
            _sep = data[1]
        day = int(data.split(_sep)[0])
        month = int(data.split(_sep)[1])
        year = int(data.split(_sep)[2])
        return cls.check_date(day, month, year)

    @staticmethod
    def check_date(day, month, year):
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


res_1 = Date.get_data("03.01.2001")
print(res_1)
res_2 = Date.get_data("28-02-2000")
print(res_2)
res_3 = Date.get_data("32/14/2001")
print(res_3)
