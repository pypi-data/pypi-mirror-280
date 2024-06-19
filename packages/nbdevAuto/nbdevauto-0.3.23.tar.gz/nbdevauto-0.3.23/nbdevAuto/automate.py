# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_Automate.ipynb.

# %% auto 0
__all__ = ['prep', 'gacp', 'status', 'upload', 'reinstall', 'update', 'release_git', 'release_pypi', 'release', 'help_output',
           'everything', 'create_env', 'hello']

# %% ../nbs/01_Automate.ipynb 6
from fastcore.script import *

@call_parse
def prep(
    p:int = 2, # Increment Part
):
    "Export, test, and clean notebooks, and render README if needed"

    import nbdev.test, nbdev.clean, nbdev.quarto, nbdev.release
    nbdev.release.nbdev_bump_version(p)
    
    nbdev.quarto.nbdev_export.__wrapped__()
    print(f'### nbdev_export finished ###')
    nbdev.test.nbdev_test.__wrapped__(
        n_workers = 8,  # Number of workers
        timing = True,  # Time each notebook to see which are slow
    )
    print(f'### nbdev_test finished ###')
    nbdev.clean.nbdev_clean.__wrapped__()
    print(f'### nbdev_clean finished ###')
    nbdev.quarto.refresh_quarto_yml()
    print(f'### refresh_quarto_yml finished ###')
    nbdev.quarto.nbdev_readme.__wrapped__(chk_time=True)
    print(f'### nbdev_readme finished ###')

# %% ../nbs/01_Automate.ipynb 7
@call_parse
def gacp(
    m:str = '', # Commit message
):
    "git add, commit and push to github"
    
    import subprocess
    subprocess.run(["git", "add", "."])
    print(f'### git added ###')
    status = subprocess.check_output(["git", "status", "-s"]).decode('utf-8')
    print(f'### git status: "{status}" ###')

    if m != '':
        subprocess.run(["git", "commit", "-m", f'{m}'])
        print(f'### git commited "{m}"###')
    else:
        subprocess.run(["git", "commit", "-m", f'{status}'])
        print(f'### git commited status ###')
    subprocess.run(["git", "push"])
    print(f'### git pushed ###')

# %% ../nbs/01_Automate.ipynb 8
def status():
    "git status"
    import subprocess
    subprocess.run(["git", "status"])

# %% ../nbs/01_Automate.ipynb 9
@call_parse
def upload(    
    m:str = '', # Commit message
    p:int = 2, #Increment part
):
    "prep, then gacp"
    prep(p)
    gacp(m)

# %% ../nbs/01_Automate.ipynb 10
def reinstall():
    "runs pip install -e ."
    import subprocess
    subprocess.run(["pip", "install", "-e", "."])

# %% ../nbs/01_Automate.ipynb 11
def update():
    "prep, then reinstall"
    prep()
    reinstall()

# %% ../nbs/01_Automate.ipynb 13
def release_git():
    "release to git"
    import nbdev.release
    nbdev.release.nbdev_bump_version(1)
    nbdev.release.release_git()

# %% ../nbs/01_Automate.ipynb 14
def release_pypi():
    "release to pypi"
    import nbdev.release
    nbdev.release.release_pypi()

# %% ../nbs/01_Automate.ipynb 15
def release():
    "release to github and pip"
    release_git()
    release_pypi()

# %% ../nbs/01_Automate.ipynb 18
def help_output():
    "Show help for all console scripts"
    from fastcore.xtras import console_help
    console_help('nbdevAuto')

# %% ../nbs/01_Automate.ipynb 20
def everything():
    "prep, gacp, release, reinstall"
    upload()
    update()
    release()

# %% ../nbs/01_Automate.ipynb 22
@call_parse
def create_env(
    n:str = 'fast', #Name of the environment 
):
    "create conda env for AI"
    from pathlib import Path
    import subprocess
    
    subprocess.run(["conda", "create", "-n", f"{n}", "python"])
    subprocess.run(["conda", "init"])
    subprocess.run(["conda", "activate", f"{n}"], shell=True)
    # subprocess.run(["pip", "install", "fastai", "fastcore"])
    

# %% ../nbs/01_Automate.ipynb 23
def hello():
    import argparse
    parser = argparse.ArgumentParser(description='My CLI function.')
    parser.add_argument('-n', '--name', type=str, help='Name of the environment', default='fast')
    args = parser.parse_args()
    
    print(f'Hello, {args.name}!')
