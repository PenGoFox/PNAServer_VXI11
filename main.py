#!/usr/bin/python3

from logger import logger
from PNAServer import PNAServer

def startRTCServer():
    s = PNAServer('', 0)

    try:
        s.unregister()
    except OSError as msg:
        logger.error(f'Error: rpcbind -i not running? {msg}')
        return
    except RuntimeError as msg:
        logger.error(f'RuntimeError: {msg} (ignored)')

    try:
        s.register()
    except RuntimeError as msg:
        logger.error(f"Error: rpcbind running in secure mode? {msg}")
        raise

    try:
        s.sock.listen(0)
        logger.info('Virtual RTC Service started...')
        while 1:
            logger.info("PNA waiting for connect...")
            s.session(s.sock.accept())
    finally:
        s.unregister()

if __name__ == "__main__":
    try:
        startRTCServer()
    except KeyboardInterrupt as e:
        logger.info("good bye")
