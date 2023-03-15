from time import sleep

import pymem
import pymem.process


class Excel:
    dwEntityList = 0x4DFFEF4
    m_bSpotted = 0x93D

    def __init__(self):
        self.pm = pymem.Pymem('csgo.exe')
        self.client = self.get_client(self)
        self.entity = None

    @staticmethod
    def get_client(self):
        return pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll

    def start(self):
        while True:
            for i in range(1, 32):
                self.entity = self.pm.read_int(self.client + self.dwEntityList + i * 0x10)
                if self.entity:
                    self.pm.write_uchar(self.entity + self.m_bSpotted, 1)
            sleep(1)
