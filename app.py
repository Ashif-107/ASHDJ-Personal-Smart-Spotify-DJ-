import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
import speech_recognition as sr

from spotify_api import authenticate_spotify
from commands.menu import run_interactive_menu

from elevenlabs_api import speak, announce_playing

class AnimeTerminalApp:
    def __init__(self, root, sp):
        self.sp = sp
        self.root = root
        self.root.title("Spotify Anime Assistant")

        # Window size
        self.window_width = 500 * 2
        self.window_height = 291 * 2
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.configure(bg="black")

        # Full-size GIF label
        self.gif_label = tk.Label(self.root, bg="black")
        self.gif_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Input box
        self.entry = tk.Entry(self.root, font=("Consolas", 12),
                              bg="black", fg="white", insertbackground="white")
        self.entry.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)
        self.entry.bind("<Return>", self.send_command)

        # Bind keyboard shortcut for voice (Ctrl+M)
        self.root.bind("<Control-m>", lambda e: self.start_voice_thread())
        self.root.bind("<Control-M>", lambda e: self.start_voice_thread())  # Uppercase M

        self.load_gif("anime_girl.gif")

    def load_gif(self, gif_path):
        gif = Image.open(gif_path)
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
        threading.Thread(target=self.process_command, args=(command,), daemon=True).start()

    def process_command(self, command):
        announce_playing(command)  # Using convenient DJ announcement function
        def speak_and_print(msg):
            print(msg)  # Still show in terminal
        speak_and_print(command)
        run_interactive_menu(self.sp, single_command=command, output_func=lambda msg: None)

    def start_voice_thread(self):
        """Start listening in a separate thread to avoid freezing UI"""
        threading.Thread(target=self.listen_voice, daemon=True).start()

    def listen_voice(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎙 Listening for command...")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
                command = recognizer.recognize_google(audio)
                print(f"✅ You said: {command}")
                self.process_command(command)
            except sr.UnknownValueError:
                print("❌ Could not understand audio.")
            except sr.RequestError:
                print("❌ Speech recognition service unavailable.")
            except sr.WaitTimeoutError:
                print("⌛ Listening timed out.")


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
