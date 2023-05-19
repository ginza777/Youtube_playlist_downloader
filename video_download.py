from pytube import YouTube


def download_video():
    while True:
        url = input("Enter the YouTube video link: ")

        try:
            video = YouTube(url)
            print("Video Title: ", video.title)
            video_stream = video.streams.filter(res="2160p").first()  # Select 4K resolution stream
            file_size_gb = video_stream.filesize / (1024 * 1024 * 1024)  # Convert to GB
            print("File Size: ", round(file_size_gb, 2), "GB")
            video_stream.download(output_path='Videoklip')
            print("Video downloaded successfully!")
        except Exception as e:
            print("Error occurred while downloading the video:", str(e))

        choice = input("Do you want to download another video? (yes/no): ")
        if choice.lower() != "yes":
            break


# Call the function to start downloading videos
download_video()
