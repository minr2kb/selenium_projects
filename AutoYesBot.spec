# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['AutoYesBot.py'],
             pathex=['/Users/kbmin/Google 드라이브/WebDevelop/Selenium'],
             binaries=[],
             datas=[('chromedriver', '.'), ('MyVid.y4m', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='AutoYesBot',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
