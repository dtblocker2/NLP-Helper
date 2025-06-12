import vosk
import pyaudio
import json

model_path = "vosk-model-en-us-0.42-gigaspeech"
model = vosk.Model(model_path)

rec = vosk.KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()

try:
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=8192)
    
    while True:
        try:
            data = stream.read(4096, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                recognized_text = result['text']

                print(recognized_text)

                if "terminate" in recognized_text.lower():
                    print("Termination keyword detected. Stopping...")
                    break
        except OSError as e:
            if e.errno == -9988:
                print("Stream closed unexpectedly.")
                break
            else:
                print(f"Keyboard interrupt")
                break
        except KeyboardInterrupt:
            print(f"Keyboard interrupt")
            break

except Exception as e:
    print(f"Failed to start stream: {e}")
finally:
    try:
        stream.stop_stream()
        stream.close()
    except Exception as e:
        print(f"Error closing stream: {e}")
    p.terminate()
