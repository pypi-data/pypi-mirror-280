# distutils: language = c++
# cython: language_level = 3

from libc.stdlib cimport malloc
from iarduino_I2C_Keyboard cimport iarduino_I2C_Keyboard
#from time import sleep

DEF_CHIP_ID_FLASH   =   0x3C
DEF_CHIP_ID_METRO   =   0xC3
DEF_MODEL_KBD       =   0x13

# Адреса регистров модуля:
REG_FLAGS_0         =   0x00
REG_BITS_0          =   0x01
REG_FLAGS_1         =   0x02
REG_BITS_1          =   0x03
REG_MODEL           =   0x04
REG_VERSION         =   0x05
REG_ADDRESS         =   0x06
REG_CHIP_ID         =   0x07
REG_KBD_KEYS        =   0x10
REG_KBD_LED_L       =   0x1A
REG_KBD_LED_H       =   0x1B
REG_KBD_FIFO_HOLD   =   0x1C
REG_KBD_FIFO_REPLAY =   0x1D
REG_KBD_FIFO_COUNTER=   0x1E
REG_KBD_FIFO        =   0x1F
REG_KBD_TIME_KEYS   =   0x20
REG_KBD_ANIMATION   =   0x2A
REG_KBD_TIME_ANIM   =   0x2B

# Позиция битов и флагов:
KBD_FLG_PUSHED      =   0x80
KBD_FLG_RELEASED    =   0x40
KBD_FLG_CHANGED     =   0x20
KBD_FLG_STATE       =   0x10
KBD_FLG_TRIGGER     =   0x08
KBD_TIM_HOLD        =   0x07

KEY_PUSHED          =   1
KEY_RELEASED        =   2
KEY_STATE           =   3
KEY_TRIGGER         =   4
KEY_HOLD_05         =   5
KEY_HOLD            =   6
KEY_FREE            =   7
KEY_CHANGED         =   8
KEY_ALL             =   0xFF
LED_ALL             =   0xFF

NO_BEGIN = 1

cdef class pyiArduinoI2Ckeyboard:
    cdef iarduino_I2C_Keyboard c_module

    _cols = 5
    _rows = 2

    def __cinit__(self, address=None, cols=None, rows=None, auto=None):

        if cols is None:
            cols=self._cols

        if rows is not None:
            rows=self._rows

        if address is not None:

            self.c_module = iarduino_I2C_Keyboard(address, cols, rows)

            if auto is None:
                #sleep(.5)
                if not self.c_module.begin():

                    print("ошибка инициализации модуля.\n"
                          "Проверьте подключение и адрес модуля,"
                          " возможно не включен интерфейс I2C.\n"
                          " Запустите raspi-config и включите интерфейс"
                          ", инструкция по включению:"
                          " https://wiki.iarduino.ru/page/raspberry-i2c-spi/")

        else:

            self.c_module = iarduino_I2C_Keyboard(0, cols, rows)

            if auto is None:
                #sleep(.5)
                if not self.c_module.begin():

                    print("ошибка инициализации модуля.\n"
                          "Проверьте подключение и адрес модуля, "
                          " возможно не включен интерфейс I2C.\n"
                          " Запустите raspi-config и включите интерфейс"
                          ", инструкция по включению:"
                          " https://wiki.iarduino.ru/page/raspberry-i2c-spi/")

    def begin(self):
        return self.c_module.begin()

    def changeAddress(self, unsigned char newAddr):
        return self.c_module.changeAddress(newAddr)

    def reset(self):
        return self.c_module.reset()

    def getAddress(self):
        return self.c_module.getAddress()

    def getVersion(self):
        return self.c_module.getVersion()

    def getPullI2C(self):
        return self.c_module.getPullI2C()

    def setPullI2C(self, flag=None):
        if flag is not None:
            return self.c_module.setPullI2C(flag)
        else:
            return self.c_module.setPullI2C(True)

    def available(self):
        return self.c_module.available()

    def readChar(self):
        return chr(self.c_module.readChar())

    def readString(self, n, end=None):
        if end is None:
            end = True
        cdef unsigned char* c_string = <unsigned char *> malloc((n + 1) * sizeof(char))
        if not c_string:
            return 0
        nbytes = self.c_module.readString(c_string, n, end)
        return c_string, nbytes

    def flush(self):
        self.c_module.flush()

    def setEncoding(self, col, row = None, sym = None):
        if row is None and sym is None and isinstance(col, str):
            self.c_module.setEncStr(col.encode('utf-8'))
        else:
            self.c_module.setEncoding(col, row, ord(sym[0]))

    def getEncoding(self, col, row=None):
        if row is None:
            return self.c_module.getEncChar(col)
        else:
            return self.c_module.getEncoding(col, row)


    def setDelay(self, tim):
        self.c_module.setDelay(tim)

    def getDelay(self):
        return self.c_module.getDelay()

    def setPeriod(self, tim):
        self.c_module.setPeriod(tim)

    def getPeriod(self):
        return self.c_module.getPeriod()

    def getKey(self, col, row, typ=None):
        if typ is None:
            if isinstance(col, str):
                return self.c_module.getKeyChar(ord(col), row)
            else:
                return self.c_module.getKeyChar(col, row)
        else:
            return self.c_module.getKey(col, row, typ)

    def getTime(self, col, row, typ=None):
        if typ is None:
            if isinstance(col, str):
                return self.c_module.getTimeChar(ord(col), row)
            else:
                return self.c_module.getTimeChar(col, row)
        else:
            return self.c_module.getTime(col, row, typ)

    def setLed(self, col, row, f=None):
        if f is None:
            if isinstance(col, str):
                self.c_module.setLedChar(ord(col), row)
            else:
                self.c_module.setLedChar(col, row)
        else:
            self.c_module.setLed(col, row, f)

    def getLed(self, col, row=None):
        if row is None:
            return self.c_module.getLedChar(col)
        else:
            return self.c_module.getLed(col, row)

    def setLight(self, light, group=None):
        if group is None:
            group = LED_ALL
        self.c_module.setLight(light, group)

    def getLight(self, group=None):
        if group is None:
            group = LED_ALL
        return self.c_module.getLight(group)

    def setAnimation(self, num, tim=None):
        if tim is None:
            tim = 200
        self.c_module.setAnimation(num, tim)

    def getAnimation(self):
        return self.c_module.getAnimation()

