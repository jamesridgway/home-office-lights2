# Home Office Lights (V2)
I have [WS2812b LED strip in my home office](https://www.jamesridgway.co.uk/using-a-raspberry-pi-to-make-my-office-desk-glow/) that is controlled by a Raspberry Pi.

This codebase aims to replace [the original codebase](https://github.com/jamesridgway/home-office-lights) I wrote which had several limitations. Ultimately, the LED strip did not present itself to Home Assistant as a Device or Entity, which limitated the ways I could use the LED strip within Home Assistant.

This codebase addresses all of these limitations by providing a series of APIs that can be consumed through a light template. You can read about this in more detail here.

![RGB Office Light strip](https://www.jamesridgway.co.uk/content/images/size/w2000/2020/10/desk-lights-orange.png)
