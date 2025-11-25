import tkinter as tk
from tkinter import messagebox
import random

# Backend imports: try packaged `modules`, fall back to local files, then to UI-only stubs
try:
    from modules.auth import login_user, register_user  # packaged layout
    from modules.database import initialize_db
except Exception:
    try:
        from auth import login_user, register_user  # local files
        from database import initialize_db
    except Exception:
        print("Backend modules not found. Running in UI-only mode.")
        def login_user(u, p):
            return True, "Bypass"
        def register_user(u, p):
            return True, "Bypass"
        def initialize_db():
            pass

# --- COLOR PALETTE (Based on your Design) ---
COLOR_DARK_BG = "#5D6D7E"   # The dark grey for Landing/Menu
COLOR_LIGHT_BG = "#FFFFFF"  # White for content pages
COLOR_ACCENT = "#E67E22"    # The Orange for buttons
COLOR_GRAY_BOX = "#D5D8DC"  # The light grey for thumbnails
COLOR_BUTTON_HOVER = "#D35D10"  # Darker orange for hover
COLOR_BORDER = "#BDC3C7"    # Light border color
FONT_HEADER = ("Arial", 20, "bold")
FONT_BODY = ("Arial", 12)
FONT_BUTTON = ("Arial", 12, "bold")
FONT_SMALL = ("Arial", 10)

