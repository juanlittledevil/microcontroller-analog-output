#include <Arduino.h>
#include "PWMDac.h"
#include "MCP4822.h"
#include "WaveGenerator.h" // Include the WaveGenerator header

// Define the pins for each PWM channel
#define CH1_PWM1 PA0
#define CH1_PWM2 PA1
#define CH2_PWM1 PA2
#define CH2_PWM2 PA3
#define PWM_TIMER TIM2

// Define pins for the MCP4822 DAC
#define DAC_CS PB10
#define DAC_SCK PA5
#define DAC_MOSI PA7

// Define Frequency knob
#define FREQ_KNOB PB1

// Define constants
const int TABLE_SIZE = 2048; // Updated table size
const int SAMPLE_RATE = 96000;
const float FREQUENCY = 2000.0;

// Create a PWMDac object for each combination of timer and pins
PWMDac pwm_dac(PWM_TIMER, CH1_PWM1, CH1_PWM2, CH2_PWM1, CH2_PWM2);

// Create an MCP4822 object for the DAC
MCP4822 dac(DAC_CS, DAC_SCK, DAC_MOSI);

// Create an instance of WaveGenerator
WaveGenerator waveGen(TABLE_SIZE, SAMPLE_RATE, FREQUENCY);

// Variables to track time for sample updates
unsigned long lastSampleTime = 0;
unsigned long sampleInterval;

TIM_HandleTypeDef htim2;

void setup() {
  // Initialize the serial monitor
  delay(1000);
  Serial.begin(115200);
  delay(1000);
  Serial.println("Wave Generator Test");

  // Initialize each PWMDac object
  pwm_dac.Init();

  // Initialize the MCP4822 DAC
  dac.Init();

  // Set the gain for the DAC
  dac.SetGain(MCP4822::GAIN_2X);

  // Initialize the frequency knob
  pinMode(FREQ_KNOB, INPUT);

  // Initialize the WaveGenerator and generate the table map
  waveGen.init();

  // Calculate the sample interval based on the sample rate
  sampleInterval = 1000000 / waveGen.getSampleRate();
  Serial.println("WaveGenerator initialized.");

  // Initialize TIM2
  __HAL_RCC_TIM2_CLK_ENABLE();

  htim2.Instance = TIM2;
  htim2.Init.Prescaler = 72 - 1; // Assuming 72 MHz clock, prescaler to 1 MHz
  htim2.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim2.Init.Period = 100 - 1; // 10 kHz update rate
  htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  HAL_TIM_Base_Init(&htim2);

  HAL_TIM_Base_Start_IT(&htim2);

  HAL_NVIC_SetPriority(TIM2_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(TIM2_IRQn);
}

void loop() {
  // Read the knob value (10-bit ADC value)
  int knobValue = analogRead(FREQ_KNOB);

  // Map the knob value to the frequency range (e.g., .1 Hz to 1500 Hz)
  float frequency = map(knobValue, 0, 1023, 1, 20000);
  waveGen.setFrequency(frequency);

  // Print debug information
  Serial.print("Frequency: ");
  Serial.println(frequency);
  Serial.print("Sample Interval: ");
  Serial.println(sampleInterval);
  Serial.print("Phase Increment: ");
  Serial.println(waveGen.getPhaseIncrement());


  // Map the knob value to the 12-bit DAC range (0-4095)
  uint16_t dacValue = map(knobValue, 0, 1023, 0, 4095);
  uint16_t pwmValue = map(knobValue, 0, 1023, 0, 16383);
  dac.Write(1, dacValue);
  pwm_dac.Write(1, pwmValue);
}

//   // Check if it's time to update the sample
//   unsigned long currentTime = micros();
//   if (currentTime - lastSampleTime >= sampleInterval) {
//     lastSampleTime = currentTime;

//     // Get the waveform sample from the WaveGenerator
//     uint16_t sample = waveGen.getSample();

//     // Write the mapped values to the DAC and PWM DAC
//     dac.Write(0, sample);
//     pwm_dac.Write(0, map(sample, 0, 4095, 0, 16383));
//   }
// }

// TIM2 interrupt handler
extern "C" void TIM2_IRQHandler(void) {
  if (__HAL_TIM_GET_FLAG(&htim2, TIM_FLAG_UPDATE) != RESET) {
    if (__HAL_TIM_GET_IT_SOURCE(&htim2, TIM_IT_UPDATE) != RESET) {
      __HAL_TIM_CLEAR_IT(&htim2, TIM_IT_UPDATE);

      // Get the waveform sample from the WaveGenerator
      uint16_t sample = waveGen.getSample();

      // Write the mapped values to the DAC and PWM DAC
      dac.Write(0, sample);
      pwm_dac.Write(0, map(sample, 0, 4095, 0, 16383));
    }
  }
}