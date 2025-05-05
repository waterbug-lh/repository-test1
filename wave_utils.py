import logging
logging.basicConfig(level=logging.INFO)

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        logging.error("除零错误:%s",e)
        return None


def is_valid_impluse(lengths):
    # 判断三浪是不是最短的浪
    return lengths[1]>min(lengths[0],lengths[2])

def fibonacci_ratio(a,b,target=1.618,tol=0.05):
    #判断b是否约等于a*target
    ratio=b/a if a!=0 else 0
    return abs(ratio-target)<tol;

