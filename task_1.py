class Date:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        _sep = self.data[2]
        day = int(self.data.split(_sep)[0])
        month = int(self.data.split(_sep)[1])
        year = int(self.data.split(_sep)[2])
        return f"{day} {type(day)}\n{month} {type(month)}\n{year} {type(year)}"


res = Date("23.01.2001")
print(res.get_data())
# res = Date("23-01-2001")
# print(res.get_data())
# res = Date("23/01/2001")
# print(res.get_data())
