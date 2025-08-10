import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk, ImageSequence
import threading
import queue

from spotify_api import authenticate_spotify
from commands.menu import run_interactive_menu

output_queue = queue.Queue()

class AnimeTerminalApp:
    def __init__(self, root, sp):
        self.sp = sp
        self.root = root
        self.root.title("Spotify Anime Assistant")
        self.root.geometry("800x500")
        self.root.configure(bg="#222")

        # Anime GIF display
        self.gif_label = tk.Label(self.root, bg="#222")
        self.gif_label.pack(side="left", padx=10, pady=10)
        self.load_gif("anime_girl.gif")

        # Terminal area
        self.terminal = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, bg="#111", fg="white", font=("Consolas", 12)
        )
        self.terminal.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # Input box
        self.entry = tk.Entry(self.root, font=("Consolas", 12))
        self.entry.pack(side="bottom", fill="x", padx=10, pady=10)
        self.entry.bind("<Return>", self.send_command)

        # Start updating output
        self.root.after(100, self.update_terminal)

    def load_gif(self, gif_path):
        gif = Image.open(gif_path)
        self.gif_frames = [
            ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)
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
        output_queue.put(f"> {command}")
        threading.Thread(target=self.process_command, args=(command,)).start()

    def process_command(self, command):
        run_interactive_menu(self.sp, single_command=command, output_func=output_queue.put)

    def update_terminal(self):
        while not output_queue.empty():
            self.terminal.insert(tk.END, output_queue.get() + "\n")
            self.terminal.see(tk.END)
        self.root.after(100, self.update_terminal)


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
