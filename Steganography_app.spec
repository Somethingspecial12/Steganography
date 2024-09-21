# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Steganography_app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('mainpage.py', '.'), 
        ('encode_page.py', '.'), 
        ('decode_page.py', '.'), 
        ('dialogclass.py', '.'), 
        ('dialog.py', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Steganography_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Steganography_app',
)
