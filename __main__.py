#This file is used for debugin puposes ONLY. This is not executed by KiCad.
import pcbnew
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))) # Ensure the parent directory is in the Python path for absolute imports
from .KiCadWorkdpaceOrganizer_action import KiCadWorkdpaceOrganizerAction, debug_init, debug_loop

debug_init()
KiCadWorkdpaceOrganizerAction().Run()
debug_loop()
