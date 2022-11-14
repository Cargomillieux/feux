def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
    
    while input.button_is_pressed(Button.A):
        pins.digital_write_pin(DigitalPin.P2, 01
        
basic.forever(on_forever)
