import multiprocessing as mp


def job(x):
    return x**3

def multiprocess():
    #mp.Pool()进程数processes默认为cpu核数
    pool = mp.Pool(processes=2)
    res = pool.map(job, range(10))
    print(res)

    #使用apply_async()只能传一组参数
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])



if __name__ == "__main__":
    multiprocess()