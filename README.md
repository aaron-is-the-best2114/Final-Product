# Final-Product

## Wiring

**Day 1 RFID Module**

  **1.** Connect the `SDA` pin on the RFID module to the `SPICE0` or `GPIO 8` on the Raspberry Pi. Physical Pin `24`
  
  **2.** Connect the `SCK` pin on the module to the `SPISCLK` or `GPIO 11` on the Raspberry Pi. Physical Pin `23`
  
  **3.** Connect the `MOSI` pin on the module to the `SPIMOSI` or `GPIO 10` on the Raspberry Pi. Pysical Pin `19`

  **4.** Connect the `MISO` pin on the module to the `SPIMISO` or `GPIO 9` on the Raspberry Pi. Physical Pin `21`

  **5.** Skip the `IRQ` pin on the module and connect the `GND` pin on the module to a `GND` pin on the Raspberry Pi

  **6.** Connect the `RST` pin on the module to `GPIO 25` on the Raspberry Pi. Physical Pin `22`

  **7.** Connect the `3.3V` pin on the module to either of the two `3.3V` pins on the Raspberry Pi

**Day 2 LED Bar Graph**

  **1.** Place the Bar Graph on a breadboard and locate the side with the label. Connect all the pins on the same side of the label to `220 Ohm` resistors. Then connect those resistors to any of the `3.3V` pins on the Raspberry Pi.

  **2.** With the module placed on a breadboard with the lable side down "facing you" from left to right connect the far left pin to `GPIO 17` on the Raspberry Pi. Physical Pin `11`

  **3.** Connect the next pin to `GPIO 18`, physical pin `12`. From left to right after that connect each of the pins to the fallowing respectivly, `GPIO 27`, `GPIO 22`, `GPIO 23`, `GPIO 24`, `GPIO 25`, `GPIO 2`, `GPIO 3`, `GPIO 8`.

**Day 3 7-Segment Display**

  **1.** Collect the segment display and a 74HC595 IC chip. Place them on the breadboard so that the labels are facing you and are not upside down. You should be able to read them clearly. With the IC chip position so you can read the lable on it, we can begin wiring that. 

  **2.** From left to right connect the far left pin to a `3.3V` pin on the Raspberry Pi. **WARNING: DO NOT PLACE IC CHIP UPSIDE DOWN!! (I've had breadboards melt because of that mistake) If you need help ask me, I will provide you with pictures to help guide you**

  **3.** Connect the next pin on the IC Chip to the top pin second from the right on the segment display.

  **4.** Connect the next pin on the IC Chip to `GPIO 17` on the Raspberry Pi. Physical Pin `11`

  **5.** Connect the next pin after that to any `GND` pin on the Raspberry Pi.

  **6.** Connect the next one to `GPIO 18` on the Raspberry Pi.

  **7.** Connect the next pin to `GPIO 27` on the Raspberry Pi.

  **8.** Connect the one after that to the far left pin on the IC Chip. Nothing will be connected to the last pin on the top

  **9.** On the botton of the IC Chip, the bottom left to the bottom right, connect the far left pin to the top far right on the segment display.

  **10.** Connect the one after that to the bottom second one from the right on the display.

  **11.** The next one will go to the bottom second from the left on the display.

  **12.** The one after that will go to the bottom far left pin on the display.

  **13.** Next one will go to the top second one from the left.

  **14.** Then the next pin on the IC Chip will connect to the top far left on the segment display.

  **15.** The next one going to the bottom far right on the segment display. With the last one going to any `GND` pin on the Raspberry Pi.

  **16.** Connect the bottom middle pin on the segment display to a `220 Ohm` resistor which will connect to any `GND` pin on the Raspberry Pi.

**Day 4 4-Digit 7-Segment Display**

  **1.** I fell like this one is redundent and is practically the same thing as the last one. I'm going to skip this one for you all to fingure out.

**Day 5 MAX7219 8x8 Matrix Display**

 **1.** Connect the `VCC` pin on the Module to any of the two `5.0V` pins on the Raspberry Pi.

 **2.** Connect the `GND` pin on the Module to any of the `GND` pins on the Raspberry Pi.

 **3.** Connect the `DIN` pin on the Module to `GPIO 10`, Physical Pin `19` on the Raspberry Pi.

 **4.** Connect the `CS` pin on the Module to `GPIO 8`, Physical Pin `24` on the Raspberry Pi.

 **5.** Connect the `CLK` pin on the Module to `GPIO 11`, Physical Pin `23` on the Raspberry Pi.

**Day 6 I2C LCD1602**

 **1.** Connect the `GND` and `VCC` pins on the Module to the `GND` and `5V` pins on the Raspberry Pi Respectivly.

 **2.** Connect the `SDA` and `SCL` pins on the Module to the `SDA` and `SCL` pins on the Raspberry Pi Respectivly.

**Day 7/8 Buzzer**

 **1.** Place the `S8550 PNP Transistor` and Buzzer on a breadboard with the flat side of the transistor facing you.

 **2.** With the flat side of the transistor facing you, connect the far left pin to the negative pin on the buzzer.

 **3.** Connect the middle pin of the transistor to a `1K Ohm` resistor, which will then connect to `GPIO 4` on the Raspberry Pi.

 **4.** Connect the far right pin on the transistor to any `GND` pin on the Raspberry Pi.

 **5.** Connect the positive side of the buzzer to any `3V3` pins on the Raspberry Pi.

**Day 9 Motor** 

 **1.** Grab a breadboard power supply and connect is so it's outputting 5 volts. Orientate the breadboard so that the power supply is on the right hand side. 

 **2.** Place your L293D IC Chip so that the lable is readable to you. **WARNING: DO NOT PLACE UPSIDE DOWN. IF YOU NEED HELP, ASK ME PLEASE!** Connect the top far left pin on the chip to the voltage rail coming from the breadboard power supply.

 **3.** Connect the bottom far left pin on the IC Chip to `GPIO 5` on the Raspberry Pi.

 **4.** Connect the one next to that pin to `GPIO 6` on the Raspberry Pi.

 **5.** Connect the next one to either the positive or negative side on the DC motor.

 **6.** Connect the next two pins on the IC Chip to a `GND` pin on the Raspberry Pi and the ground pin on the breadboard power supply.

 **7.** Connect the next pin on the IC Chip to the other pin on the DC motor. 

 **8.** Connect the pin next to that one to `GPIO 13` on the Raspberry Pi.

 **9.** Connect the last pin to the voltage rail on the breadboard power supply.

**Day 10 Servo Motor**

 **1.** Connect the Brown wire to any `GND` on the Raspberry Pi.

 **2.** Connect the Red wire to a `3V3` pin on the Raspberry Pi.

 **3.** Connect the Orange wire to `GPIO 18` on the Raspberry Pi.

**Day 11**



**Day 12**



**Day 13**



**Day 14**



**Day 15**



**Day 16**



**Day 17**



**Day 18**



**Day 19**



**Day 20**



**Day 21**



**Day 22**



**Day 23**



**Day 24**



**Day 25**



**Day 26**



**Day 27**



**Day 28**



**Day 29**



**Day 29**


