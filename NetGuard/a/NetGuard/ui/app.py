from __future__ import annotations

import os
import sys
import threading
import time
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

import customtkinter as ctk

# ----------------------------------------------------------------------
# Ancla de sys.path (respaldo: main.py ya lo hace). En el bundle
# __file__ es _MEIPASS/ui/app.py, por lo que parent.parent == raiz.
# ----------------------------------------------------------------------
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

# ----------------------------------------------------------------------
# Imports internos: ABSOLUTOS y SIN try/except.
# Quedan como dependencias inequivocas en el grafo de PyInstaller.
# ----------------------------------------------------------------------
from ui import theme
from ui.theme import (BG_BASE, BG_CARD, BG_DEEP, BG_ELEV, BG_PANEL, LedDot,
                      NeonButton, NeonFrame, ScanBar, StatCard, bind_tree,
                      device_icon, glyph_icon)

from ui.console import Console

from core import admin, arp, flood, latency, netinfo, oui, proc, scanner
from core.scanner import Device, State

APP = "NETGUARD"
VER = "2.0"