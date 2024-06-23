import threading

from rich.console import Group
import rich.progress as rp




overall_progress = rp.Progress(
    rp.TextColumn("[bold blue]{task.description}", justify="right"),
    rp.BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    rp.TextColumn("[blue]{task.completed}/{task.total}", justify="center"),
    "•",
    "Elapsed:", rp.TimeElapsedColumn(),
    "•",
    "eta:", rp.TimeRemainingColumn(),
)


current_progress = rp.Progress(
    rp.TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    rp.BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    rp.DownloadColumn(),
    "•",
    rp.TransferSpeedColumn(),
    "•",
    "Elapsed:", rp.TimeElapsedColumn(),
    "•",
    "eta:", rp.TimeRemainingColumn(),
)


progress_group = Group(
    current_progress,
    overall_progress,
)



class ProgressPercentage(object):
    '''It is the Progress Updater class used in Uploading and Downloading objects from S3.'''
    
    def __init__(self, prog_id):
        self.id = prog_id
        self._lock = threading.Lock()
 
    def __call__(self, bytes_amount):
        with self._lock:
            current_progress.update(self.id, advance=bytes_amount)