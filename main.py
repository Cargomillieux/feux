# Vert = P0
# Jaune = P1
# Rouge = P2
# LED Jaune = P8
# LED Blanc = P16

#cycle pieton
def cycle_pieton():
    pins.digital_write_pin(DigitalPin.P0, 1)#v
    pins.digital_write_pin(DigitalPin.P2, 0)#r
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P1, 1)#j
    pins.digital_write_pin(DigitalPin.P0, 0)#v
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P1, 0)#j
    pins.digital_write_pin(DigitalPin.P2, 1)#r
    pins.digital_write_pin(DigitalPin.P0, 0)#v
    pins.digital_write_pin(DigitalPin.P16, 1)#b
    basic.pause(3000)
    pins.digital_write_pin(DigitalPin.P16, 0)#b
    pins.digital_write_pin(DigitalPin.P8, 1)#jl
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P8, 0)#jl
    pins.digital_write_pin(DigitalPin.P2, 0)#r


#cycle normale 
def cycle():
    pins.digital_write_pin(DigitalPin.P0, 1)
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    pins.digital_write_pin(DigitalPin.P1, 0)
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    pins.digital_write_pin(DigitalPin.P2, 0)
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    basic.pause(1000)
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    pins.digital_write_pin(DigitalPin.P0, 0)#v
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    pins.digital_write_pin(DigitalPin.P1, 1)#J
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    pins.digital_write_pin(DigitalPin.P2, 0)#r
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    basic.pause(1000)
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    pins.digital_write_pin(DigitalPin.P2, 1)#r
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    pins.digital_write_pin(DigitalPin.P1, 0)#j
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    pins.digital_write_pin(DigitalPin.P0, 0)#v
    if input.button_is_pressed(Button.A):
            cycle_pieton()
    basic.pause(1000)
    if input.button_is_pressed(Button.A):
            cycle_pieton()
        
    
def on_forever():
    cycle()
    if input.button_is_pressed(Button.A):
        cycle_pieton()
    

    


basic.forever(on_forever)
