# How to use this repo:

I created this repo as a reference for anyone interested in exploring Control Voltage suited for Eurorack out of a Microcontroller. The code explores 3 things:

1. Wave Generation - Simple sine wave generation.
2. Analog Output using a hardware DAC, specifically the MCP4822.
3. Analog Output using PWM, specifically a technique called HiFi mode or dual PWM that combines two PWM pins to increase the resolution of the output signal.

Why? Because why not? - Here is the thing. DACs are not cheap, the MCP4822 is only 12-bit resolution which isn't great for audio but good enough for CV. While it is pricey, it does provide a ridiculously simple circuit to implement.
But if cost is a factor, we can still get away with a fairly good output using PWM. The HiFi mode is capable of producing a 14-bit output which is better than the DAC, however, it utilizes quite a bit more components. This is because in addition to adding filters to convert the PWM output to a smooth analog signal, we also need to add additional filter stages to ensure that noise doesn't make it to the signal path. After all, we are converting a high-frequency signal PWM to analog and we need to make sure that the output doesn't include this carrier signal (PWM).

Make sure to check out my YouTube channel and blog (www.scruffycatstudios.com) for the post relating to this topic.

https://youtu.be/BtJqGxOrmBY

If you want to follow along you'll need:

1. Visual Studio Code. I am very much not a fan of the Arduino IDE so all my examples are done in VSCode and PlatformIO.
2. PlatformIO. Nuff said.
3. BluePill STM32F103C6T6. I used the smaller C6T6 for this example but if you want to try it with another microcontroller you'll need to update the platformio.ini file with the correct board.
4. Arduino Framework. While I absolutely detest the Arduino IDE, I rather like the Arduino Framework so, yes, this code was done with that framework and not the STM32Cube which I'm also not a fan of the IDE.

OK, so here are a few things to check out:

I've split this code into 3 versions with corresponding branches so all you need to do is switch branches to compare.

**main branch**: this branch explores wave generationm using a value map which is populated at startup. The MCP4822 is writen manually without use of external libraries.

**spi-library**: this is the same as the main branch, but using the SPI library with the MCP4822 object. Notice how much simpler the code is thanks to the library.

**accurate-but-cpu-hungry**: This is the same as spi-library, however, in this version instead of using a value map, we calculate the samples in realtime. Notice how the BluePill is actually keeping up. Sorta, as we increasee the sample rate the output frequency is decreased, this is because calculation takes longer thus it isn't capable of keeping up.

---

**DISCLAIMER:** I realize that there are probably way better ways of doing what is in this repo. This is only intended to spark curiosity and help you get started with your own experiments. So go play with this and share your findings with all of us ya!?