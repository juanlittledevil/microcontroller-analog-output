#ifndef WAVE_GENERATOR_H_
#define WAVE_GENERATOR_H_

#include <Arduino.h>
#include <cmath> // Include cmath for sin function

class WaveGenerator {
 public:
  WaveGenerator(int tableSize, int sampleRate, float frequency);
  ~WaveGenerator();

  void init();
  uint16_t getSample();
  void setFrequency(float frequency);
  int getSampleRate() const;
  float getPhaseIncrement() const;

 private:
  int tableSize_;
  int sampleRate_;
  float frequency_;
  float currentIndex_;
  float phaseIncrement_;
};
#endif  // WAVE_GENERATOR_H_