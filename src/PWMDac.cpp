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

  // Initialize the TIMER for interrupt
  TIMER_Init();

  // Debugging output to verify configuration.
  Serial.print("Prescale Factor: ");
  Serial.println(timer_->getPrescaleFactor());
  Serial.print("Overflow: ");
  Serial.println(timer_->getOverflow(HERTZ_FORMAT));
  Serial.print("Timer Clock Frequency: ");
  Serial.println(timer_->getTimerClkFreq());
  Serial.println("PWM DAC initialized.");
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

void PWMDac::TIMER_Init() {
  // Enable the timer clock based on the timer instance.
  switch (reinterpret_cast<uintptr_t>(timerInstance_)) {
    case TIM2_BASE:
      __HAL_RCC_TIM2_CLK_ENABLE();
      break;
    case TIM3_BASE:
      __HAL_RCC_TIM3_CLK_ENABLE();
      break;
    case TIM1_BASE:
      __HAL_RCC_TIM1_CLK_ENABLE();
      break;
    // Add more cases as needed for other timers.
    default:
      // Handle error or unsupported timer.
      return;
  }

  TIM_HandleTypeDef htim;
  htim.Instance = timerInstance_;
  htim.Init.Prescaler = 72 - 1; // Assuming 72 MHz clock, prescaler to 1 MHz
  htim.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim.Init.Period = 100 - 1; // 10 kHz update rate
  htim.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  HAL_TIM_Base_Init(&htim);

  HAL_TIM_Base_Start_IT(&htim);

  // Set the priority and enable the IRQ based on the timer instance.
  IRQn_Type irq;
  switch (reinterpret_cast<uintptr_t>(timerInstance_)) {
    case TIM2_BASE:
      irq = TIM2_IRQn;
      break;
    case TIM3_BASE:
      irq = TIM3_IRQn;
      break;
    case TIM1_BASE:
      irq = TIM1_UP_IRQn;
      break;
    // Add more cases as needed for other timers.
    default:
      // Handle error or unsupported timer.
      return;
  }

  HAL_NVIC_SetPriority(irq, 0, 0);
  HAL_NVIC_EnableIRQ(irq);
}