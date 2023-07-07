import moviepy.editor as mp
import speech_recognition as sr
import os

# Option 1: Convert Video to Audio
def convert_video_to_audio(video_file, audio_file, audio_format):
    #audio_format = input("Enter audio format (wav, mp3, etc.): ")
    video = mp.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file, codec=audio_format)

# Option 2: Convert Audio to Text
def convert_audio_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    return text

# Option 3: Streaming Recognition (Not supported by speech_recognition library)
# You may need to explore other libraries or APIs that offer streaming capabilities.

# Option 4: Offline Speech Recognition
def convert_audio_to_text_offline(audio_file):
    # Perform offline speech recognition using your preferred library (e.g., CMU Sphinx, Mozilla DeepSpeech, etc.)
    # Replace this code with your chosen library's offline speech recognition implementation.
    # Make sure you have the necessary language resources installed/configured for offline recognition.
    text = "Your offline speech recognition code here"
    return text

# Option 5: Convert Audio to Video
def convert_audio_to_video(audio_file, video_file, video_format):
    #video_format = input("Enter video format (mp4, avi, etc.): ")
    audio = mp.AudioFileClip(audio_file)
    video = mp.VideoFileClip(video_file)
    video = video.set_audio(audio)
    video.write_videofile(video_file, codec=video_format)

# Main function
def convert_media_to_text(input_file, convert_option, output_format):
    filename, file_extension = os.path.splitext(input_file)
    
    if convert_option == "video_to_audio":
        # Convert Video to Audio
        output_format = input("Enter audio format (wav, mp3, etc.): ")
        audio_file = f"{filename}.{output_format}"
        convert_video_to_audio(input_file, audio_file, output_format)
        
        # Option 2: Convert Audio to Text
        text = convert_audio_to_text(audio_file)

    elif convert_option == "audio_to_text":
        # Convert Audio to Text
        text = convert_audio_to_text(input_file)

    elif convert_option == "audio_to_video":
        # Convert Audio to Video
        output_format = input("Enter video format (mp4, avi, etc.): ")
        video_file = f"{filename}.{output_format}"
        convert_audio_to_video(input_file, video_file, output_format)
        return

    else:
        print("Invalid convert option.")
        return

    # Option 3: Streaming Recognition
    # Not supported by speech_recognition library
    
    # Option 4: Offline Speech Recognition
    # Uncomment the following line to use offline speech recognition
    # text = convert_audio_to_text_offline(input_file)

    # Write the text to a file
    text_file = f"{filename}.txt"
    with open(text_file, "w") as file:
        file.write(text)
    
    print(f"Conversion complete! {input_file} has been converted to {text_file}")

# Usage example

input_file = input("Enter the input file name: ")
convert_option = input("Choose convert option (video_to_audio, audio_to_text, audio_to_video): ")
#output_format = input("Enter the output format: ")
output_format = ""

convert_media_to_text(input_file, convert_option, output_format)