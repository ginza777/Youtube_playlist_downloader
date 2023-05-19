from pytube import YouTube
from tqdm import tqdm
import os

def download_video():
    while True:
        url = input("Enter the YouTube video link: ")

        try:
            video = YouTube(url)
            print("Video Title: ", video.title)
            video_stream = video.streams.filter(res="2160p").first()  # Select 4K resolution stream
            file_size_gb = video_stream.filesize / (1024 * 1024 * 1024)  # Convert to GB
            print("File Size: ", round(file_size_gb, 2), "GB")

            # Start downloading the video with progress tracking
            output_path = 'Videoklip'
            video_stream.download(output_path=output_path, filename='video_temp')
            file_path = f"{output_path}/{video.title}.mp4"

            with tqdm(total=video_stream.filesize, unit='bytes', unit_scale=True) as progress_bar:
                def progress_callback(stream, chunk, file_handle, bytes_remaining):
                    progress_bar.update(len(chunk))

                video_stream.register_on_progress_callback(progress_callback)
                video_stream.download(output_path=output_path, filename='video_temp')
                os.rename(f"{output_path}/video_temp.mp4", file_path)

            print("Video downloaded successfully!")
        except Exception as e:
            print("Error occurred while downloading the video:", str(e))

        choice = input("Do you want to download another video? (yes/no): ")
        if choice.lower() != "yes":
            break

# Call the function to start downloading videos
download_video()
