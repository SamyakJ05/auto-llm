import speech_recognition as sr
from pydub import AudioSegment
import io

# Load MP3 as AudioSegment
def mp3_to_wav(mp3_file):
    try:
        # Load the MP3 file using AudioSegment from pydub
        audio = AudioSegment.from_mp3(mp3_file)
        
        # Export to a byte stream (no need for a temp WAV file on disk)
        wav_file = io.BytesIO()
        audio.export(wav_file, format="wav")
        wav_file.seek(0)  # Reset the byte stream to the start
        return wav_file
    except Exception as e:
        print(f"Error converting MP3 to WAV: {e}")
        return None

# Transcribe audio from WAV byte stream
def transcribe_audio(wav_stream):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_stream) as source:
            print("Recognizing audio...")
            audio = recognizer.record(source)
        
        # Use Google's free API to transcribe the audio
        text = recognizer.recognize_google(audio)
        print("Transcription: ", text)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error transcribing the audio: {e}")

# Main function
def main(mp3_file):
    wav_stream = mp3_to_wav(mp3_file)  # Convert MP3 to WAV in memory
    if wav_stream:
        transcribe_audio(wav_stream)  # Transcribe the audio

if __name__ == "__main__":
    mp3_file = "C:\\Users\\sjsam\\OneDrive\\Documents\\New folder\\Coldplay - Hymn For The Weekend (Official Video).mp3"  # Provide your MP3 file path
    main(mp3_file)