class MediaApp(tk.Tk):
    """Main application window for the Media & Entertainment System."""
    def __init__(self):
        super().__init__()
        self.title("Media & Entertainment System")
        self.geometry("900x600")
        # Prevent resizing/maximizing: lock window size
        try:
            # set fixed size and disable resizing
            self.resizable(False, False)
            self.minsize(900, 600)
            self.maxsize(900, 600)
        except Exception:
            pass

        # Track the currently logged-in user
        self.current_user = None
        # Initialize Database
        initialize_db()

        # --- Video Player Simulation State ---
        self.playback_job = None
        self.is_playing = False
        self.video_duration_seconds = 180 # Arbitrary duration (3 minutes) for simulation
        self.current_time_seconds = 0
        # --- End Simulation State ---


        # Main Container
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Start at Landing Page
        self.show_landing_page()

    def clear_screen(self):
        # Stop any running video simulation before clearing the screen
        if self.playback_job:
            self.after_cancel(self.playback_job)
            self.playback_job = None
            self.is_playing = False
            self.current_time_seconds = 0 # Reset simulation time

        for widget in self.container.winfo_children():
            widget.destroy()

    # 1. LANDING PAGE (Login)
    def show_landing_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        # Center Frame
        frame = tk.Frame(self.container, bg=COLOR_DARK_BG)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Username", bg=COLOR_DARK_BG, fg="white", font=FONT_BODY).pack(pady=5)
        self.entry_user = tk.Entry(frame, font=FONT_BODY, width=30)
        self.entry_user.pack(pady=5)

        tk.Label(frame, text="Password", bg=COLOR_DARK_BG, fg="white", font=FONT_BODY).pack(pady=5)
        self.entry_pass = tk.Entry(frame, show="*", font=FONT_BODY, width=30)
        self.entry_pass.pack(pady=5)

        # Orange Login Button
        btn = tk.Button(frame, text="Log In", bg=COLOR_ACCENT, fg="white",
                        font=FONT_BUTTON, width=20, relief="raised", bd=2, command=self.perform_login)
        btn.pack(pady=20)

        # Register Helper
        tk.Button(frame, text="Register New User", bg=COLOR_DARK_BG, fg="white",
                  borderwidth=1, font=FONT_SMALL, activebackground=COLOR_BUTTON_HOVER,
                  command=self.perform_register).pack(pady=5)

    def perform_login(self):
        user = self.entry_user.get()
        pwd = self.entry_pass.get()
        # Require both username and password before attempting login
        if not user or not pwd:
            messagebox.showwarning("Input", "Please enter username and password")
            return

        success, msg = login_user(user, pwd)
        if success:
            # store current user and go to Menu
            self.current_user = user
            try:
                self.entry_user.delete(0, tk.END)
                self.entry_pass.delete(0, tk.END)
            except Exception:
                pass
            self.show_menu_page() # Go to Menu
        else:
            messagebox.showerror("Login Failed", msg)

    def perform_register(self):
        user = self.entry_user.get()
        pwd = self.entry_pass.get()
        if user and pwd:
            success, msg = register_user(user, pwd)
            messagebox.showinfo("Registration", msg)
        else:
            messagebox.showwarning("Input", "Please enter username and password")

    def perform_logout(self):
        # Simple logout: return to landing page (clears current view)
        # If you later add session state, clear it here as well.
        # clear session state
        self.current_user = None
        # return to landing page and clear any inputs
        self.show_landing_page()
        # Clear login widgets if they exist
        if hasattr(self, 'entry_user'):
            try:
                self.entry_user.delete(0, tk.END)
            except Exception:
                pass
        if hasattr(self, 'entry_pass'):
            try:
                self.entry_pass.delete(0, tk.END)
            except Exception:
                pass

    # 2. MENU PAGE
    def show_menu_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_DARK_BG)

        # Header with Logout (left) and greeting (right)
        header = tk.Frame(self.container, bg=COLOR_DARK_BG)
        header.pack(fill="x", padx=20, pady=10)

        tk.Button(
            header,
            text="Logout",
            bg="#ffffff",
            fg="black",
            font=FONT_BUTTON,
            relief="raised",
            bd=2,
            command=self.perform_logout,
        ).pack(side="left")

        greeting = f"Hello, {self.current_user}" if self.current_user else "Hello Guest"
        tk.Label(
            header,
            text=greeting,
            bg=COLOR_DARK_BG,
            fg="white",
            font=("Arial", 14, "bold"),
        ).pack(side="right")

        frame = tk.Frame(self.container, bg=COLOR_DARK_BG)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # The 3 Big Orange Buttons
        btns = [
            ("Movies and TV Shows", self.show_movies_page),
            ("Music and Audio", self.show_audio_page),
            ("Video Games", self.show_games_page)
        ]

        for text, cmd in btns:
            b = tk.Button(frame, text=text, bg=COLOR_ACCENT, fg="white",
                          font=("Arial", 14, "bold"), width=30, height=2, relief="raised", bd=2,
                          activebackground=COLOR_BUTTON_HOVER, command=cmd)
            b.pack(pady=15)

    # 3. MOVIES SECTION
    def show_movies_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        # Header
        header = tk.Frame(self.container, bg=COLOR_LIGHT_BG, bd=1, relief="solid")
        header.pack(fill="x", padx=20, pady=15)
        tk.Button(header, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_menu_page).pack(side="left", padx=5, pady=5)

        search_entry = tk.Entry(header, width=40, font=FONT_BODY, relief="solid", bd=1)
        search_entry.pack(side="right", padx=5, pady=5)
        search_entry.insert(0, "Search...")

        # Content
        content = tk.Frame(self.container, bg=COLOR_LIGHT_BG)
        content.pack(fill="both", expand=True, padx=40)

        tk.Label(content, text="Movies and TV Shows Section", font=FONT_HEADER, bg=COLOR_LIGHT_BG).pack(anchor="w", pady=10)

        # Helper to create grid of grey boxes
        def create_grid(parent, title):
            tk.Label(parent, text=title, font=FONT_BUTTON, bg=COLOR_LIGHT_BG).pack(anchor="w", pady=(10,5))
            grid_frame = tk.Frame(parent, bg=COLOR_LIGHT_BG)
            grid_frame.pack(anchor="w")
            for i in range(3): # Create 3 placeholder boxes
                # Modified command to pass a specific movie name
                movie_name = f"Movie {i+1} Title"
                box = tk.Button(grid_frame, bg=COLOR_GRAY_BOX, width=15, height=6,
                                text=movie_name, font=FONT_SMALL, relief="raised", bd=1,
                                command=lambda name=movie_name: self.show_movie_player(name)) # Click to play
                box.grid(row=0, column=i, padx=10)

        create_grid(content, "Your Library")
        create_grid(content, "Trending")
        create_grid(content, "Genres")

    # --- VIDEO PLAYER IMPLEMENTATION START ---

    def format_time(self, seconds):
        """Converts total seconds into MM:SS format."""
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes:02d}:{secs:02d}"

    def update_time_display(self):
        """Updates the time label and progress bar value."""
        # Update current time label
        self.current_time_label.config(text=self.format_time(self.current_time_seconds))

        # Update progress bar *only* if the user is not actively dragging it
        if not self.progress_bar.grab_current():
             self.progress_bar.set(self.current_time_seconds)

    def seek_simulation(self, value):
        """Handles seeking when the user drags the progress bar."""
        try:
            new_time = int(float(value)) # Scale passes float, convert to int
            if 0 <= new_time <= self.video_duration_seconds:
                self.current_time_seconds = new_time
                self.update_time_display()
        except ValueError:
            pass # Ignore if value is invalid

    def start_playback_simulation(self):
        """Recursively updates the simulated playback time every 1000ms (1 second)."""
        if self.current_time_seconds >= self.video_duration_seconds:
            # End of video reached
            self.stop_playback_simulation()
            self.current_time_seconds = self.video_duration_seconds
            self.update_time_display()
            return

        if self.is_playing:
            self.current_time_seconds += 1 # Advance by 1 second
            self.update_time_display()

            # Schedule the next update
            self.playback_job = self.after(1000, self.start_playback_simulation)

    def stop_playback_simulation(self):
        """Stops the playback simulation."""
        self.is_playing = False
        if self.playback_job:
            self.after_cancel(self.playback_job)
            self.playback_job = None
        self.play_pause_button.config(text="▶ Play", bg=COLOR_ACCENT)

    def toggle_playback(self):
        """Toggles between Play and Pause."""
        if self.is_playing:
            # Pause
            self.stop_playback_simulation()
        else:
            # Play
            self.is_playing = True
            # If at the end, reset to 0 before starting
            if self.current_time_seconds >= self.video_duration_seconds:
                 self.current_time_seconds = 0

            self.play_pause_button.config(text="⏸ Pause", bg="green")
            self.start_playback_simulation() # Start the loop


    def show_movie_player(self, movie_name):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        # Back Button
        tk.Button(self.container, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_movies_page).pack(anchor="w", padx=20, pady=10)

        # Title
        tk.Label(self.container, text=movie_name, font=FONT_HEADER, bg=COLOR_LIGHT_BG).pack(pady=5)

        # Video Player Frame (Aspect Ratio 16:9 approx)
        player_screen = tk.Frame(self.container, bg="black", width=700, height=394, bd=2, relief="solid") # 700x394 is approx 16:9
        player_screen.pack(pady=10)
        player_screen.pack_propagate(False) # Force size

        # Placeholder text over the black screen
        tk.Label(player_screen, text=f"[ Simulated Video Playback for: {movie_name} ]", bg="black", fg="#00FF00", font=("Arial", 24)).place(relx=0.5, rely=0.5, anchor="center")

        # Control Panel
        controls_frame = tk.Frame(self.container, bg=COLOR_LIGHT_BG, bd=1, relief="solid", padx=20, pady=15)
        controls_frame.pack(fill="x", padx=100, pady=10)

        # Time Labels (Top of the bar)
        time_frame = tk.Frame(controls_frame, bg=COLOR_LIGHT_BG)
        time_frame.pack(fill="x", pady=(0, 5))
        self.current_time_label = tk.Label(time_frame, text="00:00", bg=COLOR_LIGHT_BG, font=FONT_SMALL, fg=COLOR_ACCENT)
        self.current_time_label.pack(side="left")
        self.duration_label = tk.Label(time_frame, text=self.format_time(self.video_duration_seconds), bg=COLOR_LIGHT_BG, font=FONT_SMALL, fg=COLOR_ACCENT)
        self.duration_label.pack(side="right")

        # Progress Bar (Scale widget)
        self.progress_bar = tk.Scale(
            controls_frame,
            from_=0,
            to=self.video_duration_seconds,
            orient="horizontal",
            length=600,
            showvalue=0, # Hide default value display
            troughcolor=COLOR_GRAY_BOX,
            sliderrelief="raised",
            bg=COLOR_LIGHT_BG,
            highlightthickness=1,
            bd=1,
            command=self.seek_simulation
        )
        self.progress_bar.pack(pady=5, fill="x")


        # Play/Pause/Stop Buttons
        playback_frame = tk.Frame(controls_frame, bg=COLOR_LIGHT_BG)
        playback_frame.pack(pady=10)

        # Play/Pause Button
        self.play_pause_button = tk.Button(
            playback_frame,
            text="▶ Play",
            bg=COLOR_ACCENT,
            fg="white",
            font=FONT_BUTTON,
            width=10,
            relief="raised",
            bd=2,
            command=self.toggle_playback
        )
        self.play_pause_button.pack(side="left", padx=10)

        # Start the display with time reset and button set to Play
        self.current_time_seconds = 0
        self.is_playing = False
        self.progress_bar.set(0)
        self.update_time_display()

    # --- VIDEO PLAYER IMPLEMENTATION END ---


    # 4. AUDIO SECTION
    def show_audio_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        # Header
        header = tk.Frame(self.container, bg=COLOR_LIGHT_BG, bd=1, relief="solid")
        header.pack(fill="x", padx=20, pady=15)
        tk.Button(header, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_menu_page).pack(side="left", padx=5, pady=5)

        search_entry = tk.Entry(header, width=40, font=FONT_BODY, relief="solid", bd=1)
        search_entry.pack(side="right", padx=5, pady=5)
        search_entry.insert(0, "Search...")

        content = tk.Frame(self.container, bg=COLOR_LIGHT_BG)
        content.pack(fill="both", expand=True, padx=40)

        tk.Label(content, text="MUSIC", font=FONT_HEADER, bg=COLOR_LIGHT_BG).pack(anchor="w", pady=10)

        # Grid Layout
        grid_frame = tk.Frame(content, bg=COLOR_LIGHT_BG)
        grid_frame.pack(fill="both", pady=20)

        # Columns (Discover, Podcast, Genres)
        cols = ["Discover something NEW!", "Podcasts", "Genres"]
        for col_idx, title in enumerate(cols):
            col_frame = tk.Frame(grid_frame, bg=COLOR_LIGHT_BG)
            col_frame.grid(row=0, column=col_idx, padx=30, sticky="n")
            tk.Label(col_frame, text=title, bg=COLOR_LIGHT_BG, font=FONT_BUTTON).pack(pady=5)

            for _ in range(3): # 3 boxes per column
                btn = tk.Button(col_frame, bg=COLOR_GRAY_BOX, width=20, height=4,
                                font=FONT_SMALL, relief="raised", bd=1,
                                command=lambda: self.show_audio_player("How Do I Live"))
                btn.pack(pady=5)

    def show_audio_player(self, song_name):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        tk.Button(self.container, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_audio_page).pack(anchor="w", padx=20, pady=20)

        # Album Art
        art = tk.Frame(self.container, bg=COLOR_GRAY_BOX, width=300, height=300, bd=2, relief="raised")
        art.pack(pady=20)
        art.pack_propagate(False)
        tk.Label(art, text="Album Art", bg=COLOR_GRAY_BOX, fg="#666666",
                 font=("Arial", 14), justify="center").place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.container, text=f"{song_name} (LeAnn Rimes)", font=("Arial", 14, "bold"), bg=COLOR_LIGHT_BG).pack(pady=10)

        # Controls
        controls = tk.Frame(self.container, bg=COLOR_LIGHT_BG)
        controls.pack()
        tk.Button(controls, text="<<", font=FONT_BUTTON, bg=COLOR_ACCENT, fg="white",
                  relief="raised", bd=2, width=5).pack(side="left", padx=10)
        tk.Button(controls, text="▶", font=("Arial", 20, "bold"), bg=COLOR_ACCENT, fg="white",
                  relief="raised", bd=2, width=5).pack(side="left", padx=10)
        tk.Button(controls, text=">>", font=FONT_BUTTON, bg=COLOR_ACCENT, fg="white",
                  relief="raised", bd=2, width=5).pack(side="left", padx=10)

    # 5. GAMES SECTION
    def show_games_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        # Header (Back button + optional search)
        header = tk.Frame(self.container, bg=COLOR_LIGHT_BG, bd=1, relief="solid")
        header.pack(fill="x", padx=20, pady=15)
        tk.Button(header, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_menu_page).pack(side="left", padx=5, pady=5)

        content = tk.Frame(self.container, bg=COLOR_LIGHT_BG)
        content.pack(fill="both", expand=True, padx=40)

        tk.Label(content, text="GAMES", font=FONT_HEADER, bg=COLOR_LIGHT_BG).pack(anchor="w")

        # Grid of unique games (3 columns)
        grid = tk.Frame(content, bg=COLOR_LIGHT_BG)
        grid.pack(pady=10)
        games = [
            ("Rock Paper Scissor", self.show_rps_game),
            ("Number Guessing", self.show_number_guess_game),
            ("Tic Tac Toe", self.show_tictactoe_game),
        ]

        for idx, (game_name, game_func) in enumerate(games):
            r = idx // 3
            c = idx % 3
            b = tk.Button(grid, bg=COLOR_GRAY_BOX, width=20, height=6,
                          font=FONT_SMALL, relief="raised", bd=1, text=game_name,
                          command=game_func)
            b.grid(row=r, column=c, padx=10, pady=10)

    def show_rps_game(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        tk.Button(self.container, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_games_page).pack(anchor="w", padx=20, pady=20)

        # Game Area (Replicating the Rock Paper Scissors UI)
        game_frame = tk.Frame(self.container, bg="white", bd=2, relief="solid", padx=20, pady=20)
        game_frame.pack()

        tk.Label(game_frame, text="Rock Paper Scissor", font=("Arial", 18, "bold"), fg=COLOR_ACCENT, bg="white").pack(pady=10)

        score_frame = tk.Frame(game_frame, bg="white", bd=1, relief="solid")
        score_frame.pack(fill="x", pady=10, padx=5)
        tk.Label(score_frame, text="Player", bg="white", font=FONT_BUTTON).pack(side="left", padx=20, pady=5)
        tk.Label(score_frame, text="vs", bg="white", font=FONT_BUTTON).pack(side="left", padx=20, pady=5)
        tk.Label(score_frame, text="Computer", bg="white", font=FONT_BUTTON).pack(side="right", padx=20, pady=5)

        self.result_display = tk.Entry(game_frame, justify="center", font=FONT_BODY, relief="solid", bd=1)
        self.result_display.pack(pady=10, fill="x", padx=5)

        btn_frame = tk.Frame(game_frame, bg="white")
        btn_frame.pack(pady=10)

        # Game Logic
        def play(choice):
            opts = ["Rock", "Paper", "Scissor"]
            comp = random.choice(opts)
            res = ""
            if choice == comp: res = "Draw"
            elif (choice == "Rock" and comp == "Scissor") or \
                 (choice == "Paper" and comp == "Rock") or \
                 (choice == "Scissor" and comp == "Paper"):
                res = "You Win!"
            else:
                res = "Computer Wins!"

            self.result_display.delete(0, tk.END)
            self.result_display.insert(0, f"You: {choice} | PC: {comp} -> {res}")

        tk.Button(btn_frame, text="Rock", command=lambda: play("Rock"), bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, relief="raised", bd=2).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Paper", command=lambda: play("Paper"), bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, relief="raised", bd=2).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Scissor", command=lambda: play("Scissor"), bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, relief="raised", bd=2).pack(side="left", padx=5)

        tk.Button(game_frame, text="Reset Game", bg=COLOR_DARK_BG, fg="white",
                  font=FONT_BUTTON, relief="raised", bd=2,
                  command=lambda: self.result_display.delete(0, tk.END)).pack(pady=10)

    def show_number_guess_game(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        tk.Button(self.container, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_games_page).pack(anchor="w", padx=20, pady=20)

        # Game Area (Number Guessing Game UI)
        game_frame = tk.Frame(self.container, bg="white", bd=2, relief="solid", padx=20, pady=20)
        game_frame.pack()

        tk.Label(game_frame, text="Number Guessing Game", font=("Arial", 18, "bold"), fg=COLOR_ACCENT, bg="white").pack(pady=10)

        # Game instructions
        instructions = tk.Label(game_frame, text="Guess a number between 1 and 100", font=FONT_BODY, bg="white")
        instructions.pack(pady=10)

        # Initialize game state
        if not hasattr(self, 'secret_number'):
            self.secret_number = random.randint(1, 100)
            self.guesses_left = 10

        # Display info frame
        info_frame = tk.Frame(game_frame, bg="white", bd=1, relief="solid")
        info_frame.pack(fill="x", pady=10, padx=5)
        tk.Label(info_frame, text=f"Attempts Left: {self.guesses_left}", font=FONT_BUTTON, bg="white").pack(side="left", padx=20, pady=5)
        self.hint_label = tk.Label(info_frame, text="", font=FONT_BODY, bg="white", fg=COLOR_ACCENT)
        self.hint_label.pack(side="right", padx=20, pady=5)

        # Input frame
        input_frame = tk.Frame(game_frame, bg="white")
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Your Guess:", font=FONT_BODY, bg="white").pack(side="left", padx=5)
        self.guess_entry = tk.Entry(input_frame, font=FONT_BODY, width=10, relief="solid", bd=1)
        self.guess_entry.pack(side="left", padx=5)

        self.guess_result_display = tk.Entry(game_frame, justify="center", font=FONT_BODY, relief="solid", bd=1)
        self.guess_result_display.pack(pady=10, fill="x", padx=5)

        # Buttons frame
        btn_frame = tk.Frame(game_frame, bg="white")
        btn_frame.pack(pady=10)

        # Game Logic
        def make_guess():
            try:
                guess = int(self.guess_entry.get())

                if guess < 1 or guess > 100:
                    self.guess_result_display.delete(0, tk.END)
                    self.guess_result_display.insert(0, "Please enter a number between 1 and 100!")
                    return

                self.guesses_left -= 1

                if guess == self.secret_number:
                    self.guess_result_display.delete(0, tk.END)
                    self.guess_result_display.insert(0, f"🎉 You Win! The number was {self.secret_number}!")
                    self.guess_entry.config(state="disabled")
                    guess_btn.config(state="disabled")
                elif self.guesses_left == 0:
                    self.guess_result_display.delete(0, tk.END)
                    self.guess_result_display.insert(0, f"Game Over! The number was {self.secret_number}")
                    self.guess_entry.config(state="disabled")
                    guess_btn.config(state="disabled")
                else:
                    hint = "Too High!" if guess > self.secret_number else "Too Low!"
                    self.hint_label.config(text=hint)
                    self.guess_result_display.delete(0, tk.END)
                    self.guess_result_display.insert(0, f"{hint} | Attempts Left: {self.guesses_left}")

                self.guess_entry.delete(0, tk.END)

            except ValueError:
                self.guess_result_display.delete(0, tk.END)
                self.guess_result_display.insert(0, "Invalid input! Please enter a number.")

        guess_btn = tk.Button(btn_frame, text="Guess", command=make_guess, bg=COLOR_ACCENT, fg="white",
                              font=FONT_BUTTON, relief="raised", bd=2, width=10)
        guess_btn.pack(side="left", padx=5)

        def reset_game():
            self.secret_number = random.randint(1, 100)
            self.guesses_left = 10
            self.guess_entry.delete(0, tk.END)
            self.guess_entry.config(state="normal")
            self.guess_result_display.delete(0, tk.END)
            self.hint_label.config(text="")
            guess_btn.config(state="normal")
            instructions.config(text="Guess a number between 1 and 100")

        tk.Button(btn_frame, text="New Game", command=reset_game, bg=COLOR_ACCENT, fg="white",
                  font=FONT_BUTTON, relief="raised", bd=2, width=10).pack(side="left", padx=5)

    def show_tictactoe_game(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        tk.Button(self.container, text="< Back", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, command=self.show_games_page).pack(anchor="w", padx=20, pady=20)

        # Tic Tac Toe area
        game_frame = tk.Frame(self.container, bg="white", bd=2, relief="solid", padx=20, pady=20)
        game_frame.pack()

        tk.Label(game_frame, text="Tic Tac Toe", font=("Arial", 18, "bold"), fg=COLOR_ACCENT, bg="white").pack(pady=10)

        # Status
        self.ttt_status = tk.Label(game_frame, text="Player X's turn", font=FONT_BODY, bg="white")
        self.ttt_status.pack(pady=5)

        # Board
        board_frame = tk.Frame(game_frame, bg="white")
        board_frame.pack()

        # Initialize board state
        self.ttt_board = [""] * 9
        self.ttt_current = "X"
        self.ttt_buttons = []

        def ttt_click(idx):
            if self.ttt_board[idx] != "":
                return
            self.ttt_board[idx] = self.ttt_current
            btn = self.ttt_buttons[idx]
            btn.config(text=self.ttt_current, state="disabled", bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON)

            # Check win
            combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            winner = None
            for a,b,c in combos:
                if self.ttt_board[a] and self.ttt_board[a] == self.ttt_board[b] == self.ttt_board[c]:
                    winner = self.ttt_board[a]
                    break

            if winner:
                self.ttt_status.config(text=f"Player {winner} wins!", fg="green")
                for b in self.ttt_buttons:
                    b.config(state="disabled")
                return

            if all(cell != "" for cell in self.ttt_board):
                self.ttt_status.config(text="It's a draw!", fg="orange")
                return

            # Switch player
            self.ttt_current = "O" if self.ttt_current == "X" else "X"
            self.ttt_status.config(text=f"Player {self.ttt_current}'s turn")

        for i in range(9):
            btn = tk.Button(board_frame, text="", width=6, height=3, bg=COLOR_GRAY_BOX, relief="raised", bd=1,
                            command=lambda idx=i: ttt_click(idx))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.ttt_buttons.append(btn)

        # Controls
        ctrl = tk.Frame(game_frame, bg="white")
        ctrl.pack(pady=10)

        def reset_ttt():
            self.ttt_board = [""] * 9
            self.ttt_current = "X"
            for b in self.ttt_buttons:
                b.config(text="", state="normal", bg=COLOR_GRAY_BOX, fg="black")
            self.ttt_status.config(text="Player X's turn", fg="black")

        tk.Button(ctrl, text="Reset", command=reset_ttt, bg=COLOR_ACCENT, fg="white", font=FONT_BUTTON,
                  relief="raised", bd=2, width=10).pack(side="left", padx=5)

if __name__ == "__main__":
    app = MediaApp()
    app.mainloop()