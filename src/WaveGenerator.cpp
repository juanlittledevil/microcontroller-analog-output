#include "WaveGenerator.h"
#include <cmath>

WaveGenerator::WaveGenerator(int tableSize, int sampleRate, float frequency)
  : tableSize_(tableSize), sampleRate_(sampleRate), frequency_(frequency), currentIndex_(0) {
  waveTable_ = new uint16_t[tableSize_];
  setFrequency(frequency);
}

WaveGenerator::~WaveGenerator() {
  delete[] waveTable_;
}

void WaveGenerator::init() {
  // Generate a simple sine wave table
  for (int i = 0; i < tableSize_; ++i) {
    waveTable_[i] = (uint16_t)((sin(2 * PI * i / tableSize_) + 1) * 2047.5); // 12-bit range (0-4095)
  }
}

// // Linear interpolation Method
// uint16_t WaveGenerator::getSample() {
//   // Calculate the fractional index
//   float fractionalIndex = currentIndex_ + phaseIncrement_;
//   if (fractionalIndex >= tableSize_) {
//     fractionalIndex -= tableSize_;
//   }
//   int index1 = (int)fractionalIndex;
//   int index2 = (index1 + 1) % tableSize_;
//   float fraction = fractionalIndex - index1;

//   // Perform linear interpolation
//   uint16_t sample1 = waveTable_[index1];
//   uint16_t sample2 = waveTable_[index2];
//   uint16_t interpolatedSample = sample1 + fraction * (sample2 - sample1);

//   // Update the current index
//   currentIndex_ = fractionalIndex;

//   return interpolatedSample;
// }

// Cubic interpolation Method
uint16_t WaveGenerator::getSample() {
  // Calculate the fractional index
  float fractionalIndex = currentIndex_ + phaseIncrement_;
  if (fractionalIndex >= tableSize_) {
    fractionalIndex -= tableSize_;
  }
  int index1 = (int)fractionalIndex;
  int index0 = (index1 - 1 + tableSize_) % tableSize_;
  int index2 = (index1 + 1) % tableSize_;
  int index3 = (index1 + 2) % tableSize_;
  float fraction = fractionalIndex - index1;

  // Perform cubic interpolation
  uint16_t sample0 = waveTable_[index0];
  uint16_t sample1 = waveTable_[index1];
  uint16_t sample2 = waveTable_[index2];
  uint16_t sample3 = waveTable_[index3];

  float a0 = sample3 - sample2 - sample0 + sample1;
  float a1 = sample0 - sample1 - a0;
  float a2 = sample2 - sample0;
  float a3 = sample1;

  uint16_t interpolatedSample = (uint16_t)(a0 * fraction * fraction * fraction + a1 * fraction * fraction + a2 * fraction + a3);

  // Update the current index
  currentIndex_ = fractionalIndex;

  return interpolatedSample;
}

void WaveGenerator::setFrequency(float frequency) {
  frequency_ = frequency;
  phaseIncrement_ = (float)tableSize_ * frequency_ / sampleRate_;
}

int WaveGenerator::getSampleRate() const {
  return sampleRate_;
}