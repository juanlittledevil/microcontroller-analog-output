#ifndef PWM_DAC_H_
#define PWM_DAC_H_

#include <Arduino.h>

const uint32_t kPwmFrequency = 125000;
const uint16_t kPwmResolution = 7; // bits

class PWMDac {
 public:
  PWMDac(TIM_TypeDef* timer, uint8_t pin1, uint8_t pin2, uint8_t pin3, uint8_t pin4);
  ~PWMDac();

  void Init();
  void Write(int index, uint16_t value);

 private:
  HardwareTimer* timer_;
  uint8_t pin1_, pin2_, pin3_, pin4_;
  uint16_t data_[2];
};

#endif  // PWM_DAC_H_