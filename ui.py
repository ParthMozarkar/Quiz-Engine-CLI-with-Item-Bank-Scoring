import tkinter as tk
from tkinter import ttk
import math

class QuizUI:
    def __init__(self, controller):
        self.controller = controller  
        self.root = tk.Tk()
        self.root.title("Quiz Engine Pro")
        self.root.geometry("900x650")
        self.root.resizable(False, False)
        
        # Modern color scheme
        self.colors = {
            'bg_primary': '#0a0e27',      # Dark blue-black
            'bg_secondary': '#1a1d3a',    # Lighter dark blue
            'accent': '#6366f1',          # Indigo
            'accent_hover': '#818cf8',    # Light indigo
            'success': '#10b981',         # Green
            'danger': '#ef4444',          # Red
            'text_primary': '#f9fafb',    # Almost white
            'text_secondary': '#9ca3af',  # Gray
            'card_bg': '#1e293b',         # Card background
        }
        
        # Configure root background
        self.root.configure(bg=self.colors['bg_primary'])
        
        self.selected_option = tk.IntVar()
        self.username_entry = None
        self.question_label = None
        self.option_buttons = []
        self.next_button = None
        self.progress_bar = None
        self.current_question_num = 0
        self.total_questions = 0

        # Add custom styles
        self.setup_styles()
        
        self.create_welcome_screen()

    def setup_styles(self):
        """Setup modern ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Progress bar style
        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor=self.colors['bg_secondary'],
            background=self.colors['accent'],
            bordercolor=self.colors['bg_secondary'],
            lightcolor=self.colors['accent'],
            darkcolor=self.colors['accent']
        )

    def create_gradient_frame(self, parent, height=650):
        """Create a frame with gradient effect"""
        canvas = tk.Canvas(parent, width=900, height=height, 
                          bg=self.colors['bg_primary'], highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        
        # Create gradient effect
        for i in range(height):
            color_value = int(10 + (i / height) * 20)  # Subtle gradient
            color = f'#{color_value:02x}{color_value + 14:02x}{39:02x}'
            canvas.create_line(0, i, 900, i, fill=color)
        
        return canvas

    def create_card(self, parent, x, y, width, height):
        """Create a modern card with shadow effect"""
        # Shadow
        parent.create_rectangle(
            x + 5, y + 5, x + width + 5, y + height + 5,
            fill='#000000', outline='', stipple='gray50'
        )
        # Card
        parent.create_rectangle(
            x, y, x + width, y + height,
            fill=self.colors['card_bg'], outline=self.colors['accent'], width=2
        )

    def create_welcome_screen(self):
        self.clear_screen()
        canvas = self.create_gradient_frame(self.root)
        
        # Main card
        self.create_card(canvas, 200, 100, 500, 450)
        
        # Title with glow effect
        canvas.create_text(
            450, 180, 
            text="QUIZ ENGINE", 
            font=("Helvetica", 42, "bold"),
            fill=self.colors['accent']
        )
        canvas.create_text(
            450, 182, 
            text="QUIZ ENGINE", 
            font=("Helvetica", 42, "bold"),
            fill=self.colors['text_primary']
        )
        
        # Subtitle
        canvas.create_text(
            450, 230,
            text="Test Your Knowledge, Track Your Progress",
            font=("Helvetica", 14),
            fill=self.colors['text_secondary']
        )
        
        # Decorative line
        canvas.create_line(300, 260, 600, 260, fill=self.colors['accent'], width=2)
        
        # Username label
        canvas.create_text(
            450, 310,
            text="ENTER YOUR NAME",
            font=("Helvetica", 12, "bold"),
            fill=self.colors['text_primary']
        )
        
        # Custom entry
        entry_frame = tk.Frame(self.root, bg=self.colors['bg_secondary'], 
                              highlightbackground=self.colors['accent'], 
                              highlightthickness=2)
        canvas.create_window(450, 350, window=entry_frame, width=300, height=45)
        
        self.username_entry = tk.Entry(
            entry_frame,
            font=("Helvetica", 14),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['text_primary'],
            relief='flat',
            bd=10
        )
        self.username_entry.pack(fill='both', expand=True)
        self.username_entry.focus()
        
        # Bind Enter key
        self.username_entry.bind('<Return>', lambda e: self.controller.start_quiz(self.username_entry.get()))
        
        # Modern button
        start_btn = self.create_modern_button(
            canvas, 450, 430, "START QUIZ →", 
            lambda: self.controller.start_quiz(self.username_entry.get()),
            width=200
        )
        
        # Footer
        canvas.create_text(
            450, 520,
            text="Powered by Quiz Engine Pro • Version 2.0",
            font=("Helvetica", 10),
            fill=self.colors['text_secondary']
        )

    def create_modern_button(self, canvas, x, y, text, command, width=150, height=45):
        """Create a modern button with hover effects"""
        button_frame = tk.Frame(
            self.root,
            bg=self.colors['accent'],
            cursor='hand2'
        )
        canvas.create_window(x, y, window=button_frame, width=width, height=height)
        
        button = tk.Label(
            button_frame,
            text=text,
            font=("Helvetica", 12, "bold"),
            bg=self.colors['accent'],
            fg=self.colors['text_primary'],
            cursor='hand2'
        )
        button.pack(fill='both', expand=True)
        
        # Hover effects
        def on_enter(e):
            button.configure(bg=self.colors['accent_hover'])
            button_frame.configure(bg=self.colors['accent_hover'])
        
        def on_leave(e):
            button.configure(bg=self.colors['accent'])
            button_frame.configure(bg=self.colors['accent'])
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        button.bind('<Button-1>', lambda e: command())
        button_frame.bind('<Button-1>', lambda e: command())
        
        return button_frame

    def show_question(self, question_text, options):
        self.clear_screen()
        self.current_question_num += 1
        
        canvas = self.create_gradient_frame(self.root)
        
        # Progress section
        progress_text = f"Question {self.current_question_num} of {self.total_questions}"
        canvas.create_text(
            450, 40,
            text=progress_text,
            font=("Helvetica", 14, "bold"),
            fill=self.colors['text_secondary']
        )
        
        # Progress bar
        progress_frame = tk.Frame(self.root, bg=self.colors['bg_secondary'])
        canvas.create_window(450, 70, window=progress_frame, width=700, height=8)
        
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            style="Custom.Horizontal.TProgressbar",
            length=700,
            mode='determinate',
            value=(self.current_question_num / self.total_questions) * 100
        )
        self.progress_bar.pack()
        
        # Question card
        self.create_card(canvas, 100, 120, 700, 150)
        
        # Question text
        canvas.create_text(
            450, 195,
            text=question_text,
            font=("Helvetica", 16, "bold"),
            fill=self.colors['text_primary'],
            width=650
        )
        
        # Options
        self.selected_option.set(-1)
        self.option_buttons = []
        
        option_labels = ['A', 'B', 'C', 'D', 'E']
        
        for i, opt in enumerate(options):
            y_pos = 310 + (i * 70)
            self.create_option_card(canvas, opt, i, option_labels[i], y_pos)
        
        # Next button
        next_btn_y = 310 + (len(options) * 70) + 30
        self.next_button = self.create_modern_button(
            canvas, 450, next_btn_y, "SUBMIT ANSWER →",
            lambda: self.controller.check_answer(self.selected_option.get()),
            width=200, height=50
        )

    def create_option_card(self, canvas, text, value, label, y_pos):
        """Create an option card with hover effects"""
        card_frame = tk.Frame(
            self.root,
            bg=self.colors['card_bg'],
            highlightbackground=self.colors['bg_secondary'],
            highlightthickness=2,
            cursor='hand2'
        )
        canvas.create_window(450, y_pos, window=card_frame, width=650, height=55)
        
        # Label (A, B, C, D)
        label_widget = tk.Label(
            card_frame,
            text=label,
            font=("Helvetica", 14, "bold"),
            bg=self.colors['accent'],
            fg=self.colors['text_primary'],
            width=3,
            cursor='hand2'
        )
        label_widget.pack(side='left', fill='y', padx=(0, 15))
        
        # Option text
        radio = tk.Radiobutton(
            card_frame,
            text=text,
            variable=self.selected_option,
            value=value,
            font=("Helvetica", 13),
            bg=self.colors['card_bg'],
            fg=self.colors['text_primary'],
            activebackground=self.colors['card_bg'],
            activeforeground=self.colors['text_primary'],
            selectcolor=self.colors['accent'],
            cursor='hand2',
            anchor='w',
            relief='flat',
            borderwidth=0,
            highlightthickness=0
        )
        radio.pack(side='left', fill='both', expand=True, padx=10)
        
        # Hover effects
        def on_enter(e):
            card_frame.configure(highlightbackground=self.colors['accent'])
            label_widget.configure(bg=self.colors['accent_hover'])
        
        def on_leave(e):
            if self.selected_option.get() != value:
                card_frame.configure(highlightbackground=self.colors['bg_secondary'])
                label_widget.configure(bg=self.colors['accent'])
        
        def on_select():
            # Update all option cards
            for btn in self.option_buttons:
                btn['frame'].configure(highlightbackground=self.colors['bg_secondary'])
                btn['label'].configure(bg=self.colors['accent'])
            # Highlight selected
            card_frame.configure(highlightbackground=self.colors['accent'])
            label_widget.configure(bg=self.colors['accent_hover'])
        
        card_frame.bind('<Enter>', on_enter)
        card_frame.bind('<Leave>', on_leave)
        label_widget.bind('<Enter>', on_enter)
        label_widget.bind('<Leave>', on_leave)
        
        radio.configure(command=on_select)
        
        self.option_buttons.append({
            'frame': card_frame,
            'label': label_widget,
            'radio': radio
        })

    def show_result(self, score, total, percentage):
        """Display quiz results with leaderboard and exit buttons"""
        self.clear_screen()
        canvas = self.create_gradient_frame(self.root)
        
        # Determine performance
        if percentage >= 80:
            emoji = "🏆"
            title = "OUTSTANDING!"
            color = self.colors['success']
            message = "Exceptional performance!"
        elif percentage >= 60:
            emoji = "⭐"
            title = "GREAT JOB!"
            color = self.colors['accent']
            message = "You did really well!"
        else:
            emoji = "📚"
            title = "KEEP LEARNING!"
            color = self.colors['text_secondary']
            message = "Practice makes perfect!"
        
        # Result card (taller to fit buttons)
        self.create_card(canvas, 200, 100, 500, 480)
        
        # Emoji
        canvas.create_text(
            450, 180,
            text=emoji,
            font=("Helvetica", 72)
        )
        
        # Title
        canvas.create_text(
            450, 260,
            text=title,
            font=("Helvetica", 32, "bold"),
            fill=color
        )
        
        # Message
        canvas.create_text(
            450, 300,
            text=message,
            font=("Helvetica", 14),
            fill=self.colors['text_secondary']
        )
        
        # Score
        canvas.create_text(
            450, 360,
            text=f"{score} / {total}",
            font=("Helvetica", 48, "bold"),
            fill=self.colors['text_primary']
        )
        
        # Percentage
        canvas.create_text(
            450, 420,
            text=f"{percentage:.1f}% Accuracy",
            font=("Helvetica", 18),
            fill=self.colors['accent']
        )
        
        # Leaderboard button (Left side)
        self.create_modern_button(
            canvas, 340, 510, "🏆 LEADERBOARD",
            lambda: self.view_leaderboard(),
            width=160,
            height=45
        )
        
        # Exit button (Right side)
        self.create_modern_button(
            canvas, 560, 510, "EXIT",
            self.root.destroy,
            width=160,
            height=45
        )

    def clear_screen(self):
        self.current_question_num = 0
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def set_total_questions(self, total):
        """Call this before showing first question"""
        self.total_questions = total
        self.current_question_num = 0

    def show_leaderboard(self, leaderboard_data):
        """Display the leaderboard screen"""
        self.clear_screen()
        canvas = self.create_gradient_frame(self.root)
        
        # Title
        canvas.create_text(
            450, 50,
            text="🏆 LEADERBOARD 🏆",
            font=("Helvetica", 32, "bold"),
            fill=self.colors['accent']
        )
        
        canvas.create_text(
            450, 90,
            text="Top Players of All Time",
            font=("Helvetica", 14),
            fill=self.colors['text_secondary']
        )
        
        # Main leaderboard card
        self.create_card(canvas, 100, 130, 700, 420)
        
        if not leaderboard_data:
            canvas.create_text(
                450, 340,
                text="No scores yet!\nBe the first to play!",
                font=("Helvetica", 16),
                fill=self.colors['text_secondary'],
                justify='center'
            )
        else:
            # Headers
            headers = [
                ("Rank", 150, "center"),
                ("Player", 300, "left"),
                ("Score", 500, "center"),
                ("Accuracy", 650, "center")
            ]
            
            y_pos = 160
            for header, x, align in headers:
                canvas.create_text(
                    x, y_pos,
                    text=header,
                    font=("Helvetica", 12, "bold"),
                    fill=self.colors['text_secondary'],
                    anchor='center' if align == 'center' else 'w'
                )
            
            # Divider line
            canvas.create_line(130, 185, 770, 185, fill=self.colors['bg_secondary'], width=2)
            
            # Leaderboard entries
            y_pos = 210
            medals = ["#1", "#2", "#3"]
            
            for i, entry in enumerate(leaderboard_data[:10], 1):
                # Rank with medal for top 3
                rank_text = medals[i-1] if i <= 3 else f"#{i}"
                
                # Alternate row colors
                if i % 2 == 0:
                    canvas.create_rectangle(
                        130, y_pos - 12, 770, y_pos + 18,
                        fill=self.colors['bg_secondary'], outline=''
                    )
                
                # Rank
                canvas.create_text(
                    150, y_pos,
                    text=rank_text,
                    font=("Helvetica", 14, "bold"),
                    fill=self.colors['text_primary']
                )
                
                # Player name
                player_name = str(entry.get('Name', 'Unknown'))[:20]
                canvas.create_text(
                    300, y_pos,
                    text=player_name,
                    font=("Helvetica", 13),
                    fill=self.colors['text_primary'],
                    anchor='w'
                )
                
                # Score
                score = entry.get('Score', 0)
                total = entry.get('Total', 0)
                score_text = f"{score}/{total}"
                canvas.create_text(
                    500, y_pos,
                    text=score_text,
                    font=("Helvetica", 13, "bold"),
                    fill=self.colors['accent']
                )
                
                # Percentage
                percentage_str = str(entry.get('Percentage', '0%'))
                percentage_val = float(percentage_str.rstrip('%'))
                
                canvas.create_text(
                    650, y_pos,
                    text=percentage_str,
                    font=("Helvetica", 13),
                    fill=self.colors['success'] if percentage_val >= 80 else self.colors['text_primary']
                )
                
                y_pos += 35
        
        # Back button
        self.create_modern_button(
            canvas, 450, 590, "← BACK TO MENU",
            lambda: self.create_welcome_screen(),
            width=200
        )
    
    def view_leaderboard(self):
        """Load and show leaderboard"""
        from quiz_engine.scorer import get_leaderboard
        leaderboard_data = get_leaderboard(10)
        self.show_leaderboard(leaderboard_data)
    
    def start(self):
        self.root.mainloop()