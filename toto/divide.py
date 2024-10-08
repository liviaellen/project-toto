from bdb import set_trace
from toto.lib import who_am_i


def divide_custom(x:float, y:float) -> float:
    '''divide x by y, but instead of raising errors when y equals 0, returns:
    - inf if x positive
    - -inf if x negative
    - nan if x equals 0
    '''

    who_am_i()
    if y !=0.:
        return x/y
    else:
        if x > 0. :
            return float("inf")
        if x < 0. :
            return -1 * float("inf")
        if x == 0. :
            return float('nan')

if __name__ == '__main__':
    try:
        divide_custom(2., 1.)
    except:
        import ipdb, traceback, sys
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
