#include "WaveGenerator.h"

WaveGenerator::WaveGenerator(int tableSize, int sampleRate, float frequency)
    : tableSize_(tableSize), sampleRate_(sampleRate), frequency_(frequency), currentIndex_(0.0) {
  phaseIncrement_ = (2.0 * M_PI * frequency_) / sampleRate_;
}

WaveGenerator::~WaveGenerator() {}

void WaveGenerator::init() {}

uint16_t WaveGenerator::getSample() {
  // Generate a sine wave sample in real-time
  float sample = sin(currentIndex_);
  currentIndex_ += phaseIncrement_;
  if (currentIndex_ >= 2.0 * M_PI) {
    currentIndex_ -= 2.0 * M_PI;
  }
  // Convert the sample to a 12-bit value (0-4095)
  uint16_t outputSample = static_cast<uint16_t>((sample + 1.0) * 2047.5);
  return outputSample;
}

void WaveGenerator::setFrequency(float frequency) {
  frequency_ = frequency;
  phaseIncrement_ = (2.0 * M_PI * frequency_) / sampleRate_;
}

int WaveGenerator::getSampleRate() const {
  return sampleRate_;
}

float WaveGenerator::getPhaseIncrement() const {
  return phaseIncrement_;
}