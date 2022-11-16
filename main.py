# Vert = P0
# Jaune = P1
# Rouge = P2
# LED Jaune = P8
# LED Blanc = P16
def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    if input.button_is_pressed(Button.A):
        pins.digital_write_pin(DigitalPin.P0, 1)

        while basic.pause(500):
            pins.digital_write_pin(DigitalPin.P1, 1)
            pins.digital_write_pin(DigitalPin.P0, 0)
        while basic.pause(500):
            pins.digital_write_pin(DigitalPin.P1, 0)

basic.forever(on_forever)
