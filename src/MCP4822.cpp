#include "MCP4822.h"

MCP4822::MCP4822(uint8_t cs_pin)
  : cs_pin_(cs_pin), gain_(GAIN_1X) {}

MCP4822::~MCP4822() {}

void MCP4822::Init() {
    pinMode(cs_pin_, OUTPUT);
    digitalWrite(cs_pin_, HIGH);
    SPI.begin();
}

void MCP4822::SetGain(Gain gain) {
    gain_ = gain;
}

void MCP4822::Write(uint8_t channel, uint16_t value) {
    uint16_t command = 0;
    command |= (channel << 15); // Set the channel bit (bit 15)
    command |= (0 << 14); // Set the unused bit to 0 (bit 14)
    command |= (gain_ << 13); // Set the gain bit (bit 13)
    command |= (1 << 12); // Set the shutdown bit to 1 (bit 12)
    command |= (value & 0x0FFF); // Set the value bits (bits 0-11)

    digitalWrite(cs_pin_, LOW);
    SPI.transfer16(command);
    digitalWrite(cs_pin_, HIGH);
}