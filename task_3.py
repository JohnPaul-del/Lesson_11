class NumbersErr(ValueError):
    def __init__(self, msg):
        self.msg = msg


val = ""
res = []
while val.upper() != "STOP":
    val = input("Enter number or 'Stop' for exit: ")
    try:
        if val.isdigit():
            res.append(val)
        else:
            raise NumbersErr("Only numbers")
    except NumbersErr as err:
        print("Only numbers!")

print(res)
