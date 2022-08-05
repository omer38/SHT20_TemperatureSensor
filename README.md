# SHT20_TemperatureSensor
This is an library to use SHT20 Temperature sensor in Raspberry Pico Board. Written in Micropython.

# Documentation:

* SHT20 Class:
    * __init__(scl_pin , sda_pin , clk_freq=400000):  clock frequency max 400kHz
        
          scl_pin : The pin number of the scl.
          sda_pin : The pin number of th sda.
        
    * get_temperature_C() : returns the temperature value degree in Celcuis.
    
    * get_temperature_F() : returns the temperature value in Fahrenheit.
    
    * get_temperature_K() : returns the temperature value in Kelvin.
    
# Example Code
    from sht20 import SHT20

    sht = SHT20(5,4)# scl_pin, sda_pin

    while True:
        print(sht.get_temperature_C())
        print(sht.get_temperature_F())
        print(sht.get_temperature_K())
