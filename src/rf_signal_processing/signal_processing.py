import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# Load audio file (WAV)
def load_audio(wav_path):
    sample_rate, data = wavfile.read(wav_path)
    print(f"Sample Rate: {sample_rate}, Data Shape: {data.shape}")
    return sample_rate, data

# Normalize the signal before filtering (helps prevent zero values after filtering)
def normalize_signal(data):
    max_val = np.max(np.abs(data))
    if max_val > 0:
        return data / max_val
    return data

# Envelope detection: Absolute value of the signal, followed by low-pass filtering
def envelope_detection(rf_data, cutoff, fs):
    return lowpass_filter(np.abs(rf_data), cutoff, fs)

# Simple thresholding to convert amplitudes to binary values (0 and 1) using dynamic threshold
def demodulate_ask(rf_data, threshold_factor=0.2):  
    threshold = np.mean(np.abs(rf_data)) * threshold_factor
    print(f"Dynamic Threshold: {threshold}")
    return np.where(rf_data > threshold, 1, 0)

# Low-pass filter to clean up the signal
def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# Apply the low-pass filter
def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order)
    return lfilter(b, a, data)

# Visualize raw and filtered signal
def visualize_signals(raw_signal, envelope_signal, sample_rate):
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.title("Raw Signal (First 500 samples)")
    plt.plot(raw_signal[:500])  # Plot only the first 500 samples for clarity
    
    plt.subplot(2, 1, 2)
    plt.title("Envelope Detected Signal (First 500 samples)")
    plt.plot(envelope_signal[:500])  # Plot only the first 500 samples for clarity

    plt.tight_layout()
    plt.show()

# Main function to decode RF signal from audio
def decode_rf_signal(wav_path):
    # Load the audio file
    sample_rate, rf_data = load_audio(wav_path)
    
    # Normalize the signal before filtering
    rf_data = normalize_signal(rf_data)
    
    # Apply envelope detection to extract signal amplitude variations
    filtered_signal = envelope_detection(rf_data, cutoff=1000, fs=sample_rate)
    
    # Visualize the signals to inspect them
    visualize_signals(rf_data, filtered_signal, sample_rate)
    
    # Decode the RF signal using ASK (Amplitude Shift Keying) with dynamic thresholding
    binary_signal = demodulate_ask(filtered_signal, threshold_factor=0.1)

    # Optionally, plot the binary signal for debugging
    plt.figure(figsize=(10, 6))
    plt.title("Binary Signal (First 500 samples)")
    plt.plot(binary_signal[:500])  # Plot only the first 500 samples for clarity
    plt.show()

    # Return the binary signal
    return binary_signal


