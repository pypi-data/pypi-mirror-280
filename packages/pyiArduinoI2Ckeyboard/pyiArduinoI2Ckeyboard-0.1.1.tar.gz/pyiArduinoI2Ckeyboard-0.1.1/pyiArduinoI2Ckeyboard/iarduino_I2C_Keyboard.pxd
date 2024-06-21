cdef extern from "iarduino_I2C_Keyboard.cpp":
    pass

cdef extern from "itoa.cpp":
    pass

cdef extern from "dtostrf.cpp":
    pass

cdef extern from "WString.cpp":
    pass

cdef extern from "iarduino_I2C_Keyboard.h":
    cdef cppclass iarduino_I2C_Keyboard:
        iarduino_I2C_Keyboard() except +
        iarduino_I2C_Keyboard(unsigned char) except +
        iarduino_I2C_Keyboard(unsigned char, unsigned char) except +
        iarduino_I2C_Keyboard(unsigned char, unsigned char, unsigned char) except +
        bint begin()
        bint changeAddress(unsigned char)
        bint reset()
        unsigned char getAddress()
        unsigned char getVersion()

        bint getPullI2C()
        bint setPullI2C(bint)
        unsigned char available()
        char readChar()
        unsigned char readString(unsigned char*, unsigned char, bint)
        void flush()
        void setEncoding(unsigned char, unsigned char, char)
        void setEncStr "setEncoding"(char*)
        #void setEncoding(String i)
        char getEncoding(unsigned char, unsigned char)
        unsigned char getEncChar "getEncoding"(const char)
        void setDelay(unsigned short)
        unsigned short getDelay()
        void setPeriod(unsigned short)
        unsigned short getPeriod()
        unsigned short getKey(unsigned char,unsigned char,unsigned char)
        unsigned short getKeyChar "getKey"(char, unsigned char)
        unsigned short getTime(unsigned char,unsigned char,unsigned char)
        unsigned short getTimeChar "getTime"(char, unsigned char)
        void setLed(unsigned char, unsigned char, unsigned short)
        void setLedChar "setLed"(char, unsigned short)
        unsigned short getLed(unsigned char, unsigned char)
        unsigned short getLedChar "getLed"(char)
        void setLight(unsigned char,unsigned char)
        unsigned char getLight(unsigned char)
        void setAnimation(unsigned char, unsigned short)
        unsigned char getAnimation()

