

from PyInstaller.utils.hooks import collect_submodules

import beets

BEETS_PATH = beets.__path__[0]

block_cipher = None

# Add beets and plugins modules
hidden = []
hidden.extend(collect_submodules("beetsplug"))
hidden.extend(collect_submodules("beets"))

a = Analysis(['beets\\__main__.py'],
             binaries=[],
             datas=[],
             hiddenimports=hidden,
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)



# Collect data files, like config_default.yml
non_data_ext = ["*.pyc", "*.py", "*.dll", "*.so", "*.dylib"]
a.datas += Tree(BEETS_PATH, "beets", excludes=non_data_ext)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='beets',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
