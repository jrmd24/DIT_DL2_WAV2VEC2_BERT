import os

from gradio_client import Client, handle_file

client = Client("http://localhost:7860/")

# Use a raw string for the file path
audio_file_path = r"E:\00.Divers\DIT\04.Cours\M2\06.DS-DeepLearning2\Examen\Dev\id10012_0AXjxNXiEzo_00001.flac"

# Verify the file exists (good practice!)
if not os.path.exists(audio_file_path):
    print(f"Error: The file '{audio_file_path}' does not exist. Please check the path.")
else:
    print(f"File found: {audio_file_path}")
    result = client.predict(input=handle_file(audio_file_path), api_name="/predict")
    print(result)
