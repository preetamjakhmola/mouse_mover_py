import PyInstaller.__main__
import os
import sys

def build_executable():
    # Get the directory containing this script
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(bundle_dir)
    
    # Path to the main script
    main_script = os.path.join(project_dir, 'mouse_mover.py')
    
    # Output directory
    dist_dir = os.path.join(bundle_dir, 'dist')
    build_dir = os.path.join(bundle_dir, 'build')
    
    PyInstaller.__main__.run([
        main_script,
        '--onefile',
        '--console',
        '--name=MouseMover',
        f'--distpath={dist_dir}',
        f'--workpath={build_dir}',
        '--clean'
    ])

if __name__ == '__main__':
    build_executable()