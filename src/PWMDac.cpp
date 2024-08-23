#include "PWMDac.h"

PWMDac::PWMDac(TIM_TypeDef* timer, uint8_t pin1, uint8_t pin2, uint8_t pin3, uint8_t pin4) 
  : timer_(new HardwareTimer(timer)),
    pin1_(pin1),
    pin2_(pin2),
    pin3_(pin3),
    pin4_(pin4),
    timerInstance_(timer)
    { }

PWMDac::~PWMDac() {
  delete timer_;
}

void PWMDac::Init() {
  // Initialize pins.
  pinMode(pin1_, OUTPUT);
  pinMode(pin2_, OUTPUT);
  pinMode(pin3_, OUTPUT);
  pinMode(pin4_, OUTPUT);

  // Pause the timer before configuration.
  timer_->pause();

  // Set the prescaler to 1.
  timer_->setPrescaleFactor(1);

  // Set the PWM mode for each channel.
  timer_->setMode(1, TIMER_OUTPUT_COMPARE_PWM1, pin1_);
  timer_->setMode(2, TIMER_OUTPUT_COMPARE_PWM1, pin2_);
  timer_->setMode(3, TIMER_OUTPUT_COMPARE_PWM1, pin3_);
  timer_->setMode(4, TIMER_OUTPUT_COMPARE_PWM1, pin4_);

  // Set the overflow value to achieve 125 kHz PWM frequency.
  timer_->setOverflow(kPwmFrequency, HERTZ_FORMAT);

  // Set the PWM frequency.
  analogWriteFrequency(timer_->getOverflow(HERTZ_FORMAT));

  // Refresh the timer settings.
  timer_->refresh();

  // Resume the timer to start PWM.
  timer_->resume();
}

void PWMDac::Write(int index, uint16_t value) {
  data_[index] = value;

  if (index == 0) {
    analogWrite(pin1_, data_[0] >> 9);
    uint8_t l_byte1 = (data_[0] & 0x1FC) >> 2;
    analogWrite(pin2_, l_byte1);
  } else if (index == 1) {
    analogWrite(pin3_, data_[1] >> 9);
    uint8_t l_byte2 = (data_[1] & 0x1FC) >> 2;
    analogWrite(pin4_, l_byte2);
  }
}