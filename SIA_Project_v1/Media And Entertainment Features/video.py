import tkinter as tk
from tkvideoplayer import TkVideoPlayer

root = tk.Tk()
root.title("Tkinter Video Player")

player = TkVideoPlayer(root, keep_aspect_ratio=True)
player.pack(expand=True, fill="both")

# Replace "your_video.mp4" with the actual path to your video file
player.load("C:\Users\Ralph\Desktop\All Files\Python\Python\SIA_Project\test.mp4")
player.play()
root.mainloop()