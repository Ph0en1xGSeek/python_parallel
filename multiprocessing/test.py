import multiprocessing as mp
import threading as td
import time

#串行执行
def serial():
    res = 0
    for i in range(100000):
        res += i**3 + i**2 + i
    print('serial:', res)

def job(q, a):
    res = 0
    #两个进程/线程分别负责前半部分和后半部分
    for i in range(50000*a, 50000*(a+1)):
        res += i**3 + i**2 + i
    #结果放入queue中
    q.put(res)

def multiprocess():
    # 使用queue
    q = mp.Queue()
    #传入参数
    p1 = mp.Process(target=job, args=(q, 0))
    p2 = mp.Process(target=job, args=(q, 1))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    res1 = q.get()
    res2 = q.get()

    print('multiprocess:',res1 + res2)

def multithread():
    # 使用queue
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q, 0))
    t2 = td.Thread(target=job, args=(q, 1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    res1 = q.get()
    res2 = q.get()

    print('multithread:', res1 + res2)






if __name__ == '__main__':

    st = time.time()
    serial()
    st1 = time.time()
    print('serial time:', st1 - st, "\n")
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1, "\n")
    multiprocess()
    print('multiprocess time:', time.time() - st2, "\n")


