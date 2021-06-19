import ffmpeg

input_video = ffmpeg.input(r'D:\_deep_learning_data_10\3\O__1.mp4')

(
    ffmpeg
    .output(input_video.video, r'D:\_deep_learning_data_10\3\output-video.mp4', shortest=None, vcodec='copy')
    .overwrite_output()
    .run()
)