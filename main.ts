basic.forever(function on_forever() {
    pins.digitalWritePin(DigitalPin.P0, 1)
    while (input.buttonIsPressed(Button.A)) {
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
})
