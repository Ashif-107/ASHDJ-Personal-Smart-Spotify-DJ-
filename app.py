import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading

from spotify_api import authenticate_spotify
from commands.menu import run_interactive_menu


class AnimeTerminalApp:
    def __init__(self, root, sp):
        self.sp = sp
        self.root = root
        self.root.title("Spotify Anime Assistant")

        # Set window size to match GIF dimensions
        self.window_width = 500*2
        self.window_height = 291*2
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.configure(bg="black")

        # Full-size GIF label
        self.gif_label = tk.Label(self.root, bg="black")
        self.gif_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Input box at the bottom
        self.entry = tk.Entry(self.root, font=("Consolas", 12),
                              bg="black", fg="white", insertbackground="white")
        self.entry.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)
        self.entry.bind("<Return>", self.send_command)

        self.load_gif("anime_girl.gif")

    def load_gif(self, gif_path):
        gif = Image.open(gif_path)
        # Resize all frames to match window size
        self.gif_frames = [
            ImageTk.PhotoImage(frame.copy().convert("RGBA").resize(
                (self.window_width, self.window_height), Image.LANCZOS))
            for frame in ImageSequence.Iterator(gif)
        ]
        self.gif_index = 0
        self.animate_gif()

    def animate_gif(self):
        self.gif_label.config(image=self.gif_frames[self.gif_index])
        self.gif_index = (self.gif_index + 1) % len(self.gif_frames)
        self.root.after(100, self.animate_gif)

    def send_command(self, event):
        command = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        threading.Thread(target=self.process_command, args=(command,)).start()

    def process_command(self, command):
        # No printing to terminal to avoid Unicode errors
        run_interactive_menu(self.sp, single_command=command, output_func=lambda msg: None)


def main():
    try:
        sp = authenticate_spotify()
        root = tk.Tk()
        app = AnimeTerminalApp(root, sp)
        root.mainloop()
    except Exception as e:
        print(f"❌ Error initializing Spotify: {e}")
        print("Please check your configuration and try again.")


if __name__ == "__main__":
    main()
