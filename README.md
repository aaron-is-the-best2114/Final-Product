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

  **1.** 
