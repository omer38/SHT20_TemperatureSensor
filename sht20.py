# This is an library to use SHT20 Temperature sensor in Raspberry Pico Board. Written in Micropython.
# Author : Ömer Tuğrul, 05.08.2022
# https://github.com/omer38/SHT20-TemperatureSensor
# Send me an email if you have questions about the code. omertuggrul@gmail.com

from time import sleep, sleep_ms
from machine import Pin, I2C
from struct import unpack as unp #interpret bytes as binary data

SHT20_addr = 64

# SHT Register addresses, convert them to byte array 
trigger_T_measurment_nh = b'\xf3' 
trigger_T_measurment_h = b'\xe3' #Hold Master mode: Block devices for other communications. SCL line is blocked.
write_ureg = b'\xe6'#b"11100110"
read_ureg = b'\xe7'#b"11100111" 
s_reset =  b'\xfe' #b"11111110"

class SHT20:
    def __init__(self, scl_pin , sda_pin , clk_freq=300000): # max 400kHz
        
        self._addr = SHT20_addr
        
        pin_clk = Pin(scl_pin)
        pin_data = Pin(sda_pin)
        self._bus = I2C(0,scl=pin_clk, sda=pin_data, freq=clk_freq)

    def get_temperature_C(self):
        self._bus.writeto(self._addr, trigger_T_measurment_nh )
        sleep_ms(150) # delay must be inserted, otherwise it gives error. Cannot read-write at the same time.
        
        data = self._bus.readfrom(self._addr, 2)#sensor output 2 byte = 14 bit temperature data.Each byte is followed by an acknowledge bit. The two status bits, the last bits of LSB, must be set to ‘0’ before calculating physical values.
        
        signal = unp('>h', data)[0]  # Packaging type: DFN packaging
        self.__value_c = -46.85 + 175.72 * (signal / 65536)#temperature conversion in celcius in the datasheet.
        return self.__value_c
    
    def get_temperature_F(self):
        
        val_conv = self.get_temperature_C()
        self.__value_F = (val_conv*1.8) + 32
        return self.__value_F

    def get_temperature_K(self):
        val_conv = self.get_temperature_C()
        self.__value_K = val_conv + 273.15
        return self.__value_K
