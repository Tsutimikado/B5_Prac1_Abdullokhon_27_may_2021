def time_this(rep_num):
    def decorator(func):
        def wrap(param=None):
            avg_time = 0
            if param is None:
                t0 = time.time()
                for i in range(1,rep_num+1,1):
                    func()
                t1 = time.time()
            else:
                t0 = time.time()
                for i in range(1,rep_num+1,1):
                    func(param)

                t1 = time.time()
            avg_time += (t1 - t0)
            print("Выполнение заняло %.5f секунд" % (avg_time/rep_num))
            return avg_time/rep_num
        return wrap
    return decorator

@time_this(10)
def pass_():
    for j in range(100000):
        print(j)

pass_()