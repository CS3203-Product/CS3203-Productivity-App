from nicegui import ui

class Uncram:
    # This is the main class for the Uncram tool
    pass

class TaskPrioritizationEngine:
    # This class is responsible for prioritizing tasks based on various factors
    pass
class TimeBlockingScheduler:
    # This class is responsible for scheduling tasks into time blocks
    pass

class FocusModeTimer:
    # This class is responsible for implementing a focus mode timer to help users stay focused on their tasks
    # We are creating a Pomodoro style timer
    # It breaks work into 25 minute "work" intervals with 5 minute breaks in between. 
    # After four "Pomodoros", the user takes a longer break of 15-30 minutes. Maybe we can let them set this one

class FocusModeTimer:
    def __init__(self, work_min=25, break_min=5):
        self.work_sec = work_min * 60
        self.break_sec = break_min * 60
        self.time_left = self.work_sec
        self.is_running = False
        self.mode = "Work" # Start in Work mode
        
        # Build the UI
        with ui.card().classes('w-64 items-center'):
            self.label = ui.label(self.mode).classes('text-h6')
            self.timer_display = ui.label(self.format_time()).classes('text-h3 font-mono')
            
            with ui.row():
                self.start_btn = ui.button('Start', on_click=self.start)
                ui.button('Reset', on_click=self.reset, color='red-5')

        # This is the NiceGUI way to handle loops without freezing the UI
        self.tick_timer = ui.timer(1.0, self.tick, active=False)

    def format_time(self):
        mins, secs = divmod(self.time_left, 60)
        return f"{mins:02d}:{secs:02d}"

    def start(self):
        self.is_running = not self.is_running
        self.tick_timer.active = self.is_running
        self.start_btn.text = 'Pause' if self.is_running else 'Resume'

    def reset(self):
        self.is_running = False
        self.tick_timer.active = False
        self.time_left = self.work_sec
        self.mode = "Work"
        self.update_ui()
        self.start_btn.text = 'Start'

    def tick(self):
        if self.time_left > 0:
            self.time_left -= 1
        else:
            # Switch modes when timer hits zero
            if self.mode == "Work":
                ui.notify("Time for a break!")
                self.mode = "Break"
                self.time_left = self.break_sec
            else:
                ui.notify("Back to work!")
                self.mode = "Work"
                self.time_left = self.work_sec
        
        self.update_ui()

    def update_ui(self):
        self.timer_display.text = self.format_time()
        self.label.text = self.mode

    # Instantiate the UI
    ui.label('Uncram Productivity Suite').classes('text-h4')
    FocusModeTimer()

    ui.run()

class DistractionBlocker:
    # This class is responsible for blocking distracting websites and apps during focus mode
    pass

class TaskAnalyticsDashboard:
    # This class is responsible for providing analytics and insights on task completion and productivity
    pass

class CollaborationHub:
    # This class is responsible for facilitating collaboration and communication among team members working on shared tasks
    pass

class AmbientFocusAid:
    # This class is responsible for providing ambient sounds and music to help users stay focused while working on tasks
    pass
