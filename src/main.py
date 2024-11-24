import argparse
from audio_transcription.transcription import transcribe_audio
from rf_signal_processing.signal_processing import decode_rf_signal

def main():
    parser = argparse.ArgumentParser(description="Process 433 MHz audio signal and perform transcription.")
    parser.add_argument('--audio_file', type=str, required=True, help="Path to the audio file (WAV format).")
    parser.add_argument('--action', type=str, required=True, help="Use 't' for transcription or 'd' to process 433 MHz audio signal.")
    
    
    args = parser.parse_args()
    
    if args.action == "t":
        # Step 1: Transcribe audio to text
        print(f"Transcribing audio from {args.audio_file}...")
        transcription = transcribe_audio(args.audio_file)
        print(f"Transcription: \n{transcription}")
    
    if args.action == "d":
        # Step 2: Decode the RF signal (extract binary data)
        print(f"Decoding RF signal from {args.audio_file}...")
        binary_signal = decode_rf_signal(args.audio_file)
        print(f"Decoded binary signal: {binary_signal[:100]}")  # Show the first 100 binary values

if __name__ == "__main__":
    main()