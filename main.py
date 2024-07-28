import cv2
import numpy as np
import random
from moviepy.editor import VideoFileClip, VideoClip


def add_moving_text_to_video(input_video_path, output_video_path, text):
    # Load the video using MoviePy
    clip = VideoFileClip(input_video_path)

    # Get video dimensions
    width, height = clip.size

    # Function to add text to a frame
    def add_text_to_frame(get_frame, t):
        frame = get_frame(t)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Generate random coordinates for the text
        x = random.randint(0, width - 100)
        y = random.randint(50, height - 50)

        # Add text to the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_color = (0, 255, 255)  # Yellow color
        thickness = 3

        frame = cv2.putText(frame, text, (x, y), font, font_scale, font_color, thickness, cv2.LINE_AA)

        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Apply the add_text_to_frame function to each frame
    new_clip = clip.fl(add_text_to_frame, apply_to=['mask', 'video'])

    # Write the result to a new video file
    new_clip.write_videofile(output_video_path, codec='libx264')


# Example usage
input_video = "input_video.mp4"
output_video = "output_video_with_text.mp4"
number = "123"  # The number to display

add_moving_text_to_video(input_video, output_video, number)
