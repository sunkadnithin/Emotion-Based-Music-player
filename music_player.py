# music_player.py

import tkinter as tk
from tkinter import Listbox, END
import vlc
import os

class MusicPlayer:
    def __init__(self, root, emotion_name):
        self.root = root
        self.root.title("Simple Music Player")
        
        self.player = None
        self.playlist = []
        self.current_song_index = -1
        
        # Create buttons
        self.load_button = tk.Button(root, text="Load Songs", command=lambda: self.load_from_emotion(emotion_name))
        self.load_button.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)

        self.prev_button = tk.Button(root, text="Previous", command=self.previous)
        self.prev_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next)
        self.next_button.pack(pady=10)

        # Close button
        self.close_button = tk.Button(root, text="Close", command=self.close)
        self.close_button.pack(pady=10)

        # Listbox for playlist
        self.playlist_box = Listbox(root)
        self.playlist_box.pack(pady=10)

    def load_from_emotion(self, emotion_name):
        """Load audio files from the specified emotion directory."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        emotion_dir = os.path.join(script_dir, 'Songs', emotion_name)
        
        if not os.path.exists(emotion_dir):
            os.makedirs(emotion_dir)
            print(f"Directory '{emotion_dir}' created.")
       
        audio_files = [f for f in os.listdir(emotion_dir) if f.endswith(('.mp3', '.wav'))]
        if len(audio_files) <= 0:
            emotion_dir = os.path.join(script_dir, 'Songs', "Default")
            audio_files = [f for f in os.listdir(emotion_dir) if f.endswith(('.mp3', '.wav'))]
            print(f"No Song found for emotion : {emotion_name}, Playing the default songs")

        for file in audio_files:
            full_path = os.path.join(emotion_dir, file)
            self.playlist.append(full_path)
            self.playlist_box.insert(END, file)  # Display file name only
        if self.current_song_index == -1 and self.playlist:
            self.current_song_index = 0
            self.load_song()
       

    def play(self):
        if self.player is not None:
            self.player.play()

    def stop(self):
        if self.player is not None:
            self.player.stop()

    def previous(self):
        if self.playlist:
            self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
            self.load_song()

    def next(self):
        if self.playlist:
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
            self.load_song()

    def load_song(self):
        if self.player is not None:
            self.player.stop()
            self.player = vlc.MediaPlayer(self.playlist[self.current_song_index])
            self.player.play()
            self.playlist_box.selection_clear(0, END)
            self.playlist_box.selection_set(self.current_song_index)

    def close(self):
    # Stop the player and close the application.
        self.stop()  # Stop the music if playing
        self.root.destroy()  # Close the main window



def run_music_player(emotion_name):
    # Create the main application window
    root = tk.Tk()
    
    # Set the title of the window
    root.title("Music Player")
    
    player = MusicPlayer(root, emotion_name)
    
    # Add a close button
    close_button = tk.Button(root, text="Close", command=root.destroy)
    close_button.pack(pady=10)
    
    # Start the Tkinter event loop
    root.mainloop()
