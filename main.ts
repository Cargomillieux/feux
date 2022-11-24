//  Vert = P0
//  Jaune = P1
//  Rouge = P2
//  LED Jaune = P8
//  LED Blanc = P16
// cycle pieton
function cycle_pieton() {
    pins.digitalWritePin(DigitalPin.P0, 1)
    // v
    pins.digitalWritePin(DigitalPin.P2, 0)
    // r
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P1, 1)
    // j
    pins.digitalWritePin(DigitalPin.P0, 0)
    // v
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P1, 0)
    // j
    pins.digitalWritePin(DigitalPin.P2, 1)
    // r
    pins.digitalWritePin(DigitalPin.P0, 0)
    // v
    pins.digitalWritePin(DigitalPin.P16, 1)
    // b
    basic.pause(3000)
    pins.digitalWritePin(DigitalPin.P16, 0)
    // b
    pins.digitalWritePin(DigitalPin.P8, 1)
    // jl
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P8, 0)
    // jl
    pins.digitalWritePin(DigitalPin.P2, 0)
}

// r
// cycle normale 
function cycle() {
    pins.digitalWritePin(DigitalPin.P0, 1)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 0)
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P0, 0)
    // v
    pins.digitalWritePin(DigitalPin.P1, 1)
    // J
    pins.digitalWritePin(DigitalPin.P2, 0)
    // r
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P2, 1)
    // r
    pins.digitalWritePin(DigitalPin.P1, 0)
    // j
    pins.digitalWritePin(DigitalPin.P0, 0)
    // v
    basic.pause(1000)
}

basic.forever(function on_forever() {
    while (input.buttonIsPressed(Button.A)) {
        cycle()
    }
    cycle_pieton()
})
