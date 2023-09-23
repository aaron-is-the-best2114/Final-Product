import time
import board
import neopixel

# Set the number of LEDs in your light ring
num_leds = 30

# Set the pin connected to the light ring
led_pin = board.D18

# Create a NeoPixel object
pixels = neopixel.NeoPixel(led_pin, num_leds)

# Define the colors to use
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Set the delay between color changes (in seconds)
delay = 0.5

# Set the number of steps for each color transition
steps = 100

while True:
    # Loop through each color
    for i in range(len(colors)):
        # Get the current and next color
        current_color = colors[i]
        next_color = colors[(i + 1) % len(colors)]
        
        # Calculate the color change for each step
        r_step = (next_color[0] - current_color[0]) / steps
        g_step = (next_color[1] - current_color[1]) / steps
        b_step = (next_color[2] - current_color[2]) / steps
        
        # Gradually change the color of each LED
        for j in range(steps):
            r = int(current_color[0] + r_step * j)
            g = int(current_color[1] + g_step * j)
            b = int(current_color[2] + b_step * j)
            pixels.fill((r, g, b))
            time.sleep(delay / steps)