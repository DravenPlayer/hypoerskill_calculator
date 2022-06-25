# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
memory = 0
b = False
a = False


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer() is True:
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if v1 == 1 or v2 == 1 and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == '-'):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    if b:
        break

    calc = input(msg_0)
    array = calc.split()
    x = array[0]
    y = array[-1]
    oper = array[1]
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    else:
        if oper != "+" and oper != "-" and oper != "*" and oper != "/":
            print(msg_2)

            continue
        else:
            pass
    finally:
        check(x, y, oper)
        x = float(x)
        y = float(y)
        if oper == "+":
            result = x + y
            print(result)
        elif oper == "-":
            result = x - y
            print(result)
        elif oper == "*":
            result = x * y
            print(result)
        elif oper == "/":
            try:
                result = x / y
            except ZeroDivisionError:
                print(msg_3)
                continue
            else:
                print(result)

    while True:
        answer = input(msg_4)
        if answer == "y":
            mesg = {10: msg_10, 11: msg_11, 12: msg_12}
            if is_one_digit(result):

                msg_index = 10
                while True:
                    answer = input(mesg[msg_index])
                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer == "n":
                        break
                    else:
                        continue
            else:
                memory = result
                pass
        elif answer != "n" and answer != "y":
            continue

        elif answer == "n":
            memory = 0
        while True:
            answer_5 = input(msg_5)
            if answer_5 == "y":
                a = True
                break

            elif answer_5 == "n":
                b = True
                break
            else:
                continue
        if b or a:
            break
