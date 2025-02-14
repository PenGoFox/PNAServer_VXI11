from logger import logger
from vxi11server import TCPServer
from PNAParser import PNAParser

class PNAServer(TCPServer):
    def __init__(self, host, port):
        super().__init__(host, 395183, 1, port)

        self.parser = PNAParser()

    def handle_10(self):
        params = self.unpacker.unpack_create_link_parms()
        logger.info('CREATE_LINK %s' ,params)
        self.packer.pack_create_link_resp(0, 0, 10000, 10024)

    def handle_11(self):
        params = self.unpacker.unpack_device_write_params()
        self.packer.pack_device_write_resp(0,len(params[4]))
        logger.info('DEVICE_WRITE %s', params)
        self.wts = self.parser.parse(params[4])

    def handle_12(self):
        #params = self.unpacker.unpack_device_write_params()
        data = self.wts.encode()
        if len(data) > 2000:
            logger.info(f"data is:{data[:2000]}")
        else:
            logger.info(f"data is:{data}")
        self.packer.pack_device_read_resp(0, 0, data)

    def handle_23(self):
        params = self.unpacker.unpack_destroy_link_params()
        logger.info('DESTROY_LINK %s', params)
        self.packer.pack_device_error(0)

