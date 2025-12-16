import tkinter as tk
from tkinter import messagebox
import random
import os
import pygame
import vlc

# ================= BASE DIR FIX =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dummy backend auth and DB (replace with actual imports if available)
try:
    from modules.auth import login_user, register_user  # packaged layout
    from modules.database import initialize_db
except Exception:
    try:
        from modules.auth import login_user, register_user  # local files
        from modules.database import initialize_db
    except Exception:
        print("Backend modules not found. Running in UI-only mode.")
        def login_user(u, p):
            return True, "Bypass"
        def register_user(u, p):
            return True, "Bypass"
        def initialize_db():
            pass

# Colors and fonts
COLOR_DARK_BG = "#5D6D7E"
COLOR_ACCENT = "#E67E22"
COLOR_GRAY_BOX = "#D5D8DC"
COLOR_BUTTON_HOVER = "#D35D10"

FONT_HEADER = ("Arial", 20, "bold")
FONT_BODY = ("Arial", 12)
FONT_BUTTON = ("Arial", 12, "bold")
FONT_SMALL = ("Arial", 10)

# Video files - add your actual video paths here
VIDEO_FILES = {
    "Batman": os.path.join(BASE_DIR, "video", "bat-man.mp4"),
    "Spider-Man": os.path.join(BASE_DIR, "video", "spider-man.mp4"),
    "Superman": os.path.join(BASE_DIR, "video", "super-man.mp4"),
    "Iron Man": os.path.join(BASE_DIR, "video", "iron-man.mp4"),
    "Avatar": os.path.join(BASE_DIR, "video", "avatar.mp4")
}

AUDIO_FILES = {
    "Nandito Ako": os.path.join(BASE_DIR, "audio", "nandito.mp3"),
    "Buwan": os.path.join(BASE_DIR, "audio", "buwan.mp3"),
    "Dilaw": os.path.join(BASE_DIR, "audio", "dilaw.mp3"),
    "Upuan": os.path.join(BASE_DIR, "audio", "upuan.mp3"),
    "Multo": os.path.join(BASE_DIR, "audio", "multo.mp3")
}

class MediaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Media & Entertainment System")
        self.geometry("900x600")
        self.resizable(False, False)

        initialize_db()
        pygame.mixer.init()  # Initialize once

        # VLC instance for video playback
        self.vlc_instance = vlc.Instance("--vout=d3d9", "--no-video-title-show")
        self.vlc_player = None

        self.current_user = None
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.show_landing_page()

    def clear_screen(self):
        pygame.mixer.music.stop()
        if self.vlc_player:
            self.vlc_player.stop()
            self.vlc_player = None
        for widget in self.container.winfo_children():
            widget.destroy()

    # --- PART 1: Login Page ---
    def show_landing_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        frame = tk.Frame(self.container, bg=COLOR_DARK_BG)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Username", bg=COLOR_DARK_BG, fg="white", font=FONT_BODY).pack(pady=5)
        self.entry_user = tk.Entry(frame, font=FONT_BODY, width=30)
        self.entry_user.pack(pady=5)

        tk.Label(frame, text="Password", bg=COLOR_DARK_BG, fg="white", font=FONT_BODY).pack(pady=5)
        self.entry_pass = tk.Entry(frame, show="*", font=FONT_BODY, width=30)
        self.entry_pass.pack(pady=5)

        tk.Button(frame, text="Log In", bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, width=20, relief="raised", bd=2,
                  command=self.perform_login).pack(pady=20)

        tk.Button(frame, text="Register New User", bg=COLOR_DARK_BG, fg="white",
                  borderwidth=1, font=FONT_SMALL, activebackground=COLOR_BUTTON_HOVER,
                  command=self.perform_register).pack(pady=5)

    def perform_login(self):
        user = self.entry_user.get()
        pwd = self.entry_pass.get()
        if not user or not pwd:
            messagebox.showwarning("Input", "Please enter username and password.")
            return
        success, msg = login_user(user, pwd)
        if success:
            self.current_user = user
            self.show_menu_page()
        else:
            messagebox.showerror("Login Failed", msg)

    def perform_register(self):
        user = self.entry_user.get()
        pwd = self.entry_pass.get()
        if user and pwd:
            success, msg = register_user(user, pwd)
            messagebox.showinfo("Registration", msg)
        else:
            messagebox.showwarning("Input", "Please enter username and password.")

    def perform_logout(self):
        self.current_user = None
        self.show_landing_page()

    # --- PART 2: Main Menu ---
    def show_menu_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        header = tk.Frame(self.container, bg=COLOR_DARK_BG)
        header.pack(fill="x", padx=20, pady=10)

        tk.Button(header, text="Logout", bg="#ffffff", fg="black",
                  font=FONT_BUTTON, relief="raised", bd=2,
                  command=self.perform_logout).pack(side="left")

        greeting = f"Hello, {self.current_user}" if self.current_user else "Hello Guest"
        tk.Label(header, text=greeting, bg=COLOR_DARK_BG, fg="white", font=("Arial", 14, "bold")).pack(side="right")

        frame = tk.Frame(self.container, bg=COLOR_DARK_BG)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        menu_items = [
            ("Movies and TV Shows", self.show_movies_page),
            ("Music and Audio", self.show_audio_page),
            ("Video Games", self.show_games_page),
        ]

        for text, action in menu_items:
            btn = tk.Button(frame, text=text, bg=COLOR_ACCENT, fg="white",
                            font=("Arial", 14, "bold"), width=30, height=2,
                            relief="raised", bd=2, activebackground=COLOR_BUTTON_HOVER,
                            command=action)
            btn.pack(pady=15)

    # --- PART 3: Movies Page ---
    def show_movies_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        top = tk.Frame(self.container, bg=COLOR_DARK_BG)
        top.pack(fill="x", padx=20, pady=10)

        tk.Button(top, text="Go Back", bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, relief="raised", bd=2,
                  command=self.show_menu_page).pack(side="left")

        tk.Label(top, text="Movies & TV Shows", bg=COLOR_DARK_BG, fg="white",
                 font=FONT_HEADER).pack(side="left", padx=20)

        main = tk.Frame(self.container, bg=COLOR_DARK_BG)
        main.place(relx=0.5, rely=0.55, anchor="center")

        for title in VIDEO_FILES.keys():
            available = os.path.exists(VIDEO_FILES[title])
            btn_bg = COLOR_ACCENT if available else COLOR_GRAY_BOX
            btn_fg = "white" if available else "black"
            btn_command = (lambda t=title: self.show_movie_player(t)) if available else None

            btn = tk.Button(main, text=f"{title} {'' if available else '(Unavailable)'}",
                            width=40, height=2, bg=btn_bg, fg=btn_fg,
                            font=FONT_BODY, relief="raised", bd=2,
                            activebackground=COLOR_BUTTON_HOVER,
                            command=btn_command)
            btn.pack(pady=10)

    # --- PART 4: Video Player ---
    def show_movie_player(self, title):
        if title not in VIDEO_FILES or not os.path.exists(VIDEO_FILES[title]):
            messagebox.showerror("Error", "Video file not found.")
            return

        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        top = tk.Frame(self.container, bg=COLOR_DARK_BG)
        top.pack(fill="x", padx=20, pady=10)

        tk.Button(top, text="⬅ Go Back", bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, relief="raised", bd=2,
                  command=self.exit_video_player).pack(side="left")

        tk.Label(top, text=f"Now Playing: {title}", bg=COLOR_DARK_BG, fg="white",
                 font=FONT_HEADER).pack(side="left", padx=20)

        video_frame = tk.Frame(self.container, bg="black", width=700, height=394)
        video_frame.place(relx=0.5, rely=0.55, anchor="center")

        self.update()  # Needed for VLC embedding

        # Use existing VLC instance
        self.vlc_player = self.vlc_instance.media_player_new()
        media = self.vlc_instance.media_new(VIDEO_FILES[title])
        self.vlc_player.set_media(media)
        self.vlc_player.set_hwnd(video_frame.winfo_id())
        self.vlc_player.play()

        # --- Controls ---
        controls = tk.Frame(self.container, bg=COLOR_DARK_BG)
        controls.pack(side="bottom", pady=10)

        tk.Button(controls, text="⏸ Pause", bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, width=10,
                  command=self.vlc_player.pause).grid(row=0, column=0, padx=5)

        tk.Button(controls, text="▶ Play", bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, width=10,
                  command=self.vlc_player.play).grid(row=0, column=1, padx=5)

        tk.Button(controls, text="⏹ Stop", bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, width=10,
                  command=self.vlc_player.stop).grid(row=0, column=2, padx=5)

    def exit_video_player(self):
        if self.vlc_player:
            self.vlc_player.stop()
            self.vlc_player = None
        self.show_movies_page()

    # --- PART 5: Audio Page ---
    def show_audio_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        top = tk.Frame(self.container, bg=COLOR_DARK_BG)
        top.pack(fill="x", padx=20, pady=10)

        tk.Button(top, text="Go Back", bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, relief="raised", bd=2,
                  command=self.show_menu_page).pack(side="left")

        tk.Label(top, text="Music & Audio", bg=COLOR_DARK_BG, fg="white",
                 font=FONT_HEADER).pack(side="left", padx=20)

        main = tk.Frame(self.container, bg=COLOR_DARK_BG)
        main.place(relx=0.5, rely=0.5, anchor="center")

        self.audio_files = AUDIO_FILES
        self.currently_playing = None
        self.audio_buttons = []

        for name in self.audio_files.keys():
            available = os.path.exists(self.audio_files[name])
            btn_bg = COLOR_ACCENT if available else COLOR_GRAY_BOX
            btn_fg = "white" if available else "black"
            btn_command = (lambda n=name: self.play_audio_feedback(n)) if available else None

            btn = tk.Button(main, text=name, width=40, height=2,
                            bg=btn_bg, fg=btn_fg, font=FONT_BODY,
                            relief="raised", bd=2, activebackground=COLOR_BUTTON_HOVER,
                            command=btn_command)
            btn.pack(pady=10)
            self.audio_buttons.append(btn)

        self.audio_display = tk.Label(self.container, text="Select a music category to play.",
                                      bg=COLOR_DARK_BG, fg="white", font=("Arial", 14))
        self.audio_display.place(relx=0.5, rely=0.85, anchor="center")

    def play_audio_feedback(self, selected):
        if self.currently_playing:
            pygame.mixer.music.stop()
            self.currently_playing = None

        file_path = self.audio_files[selected]
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            self.currently_playing = selected
            self.audio_display.config(text=f"Now Playing: {selected} 🎶")
        else:
            self.audio_display.config(text=f"Audio file for {selected} not found.")

    # --- PART 6: Games Page ---
    def show_games_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        top = tk.Frame(self.container, bg=COLOR_DARK_BG)
        top.pack(fill="x", padx=20, pady=10)

        tk.Button(top, text="Go Back", bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, relief="raised", bd=2,
                  command=self.show_menu_page).pack(side="left")

        tk.Label(top, text="Video Games", bg=COLOR_DARK_BG, fg="white",
                 font=FONT_HEADER).pack(side="left", padx=20)

        grid = tk.Frame(self.container, bg=COLOR_DARK_BG)
        grid.place(relx=0.5, rely=0.5, anchor="center")

        games = [
            ("Rock Paper Scissors", self.show_rps_game),
            ("Number Guessing", self.show_number_guess_game),
            ("Tic Tac Toe", self.show_tictactoe_game),
        ]

        for idx, (name, func) in enumerate(games):
            btn = tk.Button(grid, text=name, width=25, height=3, bg=COLOR_ACCENT, fg="white",
                            font=FONT_BODY, relief="raised", bd=2, command=func)
            btn.grid(row=0, column=idx, padx=20, pady=20)

    # --- Rock Paper Scissors ---
    def show_rps_game(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        tk.Button(self.container, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_games_page).pack(anchor="w", padx=20, pady=20)

        frame = tk.Frame(self.container, bg=COLOR_GRAY_BOX, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Rock Paper Scissors", font=FONT_HEADER, bg=COLOR_GRAY_BOX).pack(pady=10)

        self.rps_result = tk.Entry(frame, justify="center", font=FONT_BODY, relief="solid", bd=1)
        self.rps_result.pack(pady=10, fill="x")

        def play(choice):
            opts = ["Rock", "Paper", "Scissors"]
            comp = random.choice(opts)
            if choice == comp:
                res = "Draw"
            elif (choice=="Rock" and comp=="Scissors") or (choice=="Paper" and comp=="Rock") or (choice=="Scissors" and comp=="Paper"):
                res = "You Win!"
            else:
                res = "Computer Wins!"
            self.rps_result.delete(0, tk.END)
            self.rps_result.insert(0, f"You: {choice} | PC: {comp} -> {res}")

        btn_frame = tk.Frame(frame, bg=COLOR_GRAY_BOX)
        btn_frame.pack(pady=10)

        for opt in ["Rock", "Paper", "Scissors"]:
            tk.Button(btn_frame, text=opt, width=10, command=lambda o=opt: play(o),
                      bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON, relief="raised", bd=2).pack(side="left", padx=5)

        tk.Button(frame, text="Reset", width=10, command=lambda: self.rps_result.delete(0, tk.END),
                  bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON, relief="raised", bd=2).pack(pady=10)

    # --- Number Guessing ---
    def show_number_guess_game(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        tk.Button(self.container, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_games_page).pack(anchor="w", padx=20, pady=20)

        frame = tk.Frame(self.container, bg=COLOR_GRAY_BOX, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Number Guessing Game", font=FONT_HEADER, bg=COLOR_GRAY_BOX).pack(pady=10)

        if not hasattr(self, "secret_number") or not hasattr(self, "guesses_left"):
            self.secret_number = random.randint(1, 100)
            self.guesses_left = 10

        tk.Label(frame, text="Guess a number between 1 and 100", font=FONT_BODY, bg=COLOR_GRAY_BOX).pack(pady=5)

        self.guess_entry = tk.Entry(frame, font=FONT_BODY, width=10)
        self.guess_entry.pack(pady=5)

        self.guess_feedback = tk.Label(frame, text="", font=FONT_BODY, bg=COLOR_GRAY_BOX)
        self.guess_feedback.pack(pady=5)

        def guess_number():
            try:
                val = int(self.guess_entry.get())
            except:
                self.guess_feedback.config(text="Enter a valid number!")
                return

            if val == self.secret_number:
                self.guess_feedback.config(text="Correct! You Win!")
            elif val < self.secret_number:
                self.guess_feedback.config(text="Too low!")
            else:
                self.guess_feedback.config(text="Too high!")

            self.guesses_left -= 1
            if self.guesses_left <= 0:
                self.guess_feedback.config(text=f"Game Over! Number was {self.secret_number}")

        tk.Button(frame, text="Guess", width=10, command=guess_number,
                  bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON, relief="raised", bd=2).pack(pady=5)

        def reset_game():
            self.secret_number = random.randint(1, 100)
            self.guesses_left = 10
            self.guess_feedback.config(text="")
            self.guess_entry.delete(0, tk.END)

        tk.Button(frame, text="Reset", width=10, command=reset_game,
                  bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON, relief="raised", bd=2).pack(pady=5)

    # --- Tic Tac Toe ---
    def show_tictactoe_game(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        tk.Button(self.container, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_games_page).pack(anchor="w", padx=20, pady=20)

        frame = tk.Frame(self.container, bg=COLOR_GRAY_BOX, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Tic Tac Toe", font=FONT_HEADER, bg=COLOR_GRAY_BOX).pack(pady=10)

        self.ttt_board = [""] * 9
        self.ttt_turn = "X"
        self.ttt_buttons = []

        def check_winner():
            combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            for a,b,c in combos:
                if self.ttt_board[a] == self.ttt_board[b] == self.ttt_board[c] != "":
                    return self.ttt_board[a]
            return None

        def button_click(i):
            if self.ttt_board[i] == "":
                self.ttt_board[i] = self.ttt_turn
                self.ttt_buttons[i].config(text=self.ttt_turn)
                winner = check_winner()
                if winner:
                    messagebox.showinfo("Tic Tac Toe", f"{winner} wins!")
                    reset_board()
                    return
                elif "" not in self.ttt_board:
                    messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                    reset_board()
                    return
                self.ttt_turn = "O" if self.ttt_turn == "X" else "X"

        def reset_board():
            self.ttt_board[:] = ["" for _ in range(9)]
            for btn in self.ttt_buttons:
                btn.config(text="")
            self.ttt_turn = "X"

        grid = tk.Frame(frame, bg=COLOR_GRAY_BOX)
        grid.pack(pady=10)
        for i in range(9):
            btn = tk.Button(grid, text="", width=6, height=3, font=FONT_BUTTON,
                            bg=COLOR_ACCENT, fg="white", relief="raised", bd=2,
                            command=lambda i=i: button_click(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.ttt_buttons.append(btn)

        tk.Button(frame, text="Reset", width=10, command=reset_board,
                  bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON, relief="raised", bd=2).pack(pady=10)


if __name__ == "__main__":
    app = MediaApp()
    app.mainloop()
