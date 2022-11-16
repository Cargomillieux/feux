//  Vert = P0
//  Jaune = P1
//  Rouge = P2
//  LED Jaune = P8
//  LED Blanc = P16
basic.forever(function on_forever() {
    pins.digitalWritePin(DigitalPin.P0, 1)
    pins.digitalWritePin(DigitalPin.P1, 0)
    if (input.buttonIsPressed(Button.A)) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        while (basic.pause(500)) {
            pins.digitalWritePin(DigitalPin.P1, 1)
            pins.digitalWritePin(DigitalPin.P0, 0)
        }
        while (basic.pause(500)) {
            pins.digitalWritePin(DigitalPin.P1, 0)
        }
    }
    
})
