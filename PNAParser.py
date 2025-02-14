import random
import re
import math
import time
from algorithm import ampPha2complex
from logger import logger

class PNAParser:
    def __init__(self):
        self._frequencyNum = 0
        self._totalPntNum = 70
        self._cntPntNum = 0
        self._sigmaAmple = 1
        self._sigmaPhase = 0.1
    
    def parse(self, datas):
        ret = None
        msg = datas.decode()
        if re.findall(r"\*IDN\?", msg) != []:
            ret = self._handle_IDN(msg)
        elif re.findall(r"CALC1:DATA\?", msg) != []:
            ret = self._handle_DATA(msg)
        elif re.findall(r"\*OPC\?", msg) != []:
            ret = self._handle_OPC(msg)
        elif re.findall(r"CALC:MARK:Y\?", msg) != []:
            ret = self._handle_MARK(msg)
        elif re.findall(r":WAVeform:POINts\?", msg) != []:
            ret = self._handle_WAVE_POINTS(msg)
        elif re.findall(r":WAVeform:DATA\?", msg) != []:
            ret = self._handle_WAVE_DATA(msg)
        elif re.findall(r"SENS:SEGM:LIST SSTOP", msg) != []:
            ret = self._handle_SEG_LIST_STOP(msg)
        elif re.findall(r"SENS1:SWE:POIN", msg) != []:
            ret = self._handle_SWE_POINT(msg)
        elif re.findall(r"SYST:ERR?", msg) != []:
            ret = self._handle_SYST_ERR(msg)
        else:
            logger.info("not match any rules, return 1")
            ret = "1\n"
        return ret

    def _handle_IDN(self, msg):
        return "Virtual PNA Server v1.0\n"
    
    def _handle_OPC(self, msg):
        return "1\n"
    
    def _handle_MARK(self, msg):
        def randFloat(start=0, end=1):
            return start + (end - start) * random.random()
        return f"{randFloat(-1,1)},{randFloat(-1, 1)}\n"
    
    def _handle_WAVE_POINTS(self, msg):
        return "500000\n"

    def _handle_SYST_ERR(self, msg):
        return "No Error\n"
    
    def _handle_DATA(self, msg):
        self._cntPntNum += 1
        if self._cntPntNum > self._totalPntNum:
            self._cntPntNum = 1
            random.seed(114514)
            self._sigmaAmple *= 0.1
            self._sigmaPhase *= 0.1
            logger.info(f"sigmaAmple: {self._sigmaAmple}, sigmaPhase: {self._sigmaPhase}")
            logger.info("point num clear")

        t = time.time() / 10
        amp = 5 * math.sin(t)
        pha = math.pi * math.cos(t)
        r, i = ampPha2complex(amp, pha)
        pnt = [str(r),str(i)]
        pntLst = pnt * self._frequencyNum

        return ",".join(pntLst) + "\n"
    
    def _handle_WAVE_DATA(self, msg):
        suffix = msg[15:]
        if len(suffix) > 0:
            params = suffix.split(",")
            if len(params) > 1:
                start = int(params[0])
                size = int(params[1])
                size = size * 2
            else:
                size = 20000
            tmp = "#0"
            for i in range(size):
                tmp += str(i%10)
            return tmp

        else:
            tmp = "#0"
            for i in range(20000):
                tmp += str(i%10)
            return tmp

    def _handle_SEG_LIST_STOP(self, msg):
        self._frequencyNum = 1
        try:
            msgLst = msg.split(",")
            self._frequencyNum = int(msgLst[1])
            random.seed(114514)
            self._sigmaAmple = 1
            self._sigmaPhase = 0.1
            self._cntPntNum = 0
            logger.info(f"frequency num is: {self._frequencyNum}")
        except Exception as e:
            logger.error(f"get frequency num error, msg: {e}")

    def _handle_SWE_POINT(self, msg):
        self._frequencyNum = 1
        try:
            msg.replace("\n", "")
            msgLst = msg.split(" ")
            self._frequencyNum = int(msgLst[1])
            random.seed(114514)
            self.igmaAmple = 1
            self.igmaPhase = 0.1
            self._cntPntNum = 0
            logger.info(f"frequency num is: {self._frequencyNum}")
        except Exception as e:
            logger.error(f"get frequency num error, msg: {e}")
