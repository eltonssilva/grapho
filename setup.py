from cx_Freeze import setup, Executable
 
setup(name='IluGraph',
    version='1.0',
    description='Grago Iluflex',
    options={'build_exe': {'packages': ['matplotlib']}},
    executables = [Executable(
                   script='main_g.py',
                   base=None,
                   icon='my-icon.ico'
                   )]
)