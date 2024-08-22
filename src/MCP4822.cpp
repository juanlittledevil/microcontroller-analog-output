#include "MCP4822.h"
MCP4822::MCP4822(uint8_t cs_pin, uint8_t sck_pin, uint8_t mosi_pin)
  : cs_pin_(cs_pin), sck_pin_(sck_pin), mosi_pin_(mosi_pin), gain_(GAIN_1X) {}

MCP4822::~MCP4822() {}

void MCP4822::Init() {
    pinMode(cs_pin_, OUTPUT);
    pinMode(sck_pin_, OUTPUT);
    pinMode(mosi_pin_, OUTPUT);
    digitalWrite(cs_pin_, HIGH);
}

void MCP4822::SetGain(Gain gain) {
    gain_ = gain;
}

void MCP4822::Write(uint8_t channel, uint16_t value) {
    // the following line of code creates a 16-bit command word by combining the channel, gain, and value
    // uint16_t command = (0x3000 | (channel << 15) | (gain_ << 13) | (value & 0x0FFF));

    // Create a 16-bit command word by explicitly setting each bit
    uint16_t command = 0;
    command |= (channel << 15); // Set the channel bit (bit 15)
    command |= (0 << 14); // Set the unused bit to 0 (bit 14)
    command |= (gain_ << 13); // Set the gain bit (bit 13)
    command |= (1 << 12); // Set the shutdown bit to 1 (bit 12)
    command |= (value & 0x0FFF); // Set the value bits (bits 0-11)

    // First, we need to select the chip by setting the CS pin low
    digitalWrite(cs_pin_, LOW);

    // Next, we send the command to the DAC
    SendData(command);

    // Finally, we deselect the chip by setting the CS pin high
    digitalWrite(cs_pin_, HIGH);
}

void MCP4822::SendData(uint16_t data) {
    // We need to send the data to the DAC one bit at a time
    for (int i = 15; i >= 0; i--) {
        // We send the data MSB first
        digitalWrite(sck_pin_, LOW);

        // We use a bitwise operation to check if the i-th bit is set
        digitalWrite(mosi_pin_, (data & (1 << i)) ? HIGH : LOW);

        // We toggle the clock pin to send the data
        digitalWrite(sck_pin_, HIGH);
    }
}