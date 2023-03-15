import pymem
import pymem.process
import keyboard

dwEntityList = (0x4DFFEF4)
m_bSpotted = (0x93D)


def main():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        if keyboard.is_pressed("end"):
            exit(0)
        for i in range(1, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)
            if entity:
                pm.write_uchar(entity + m_bSpotted, 1)


if __name__ == '__main__':
    main()
