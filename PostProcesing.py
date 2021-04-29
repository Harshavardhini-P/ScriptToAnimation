import moviepy.video.io.ImageSequenceClip
import os
destinFolder = "VideoOut/"

def CleanDestinFolder():
    for x in os.listdir(destinFolder):
        os.remove(destinFolder + x)
    return

fps=24
image_files = [destinFolder+'/'+img for img in os.listdir(destinFolder) if img.endswith(".png")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('Final/Out.mp4')
CleanDestinFolder()