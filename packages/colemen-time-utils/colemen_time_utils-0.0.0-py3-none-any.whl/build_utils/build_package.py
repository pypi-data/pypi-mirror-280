



import base64
from encodings import utf_8
import os
from pathlib import Path, PurePath
import re
from string import Template
import sys
import subprocess
# import colemen_utils as c


def write_file(path,content):
    f = open(path, "w",encoding=None)
    f.write(content)
    f.close()

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)

def venv_path():
    cwd = os.getcwd()
    return PurePath(f"{cwd}/.venv").as_posix()

def increment(release_type:str):
    '''
    Read the setup.py file and parse the contents to locate the release version and increment
    the correct digit.


    Arguments
    -------------------------
    `release_type` {str}
        This is used to specify which digit should be incremented, the options are:

        - major
        - minor
        - patch



    '''
    
    # print(f"vpath: {vpath}")
    setup_path = f"{venv_path()}/setup.py"
    print(f"setup_path: {setup_path}")
    # setup = c.file.readr(setup_path)
    setup = str(open(setup_path, "r",encoding=None))
    match = re.findall(r"((VERSION)\s*=\s*'([0-9]*).([0-9]*).([0-9]*)')",setup,re.IGNORECASE)
    version_string = "VERSION"
    if len(match) > 0:
        match = match[0]
        version_string = match[1]
        major = int(match[2])
        minor = int(match[3])
        patch = int(match[4])
        if release_type.lower() == "major":
            major = int(match[2]) + 1
        if release_type.lower() == "minor":
            minor = int(match[3]) + 1
        if release_type.lower() == "patch":
            patch = int(match[4]) + 1

        new_version = f"{version_string}='{major}.{minor}.{patch}'"
        setup = setup.replace(match[0],new_version)

        # f = open(setup_path, "w")
        # f.write(setup)
        # f.close()
        print(f"SAVING: setup_path: {setup_path}")
        write_file(setup_path,setup)
        # c.file.write(setup_path,setup)

def create_master_batch(pypi_upload=False):
    '''
        Create the master batch file, this bad boy executes the setup.py to compile the package and upload to pypi

        ----------

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 02-25-2023 11:02:29
        `memberOf`: build_package
        `version`: 1.0
        `method_name`: create_master_batch
        * @xxx [02-25-2023 11:03:18]: documentation for create_master_batch
    '''

    pp = PurePath(Path(os.getcwd()))
    drive_letter = pp.drive
    # venv_path = pp.as_posix()
    batch_name = "master_batch.bat"
    batch_path = f"{venv_path()}/build_utils/{batch_name}"


    ZvKlMuDG3zLh="cjE0NjAyMw=="
    Xwvy8ZgAshQW="UjE0NlJhY29tcGxleDMhNTE3MU5vdmF0dXJpZW50IQ=="


    pypi_template = ''
    if ZvKlMuDG3zLh != "none":
        ZvKlMuDG3zLh = base64.b64decode(ZvKlMuDG3zLh.encode("ascii")).decode("ascii")
        Xwvy8ZgAshQW = base64.b64decode(Xwvy8ZgAshQW.encode("ascii")).decode("ascii")



        # pypi_template = f''' && twine upload dist/* -u {ZvKlMuDG3zLh} -p {Xwvy8ZgAshQW}'''
        pypi_template = f''' && twine upload dist/* -u __token__ -p "pypi-AgEIcHlwaS5vcmcCJDRjNzEyMDgzLWFlMjItNDFmZC04YjJjLTZiMzRjMjk2NzE5OAACKlszLCIxMGI2ZDE1ZC1iYzM1LTQ3MmMtOTY4Yy1kOTRlOWQ2MGNiNDgiXQAABiDTRclT24IPkX2IF3mlbgjVfmgx2qLBcBaps-egzXveQg"'''
    if pypi_upload is False:
        pypi_template = ''

    upload_template = f'''cmd /c "$drive_letter" & cd "$venv_path" & "Scripts/activate.bat" & python "setup.py" sdist bdist_wheel{pypi_template}'''

    s = Template(upload_template)
    batch = s.substitute(
        drive_letter=drive_letter,
        venv_path=venv_path(),
    )

    # c.file.write(batch_path,batch)
    write_file(batch_path,batch)
    return batch_path

def create_release_batches():

    releases = ["major","minor","patch"]
    template = '''
    cmd /c "$drive_letter" & cd "$venv_path" & "Scripts/activate.bat" & python "build_utils/build_package.py" $release
    '''


    for release in releases:
        # print(f"os.getcwd(): {os.getcwd()}\.venv")
        pp = PurePath(Path(os.getcwd()))
        drive_letter = pp.drive
        ven_path = venv_path()
        
        batch_name = f"{release}_release.bat"
        batch_path = f"{ven_path}/build_utils/{batch_name}"
        # print(f"cwd: {os.getcwd()}")
        # print(f"venv_path: {venv_path}")
        # print(f"batch_path: {batch_path}")

        s = Template(template)
        batch = s.substitute(
            drive_letter=drive_letter,
            venv_path=ven_path,
            release=release,
        )
        write_file(batch_path,batch)
        # c.file.write(batch_path,batch)

def main(release):
    # @Mstep [] (re)create the release batches
    create_release_batches()
    # @Mstep [] increment the setup.py version
    increment(release)
    # @Mstep [] generate the master batch file.
    batch_path = create_master_batch(True)

    # @Mstep [] execute the master batch file
    subprocess.run([batch_path])
    # @Mstep [] delete the master batch file.
    # c.file.delete(batch_path)
    # delete_file(batch_path)

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        args = ['','patch']
    main(args[1])

