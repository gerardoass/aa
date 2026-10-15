# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec - NetGuard v2.0
--------------------------------
Un unico .exe en modo ventana (sin consola), con manifest UAC admin.

Puntos clave del empaquetado:
  * pathex = raiz del proyecto (SPECPATH) para que `ui` y `core` se
    resuelvan como paquetes y no como modulos sueltos.
  * collect_submodules("ui") / collect_submodules("core") garantizan que
    ui.theme, ui.console, ui.app y todos los modulos de core entren al
    bundle con su nombre de paquete correcto, sin depender de que el
    analizador siga imports relativos.
  * Se compila con:  pyinstaller --clean --noconfirm netguard.spec
"""
import os

from PyInstaller.utils.hooks import collect_all, collect_submodules

# ----------------------------------------------------------------------
# Dependencias de terceros: datos + binarios + submodulos ocultos
# ----------------------------------------------------------------------
scapy_d, scapy_b, scapy_h = collect_all("scapy")
ctk_d, ctk_b, ctk_h = collect_all("customtkinter")
pil_d, pil_b, pil_h = collect_all("PIL")

# ----------------------------------------------------------------------
# Paquetes propios de NetGuard: inclusion garantizada
# ----------------------------------------------------------------------
ui_h = collect_submodules("ui")
core_h = collect_submodules("core")

hidden = (
    scapy_h
    + ctk_h
    + pil_h
    + ui_h
    + core_h
    + collect_submodules("scapy.layers")
    + [
        "scapy.arch.windows",
        "scapy.layers.l2",
        "scapy.layers.inet",
        "scapy.sendrecv",
        "PIL._tkinter_finder",
    ]
)

# ----------------------------------------------------------------------
# Analisis
# ----------------------------------------------------------------------
a = Analysis(
    ["main.py"],
    pathex=[os.path.abspath(SPECPATH)],
    binaries=scapy_b + ctk_b + pil_b,
    datas=scapy_d + ctk_d + pil_d,
    hiddenimports=hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "matplotlib",
        "numpy.testing",
        "pytest",
        "IPython",
        "PyQt5",
        "PyQt6",
        "PySide2",
        "PySide6",
    ],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="NetGuard",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=True,
    icon="icono.ico",
)