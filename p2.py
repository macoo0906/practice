def get_integer(prompt):
    hi = int(input(prompt))
    return hi

def convert_time(T):
    hour = T // 3600
    T %= 3600
    min = T // 60
    T %= 60
    sec = T
    print(time,'초는',hour,'시간',min,'분',sec,'초이다.')



time = get_integer('변환하고자 하는 시간은? ')

convert_time(time)