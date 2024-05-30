import utime
from machine import Pin, PWM

# Motorlar
m_sag = Pin(21, Pin.OUT)
m_sol = Pin(22, Pin.OUT)

# Önce motorları bir kez durduralım.
m_sag.low()
m_sol.low()

# Mesafe Sensörü
trig = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)

def mesafe():
    trig.low()
    utime.sleep_us(2)
    trig.high()
    utime.sleep_us(5)
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    gecenZaman = signalon - signaloff
    mesafe = (gecenZaman * 0.0343) / 2
    print("Ölçülen mesafe=", mesafe)
    return mesafe

def dur():
    m_sag.low()
    m_sol.low()
    utime.sleep(0.1)
    
def ileri():
    m_sag.high()
    m_sol.high()
    utime.sleep(0.1)

def sol():
    m_sag.high()
    m_sol.low()
    utime.sleep(0.1)
    
def sag():
    m_sag.low()
    m_sol.high()
    utime.sleep(0.1)

say = 0

while say < 2:
    print(say)
    
    u = mesafe()
    print(u)
    if u < 10:
        say += 1
        utime.sleep(0.5)


while True:
    uzaklik = mesafe()
    #print("mesafe:", uzaklik)
    if uzaklik > 10:
        ileri()
    elif uzaklik <= 10:
        sol()
        utime.sleep(0.5)
    
