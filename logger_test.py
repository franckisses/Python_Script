import traceback
import sys
import logging

gList = ['a','b','c','d','e','f','g']
logging.basicConfig(
    level=logging.DEBUG,
    filename='mylog.txt',
    filemode='w',
    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelbane)s %(message)s"
)

def f():
    gList[5]
    logging.info('[info]:calling method g() in f()')
    return g()

def g():
    logging.info('[info]:calling method in gList in h()')
    return h()

def h():
    logging.info('[info]:delete element in gList in h()')
    del gList[2]
    logging.info('[info]:calling method i() in h()')
    return i()

def i():
    logging.info('[info]: append element i to gList in i()')
    gList.append('i')
    print(gList[7])


if __name__ == "__main__":
    logging.debug('information during calling f()')
    try:
        f()
    except IndexError as ex:
        print('sorry')
        ty,tv,tb = sys.exc_info()
        logging.error('[error]:sorry exception occured,you accessed an element out of range')
        logging.critical('object info:%s'%ex)
        logging.critical('[error type:{0},error information{1}'.format(ty,tv))
        logging.critical(''.join(traceback.format_tb(tb)))
        sys.exit(1)
        