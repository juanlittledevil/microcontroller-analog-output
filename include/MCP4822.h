#ifndef MCP4822_H_
#define MCP4822_H_

#include <Arduino.h>

class MCP4822 {
 public:
  enum Gain {
    GAIN_2X = 0,
    GAIN_1X = 1
  };

  MCP4822(uint8_t cs_pin, uint8_t sck_pin, uint8_t mosi_pin);
  ~MCP4822();

  void Init();
  void Write(uint8_t channel, uint16_t value);
  void SetGain(Gain gain);

 private:
  uint8_t cs_pin_;
  uint8_t sck_pin_;
  uint8_t mosi_pin_;
  Gain gain_;

  void SendData(uint16_t data);
};

#endif  // MCP4822_H_