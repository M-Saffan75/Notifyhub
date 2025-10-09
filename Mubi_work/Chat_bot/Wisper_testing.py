# whisper_test.py
import whisper
import speech_recognition as sr
import tempfile, os, time

# Model select: small / medium / large
MODEL_NAME = "tiny"   # better balance for speed+accuracy

def record_audio(max_seconds=12, timeout=6):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Calibrating for ambient noise (0.6s)...")
        r.adjust_for_ambient_noise(source, duration=0.6)
        print(f"Start speaking (max {max_seconds}s)...")
        audio = r.listen(source, timeout=timeout, phrase_time_limit=max_seconds)
        wav_bytes = audio.get_wav_data(convert_rate=16000)  # 16 kHz mono
        tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        tmp.write(wav_bytes)
        tmp.flush()
        tmp.close()
        return tmp.name

def main():
    print("Loading Whisper model:", MODEL_NAME)
    t0 = time.time()
    model = whisper.load_model(MODEL_NAME)
    print(f"Model loaded in {time.time()-t0:.1f}s. Ready.\n")

    language_mode = None  # None = auto-detect, "en" = English, "ur" = Urdu

    try:
        while True:
            cmd = input("Press Enter=record | 'e'=force English | 'u'=force Urdu | 'exit'=quit: ").strip().lower()

            if cmd == "exit":
                break
            elif cmd == "e":
                language_mode = "en"
                print(">>> Forced language: English\n")
                continue
            elif cmd == "u":
                language_mode = "ur"
                print(">>> Forced language: Urdu\n")
                continue
            elif cmd == "":
                wav_path = None
                try:
                    wav_path = record_audio(max_seconds=12, timeout=6)
                    print("Recorded to:", wav_path)
                    print("Transcribing... (wait)")
                    t1 = time.time()
                    result = model.transcribe(wav_path, language=language_mode)
                    elapsed = time.time() - t1
                    text = result.get("text", "").strip()
                    print(f"Transcribed ({elapsed:.1f}s) [lang={language_mode or 'auto'}]:\n>>> {text}\n")
                except Exception as e:
                    print("Error:", e)
                finally:
                    if wav_path and os.path.exists(wav_path):
                        os.unlink(wav_path)
            else:
                print("Invalid input. Use Enter/e/u/exit.\n")

    except KeyboardInterrupt:
        print("\nExiting.")

if __name__ == "__main__":
    main()
