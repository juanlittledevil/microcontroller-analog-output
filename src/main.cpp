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
const int TABLE_SIZE = 2048;
const int SAMPLE_RATE = 96000;
// const int SAMPLE_RATE = 44100;
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
unsigned long sampleCount = 0;

float mapFloat(float x, float in_min, float in_max, float out_min, float out_max);

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
  // sampleInterval = 1000000 / waveGen.getSampleRate();
  sampleInterval = 1000000 / SAMPLE_RATE;
  Serial.println("WaveGenerator initialized.");
}

void loop() {
  // Read the knob value (10-bit ADC value)
  int knobValue = analogRead(FREQ_KNOB);

  // Map the knob value to the frequency range (e.g., .1 Hz to 500 Hz)
  // float frequency = map(knobValue, 0, 1023, .1, 5000);
  float frequency = mapFloat(knobValue, 0, 1023, 0.1, 5000.0);
  waveGen.setFrequency(frequency);

  // Calculate the sample interval based on the frequency
  sampleInterval = 1000000 / frequency; // in microseconds

  // Debugging information
  Serial.print("Knob Value: ");
  Serial.println(knobValue);
  Serial.print("Frequency: ");
  Serial.println(frequency);
  Serial.print("Sample Interval: ");
  Serial.println(sampleInterval);

  // Additional debugging to check the timing
  unsigned long startTime = micros();
  delayMicroseconds(sampleInterval);
  unsigned long endTime = micros();
  Serial.print("Actual Interval: ");
  Serial.println(endTime - startTime);

  // Map the knob value to the 12-bit DAC range (0-4095)
  uint16_t dacValue = map(knobValue, 0, 1023, 0, 4095);
  uint16_t pwmValue = map(knobValue, 0, 1023, 0, 16383);
  dac.Write(1, dacValue);
  pwm_dac.Write(1, pwmValue);

  // Check if it's time to update the sample
  unsigned long currentTime = micros();
  if (currentTime - lastSampleTime >= sampleInterval) {
    lastSampleTime += sampleInterval;

    sampleCount++;
    Serial.print("Sample Count: ");
    Serial.println(sampleCount);
    Serial.print("Current Time: ");
    Serial.println(currentTime);

    // Get the waveform sample from the WaveGenerator
    uint16_t sample = waveGen.getSample();

    // Debugging information
    Serial.print("Sample: ");
    Serial.println(sample);


    // Write the mapped values to the DAC and PWM DAC
    dac.Write(0, sample);
    pwm_dac.Write(0, map(sample, 0, 4095, 0, 16383));
  }
}

float mapFloat(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}