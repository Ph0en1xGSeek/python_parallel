# shared value and lock
import multiprocessing as mp
import time

def job(v, num, l):
    #请求锁
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value = v.value + num
        print(v.value)
    #释放锁
    l.release()

def multiprocess():

    #共享变量
    v = mp.Value('i', 0)
    #互斥锁
    l = mp.Lock()

    p1 = mp.Process(target=job, args=(v, -1, l))
    p2 = mp.Process(target=job, args=(v, 1, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('final:', v.value)


if __name__ == "__main__":

    multiprocess()

'''
without lock
-1
0
-1
0
-1
0
-1
0
-1
1
1
1
2
1
0
2
3
3
2
4
final: 4

with lock
-1
-2
-3
-4
-5
-6
-7
-8
-9
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
0
final: 0
'''