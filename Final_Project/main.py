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
FONT_HEADER = ("Arial", 20, "bold")
FONT_BODY = ("Arial", 12)

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

        # Main Container
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Start at Landing Page
        self.show_landing_page()

    def clear_screen(self):
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
                        font=("Arial", 12, "bold"), width=20, command=self.perform_login)
        btn.pack(pady=20)

        # Register Helper
        tk.Button(frame, text="Register New User", bg=COLOR_DARK_BG, fg="white",
                  borderwidth=0, command=self.perform_register).pack()

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
            font=("Arial", 13),
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
                          font=("Arial", 14, "bold"), width=30, height=2, command=cmd)
            b.pack(pady=15)

    # 3. MOVIES SECTION
    def show_movies_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        # Header
        header = tk.Frame(self.container, bg=COLOR_LIGHT_BG)
        header.pack(fill="x", padx=20, pady=20)
        tk.Button(header, text="< Back", command=self.show_menu_page).pack(side="left")
        tk.Entry(header, width=40).pack(side="right") # Search Bar

        # Content
        content = tk.Frame(self.container, bg=COLOR_LIGHT_BG)
        content.pack(fill="both", expand=True, padx=40)

        tk.Label(content, text="Movies and TV Shows Section", font=FONT_HEADER, bg=COLOR_LIGHT_BG).pack(anchor="w", pady=10)

        # Helper to create grid of grey boxes
        def create_grid(parent, title):
            tk.Label(parent, text=title, font=("Arial", 10, "bold"), bg=COLOR_LIGHT_BG).pack(anchor="w", pady=(10,5))
            grid_frame = tk.Frame(parent, bg=COLOR_LIGHT_BG)
            grid_frame.pack(anchor="w")
            for i in range(3): # Create 3 placeholder boxes
                box = tk.Button(grid_frame, bg=COLOR_GRAY_BOX, width=15, height=6,
                                command=lambda: self.show_movie_player("Iron Man")) # Click to play
                box.grid(row=0, column=i, padx=10)

        create_grid(content, "Your Library")
        create_grid(content, "Trending")
        create_grid(content, "Genres")

    def show_movie_player(self, movie_name):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        tk.Button(self.container, text="< Back", command=self.show_movies_page).pack(anchor="w", padx=20, pady=20)

        tk.Label(self.container, text=movie_name, font=FONT_HEADER, bg=COLOR_LIGHT_BG).pack(pady=10)

        # Big Grey Box (Player Screen)
        player_screen = tk.Frame(self.container, bg=COLOR_GRAY_BOX, width=600, height=350)
        player_screen.pack(pady=20)
        player_screen.pack_propagate(False) # Force size

        tk.Label(player_screen, text="[ Video Player Placeholder ]", bg=COLOR_GRAY_BOX).place(relx=0.5, rely=0.5, anchor="center")

    # 4. AUDIO SECTION
    def show_audio_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        # Header
        header = tk.Frame(self.container, bg=COLOR_LIGHT_BG)
        header.pack(fill="x", padx=20, pady=20)
        tk.Button(header, text="< Back", command=self.show_menu_page).pack(side="left")
        tk.Entry(header, width=40).pack(side="right")

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
            tk.Label(col_frame, text=title, bg=COLOR_LIGHT_BG).pack(pady=5)

            for _ in range(3): # 3 boxes per column
                btn = tk.Button(col_frame, bg=COLOR_GRAY_BOX, width=20, height=4,
                                command=lambda: self.show_audio_player("How Do I Live"))
                btn.pack(pady=5)

    def show_audio_player(self, song_name):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        tk.Button(self.container, text="< Back", command=self.show_audio_page).pack(anchor="w", padx=20, pady=20)

        # Album Art
        art = tk.Frame(self.container, bg=COLOR_GRAY_BOX, width=300, height=300)
        art.pack(pady=20)

        tk.Label(self.container, text=f"{song_name} (LeAnn Rimes)", font=("Arial", 14), bg=COLOR_LIGHT_BG).pack(pady=10)

        # Controls
        controls = tk.Frame(self.container, bg=COLOR_LIGHT_BG)
        controls.pack()
        tk.Button(controls, text="<<", font=("Arial", 14)).pack(side="left", padx=10)
        tk.Button(controls, text="▶", font=("Arial", 18)).pack(side="left", padx=10)
        tk.Button(controls, text=">>", font=("Arial", 14)).pack(side="left", padx=10)

    # 5. GAMES SECTION
    def show_games_page(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        header = tk.Frame(self.container, bg=COLOR_LIGHT_BG)
        header.pack(fill="x", padx=20, pady=20)
        tk.Button(header, text="< Back", command=self.show_menu_page).pack(side="left")
        tk.Entry(header, width=30).pack(side="right")

        content = tk.Frame(self.container, bg=COLOR_LIGHT_BG)
        content.pack(fill="both", expand=True, padx=40)

        tk.Label(content, text="GAMES", font=FONT_HEADER, bg=COLOR_LIGHT_BG).pack(anchor="w")

        # Tab-like headers
        tabs = tk.Frame(content, bg=COLOR_LIGHT_BG)
        tabs.pack(anchor="w", pady=10)
        for t in ["Library", "Store", "Favorites", "Kids"]:
            tk.Label(tabs, text=t, padx=15, bg=COLOR_LIGHT_BG).pack(side="left")

        # Grid of Games
        grid = tk.Frame(content, bg=COLOR_LIGHT_BG)
        grid.pack(pady=10)
        for r in range(2):
            for c in range(4):
                b = tk.Button(grid, bg=COLOR_GRAY_BOX, width=18, height=6,
                              command=self.show_rps_game) # All buttons open RPS game for now
                b.grid(row=r, column=c, padx=10, pady=10)

    def show_rps_game(self):
        self.clear_screen()
        self.container.configure(bg=COLOR_LIGHT_BG)

        tk.Button(self.container, text="< Back", command=self.show_games_page).pack(anchor="w", padx=20, pady=20)

        # Game Area (Replicating the Rock Paper Scissors UI)
        game_frame = tk.Frame(self.container, bg="white", bd=2, relief="solid", padx=20, pady=20)
        game_frame.pack()

        tk.Label(game_frame, text="Rock Paper Scissor", font=("Arial", 18, "bold"), fg="blue", bg="white").pack(pady=10)

        score_frame = tk.Frame(game_frame, bg="white")
        score_frame.pack(fill="x", pady=10)
        tk.Label(score_frame, text="Player", bg="white").pack(side="left", padx=20)
        tk.Label(score_frame, text="vs", bg="white").pack(side="left", padx=20)
        tk.Label(score_frame, text="Computer", bg="white").pack(side="right", padx=20)

        self.result_display = tk.Entry(game_frame, justify="center", font=("Arial", 12))
        self.result_display.pack(pady=10, fill="x")

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

        tk.Button(btn_frame, text="Rock", command=lambda: play("Rock")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Paper", command=lambda: play("Paper")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Scissor", command=lambda: play("Scissor")).pack(side="left", padx=5)

        tk.Button(game_frame, text="Reset Game", bg="black", fg="red",
                  command=lambda: self.result_display.delete(0, tk.END)).pack(pady=10)

if __name__ == "__main__":
    app = MediaApp()
    app.mainloop()