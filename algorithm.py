import math

def ampPha2complex(amp, pha):
    '''
    把幅值相位转换为复数

    返回值为复数元组

    @param amp 幅值，单位为 dBm
    @param pha 相位，单位为 rad
    '''

    A = 10 ** (amp / 20)
    r = A * math.cos(pha)
    i = A * math.sin(pha)
    return r, i