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
    pass

class DistractionBlocker:
    # This class is responsible for blocking distracting websites and apps during focus mode
    class DistractionBlocker:
   # This class manages a list of distracting apps and websites
    # Activates when the Pomodoro task completion session begins
    # 

    BLOCKED_SITES = [

        "youtube.com",
        "twitter.com",
        "reddit.com",
        "instagram.com",
        "facebook.com",
        "tiktok.com",
        "twitch.tv",
        "netflix.com",

    ]

    def __init__(self):

        self.blocked_sites: list[str] = list(self.BLOCKED_SITES)
        self.is_active = False
        self.log_entries: list[str] = []
        self._build_ui()

    # UI 

   def _build_ui(self):

    with ui.card().classes('blocker-card'):

        self._build_header()

        ui.separator().classes('q-my-sm')

        self._build_blocklist_section()

        ui.separator().classes('q-my-sm')

        self._build_log_section()

def _build_header(self):

    with ui.row().classes('blocker-header'):

        ui.icon('shield', size = 'sm').classes('shield-icon')

        ui.label('Distraction Blocker').classes('blocker-title')

        self.status_chip = ui.chip(
            'INACTIVE', icon = 'lock_open'
        ).classes('status-chip inactive')

def _build_blocklist_section(self):

    with ui.column().classes('full-width gap-xs'):

        ui.label('Blocked Sites').classes('section-label')

        self.site_list_container = ui.column().classes('site-list')

        self._render_site_list()

        self._build_add_site_row()

def _build_add_site_row(self):

    with ui.row().classes('full-width items-center gap-xs add-row'):

        self.new_site_input = ui.input(
            placeholder = 'add a site (i.e. yahoo.com)'
        ).classes('site-input').props('dense outlined')
        ui.button(
            icon='add', on_click=self._add_site
        ).props('flat dense').classes('add-btn')

def _build_log_section(self):

    with ui.column().classes('full-width space-xs'):

        ui.label('Session Log').classes('section-label')

        self.log_container = ui.column().classes('log-box')

        self._render_log()

            # Manager for blocklist
            with ui.column().classes('full-width gap-xs'):
                ui.label('Blocked Sites').classes('section-label')

                self.site_list_container = ui.column().classes('site-list')
                self._render_site_list()




class TaskAnalyticsDashboard:
    # This class is responsible for providing analytics and insights on task completion and productivity
    pass

class CollaborationHub:
    # This class is responsible for facilitating collaboration and communication among team members working on shared tasks
    pass

class AmbientFocusAid:
    # This class is responsible for providing ambient sounds and music to help users stay focused while working on tasks
    pass

