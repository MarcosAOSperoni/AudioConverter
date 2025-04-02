import os
import subprocess

def convert_m4a_to_mp3(directory):
    """
    Recursively search the given directory for .m4a files and convert them to .mp3.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.m4a'):
                input_path = os.path.join(root, file)
                output_file = os.path.splitext(file)[0] + '.mp3'
                output_path = os.path.join(root, output_file)

                print(f"Converting:\n  From: {input_path}\n  To:   {output_path}")
                
                # Construct the ffmpeg command
                command = ['ffmpeg', '-i', input_path, output_path]
                try:
                    subprocess.run(command, check=True)
                    print("✅ Conversion successful.\n")
                except subprocess.CalledProcessError as error:
                    print(f"❌ Conversion failed for {input_path}. Error: {error}\n")

if __name__ == '__main__':
    directory = input("Enter the directory path containing .m4a files: ").strip()
    if os.path.isdir(directory):
        convert_m4a_to_mp3(directory)
    else:
        print("The specified directory does not exist.")