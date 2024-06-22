from moviepy.editor import VideoFileClip
from math import floor
from dotenv import load_dotenv

load_dotenv()

WIP_FOLDER = os.getenv('WIP_FOLDER')

import os

def rescale_video(origin_filename, output_width = 1920, output_height = 1080, output_filename = 'scaled.mp4'):
    """
    This method was created to rescale videos upper to 1920x1080 or 1080x1920. This is,
    when a 4k video appears, we simplify it to 1080p resolution to work with only that
    resolution.

    This method is used in the script-guided video generation. Please, do not touch =).
    """
    # We only want to accept 16/9 or 9/16 by now, so:
    if not (output_width == 1920 and output_height == 1080) and not (output_width == 1080 and output_height == 1920):
        print('Sorry, not valid input parameters.')
        return
    
    SCALE_WIDTH = 16
    SCALE_HEIGHT = 9
    if output_width == 1080 and output_height == 1920:
        SCALE_WIDTH = 9
        SCALE_HEIGHT = 16

    clip = VideoFileClip(origin_filename)

    width = clip.w
    height = clip.h

    # We avoid things like 1927 instead of 1920
    new_width = width - width % SCALE_WIDTH
    new_height = height - height % SCALE_HEIGHT

    proportion = new_width / new_height

    if proportion > (SCALE_WIDTH / SCALE_HEIGHT):
        print('This video has more width than expected. Cropping horizontally.')
        while (new_width / new_height) != (SCALE_WIDTH / SCALE_HEIGHT):
            new_width -= SCALE_WIDTH
    elif proportion < (SCALE_WIDTH / SCALE_HEIGHT):
        print('This video has more height than expected. Cropping vertically.')
        while (new_width / new_height) != (SCALE_WIDTH / SCALE_HEIGHT):
            new_height -= SCALE_HEIGHT

    print('Final: W' + str(new_width) + ' H' + str(new_height))
    clip2 = clip.crop(x_center = floor(width / 2), y_center = floor(height / 2), width = new_width, height = new_height)
    
    # Force output dimensions
    if new_width != output_width:
        print('Forcing W' + str(output_width) + ' H' + str(output_height))
        clip2 = clip2.resize(width = output_width, height = output_height)

    # This fixes the problem of rewriting over an existing video
    clip2.write_videofile(WIP_FOLDER + 'scaled.mp4', codec = 'libx264', audio_codec = 'aac', temp_audiofile = WIP_FOLDER + 'temp-audio.m4a', remove_temp = True)
    os.remove(origin_filename)
    os.rename(WIP_FOLDER + 'scaled.mp4', output_filename)
    
    return True