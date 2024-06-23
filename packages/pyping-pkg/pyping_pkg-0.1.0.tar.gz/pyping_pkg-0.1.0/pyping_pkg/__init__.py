"""
Pyping_pkg
----------

    Pyping_pkg is a module used to check projects PyPi web site informations as if already exists and your respective versions.

    This module also is prepared to leading you to upload your own python module project on PyPi repository.

    Can we try? Let's go!

Best regards from Natanael Quintino
"""

import os
import re
import requests
from .scriptsText import setupScript, tomlScript, mitLicenseScript, readmeScript
from metadata import metadata


__version__ = "0.1.0"
__all__ = [
    "exists", "getVersions", "uploadPackage", "buildProject",
    "pyping"
    ]


def prepareRequirements(requirements: str) -> (str):
    requirements = requirements.split(",")
    for i, req in enumerate(requirements):
        requirements[i] = f"'{req.strip()}'"
    return ", ".join(requirements)


def getKey(dic, key, func, *args):

    value = dic[key]\
        if key in dic\
        else func(*args)

    return value


def exists(package: str, verbose: bool = False) -> (bool):
    response = requests.get(f"https://pypi.org/project/{package}")
    unavailable = response.status_code == 200
    if unavailable and verbose:
        print(
        f"Unfortunately, '{package}' already exists in the Pypi repository."
        )
    elif verbose:
        print(
        f"Fortunately, '{package}' does not exist in Pypi repository!"
        )

    return unavailable


def getVersions(package) -> (list[str]):
    response = requests.get(f"https://pypi.org/project/{package}/#history")

    versions = re.findall(
        "\<p class=\"release__version\"\>\s*(.*)\s*\<\/p\>",
        response.text
    )

    # # Get lines from response text content
    # contentLines = response.text.split("\n")

    # # Get versions index on contentLines
    # versionsIdx = [
    #     i+1 for i, t in enumerate(contentLines)
    #         if '<p class="release__version">' in t
    # ]

    # # Get versions from contentLines
    # versions = [contentLines[i].strip() for i in versionsIdx]

    return versions


def generateSetup(module, path) -> (None):
    """Generate setup.py file"""

    printed = False
    while exists(module, verbose=True):
        module=input("Type the pymodule name: ")
        printed = True

    if not printed:
        print("Type the pymodule ", end="")

    description = getKey(
        metadata[module],
        "description",
        input,
        "           description: "
    )
    author = getKey(
        metadata[module],
        "author",
        input,
        "           author name: "
    )
    author_email = getKey(
        metadata[module],
        "author_email",
        input,
        "          author email: "
    )
    license = getKey(
        metadata[module],
        "license",
        input,
        "               license: "
    )
    requirements = getKey(
        metadata[module],
        "requirements",
        input,
        " packages requirements: "
    )
    keywords = getKey(
        metadata[module],
        "keywords",
        input,
        "              keywords: "
    )
    long_description = description

    path = path.rstrip("/")

    if "setup.py" in os.listdir(path):
        print("setup.py already exists!")
        answer = input("Do you wanna update 'setup.py'? (Y/n) ")
        if "n" in answer.lower():
            return None

    with open("{path}/setup.py", "x") as f:
        f.write(
            setupScript.format(
                module=module, description=description,
                long_description=long_description, author=author,
                author_email=author_email, license=license,
                requirements=prepareRequirements(requirements),
                keywords=keywords,
            )
        )

    return None


def generateToml(module, path) -> (None):
    """Generate <module>.toml file"""

    printed = False
    while exists(module, verbose=True):
        module=input("Type the pymodule name: ")
        printed = True

    if not printed:
        print("Type the pymodule ", end="")

    description = getKey(
        metadata[module],
        "description",
        input,
        "     description: "
    )
    author = getKey(
        metadata[module],
        "author",
        input,
        "     author name: "
    )
    author_email = getKey(
        metadata[module],
        "author_email",
        input,
        "    author email: "
    )
    license = getKey(
        metadata[module],
        "license",
        input,
        "         license: "
    )
    githubUserName = getKey(
        metadata[module],
        "githubUserName",
        input,
        " github UserName: "
    )

    path = path.rstrip("/")

    if f"{module}.toml" in os.listdir(path):
        print(f"{module}.toml already exists!")
        answer = input(f"Do you wanna update '{module}.toml'? (Y/n) ")
        if "n" in answer.lower():
            return None

    with open("{path}/{module}.toml", "w") as f:
        f.write(
            tomlScript % {
                "module": module,
                "author": author,
                "author_email": author_email,
                "description": description,
            }
        )

    return None


def generateReadme(module, path) -> (None):
    """Generate README.md file"""

    printed = False
    while exists(module, verbose=True):
        module=input("Type the pymodule name: ")
        printed = True

    if not printed:
        print("Type the pymodule ", end="")

    description = getKey(
        metadata[module],
        "description",
        input,
        "     description: "
    )

    path = path.rstrip("/")

    if f"README.md" in os.listdir(path):
        print(f"README.md already exists!")
        answer = input(f"Do you wanna update 'README.md'? (Y/n) ")
        if "n" in answer.lower():
            return None

    with open("{path}/README.md", "w") as f:
        f.write(
            readmeScript.format(
                module=module, description=description
            )
        )

    return None


def generateMitLicense(module, path) -> (None):
    """Generate LICENSE file"""

    author = getKey(
        metadata[module],
        "author",
        input,
        "Type the pymodule author name: "
    )

    path = path.rstrip("/")

    if f"LICENSE" in os.listdir(path):
        print(f"LICENSE already exists!")
        answer = input(f"Do you wanna update 'LICENSE'? (Y/n) ")
        if "n" in answer.lower():
            return None

    with open("{path}/LICENSE", "w") as f:
        f.write(
            mitLicenseScript.format(
                author=author
            )
        )

    return None


def generateAllFiles(module, path):
    """Generate setup.py, <module>.toml, README.md and LICENSE files"""

    printed = False
    while exists(module, verbose=True):
        module=input("Type the pymodule name: ")
        printed = True

    if not printed:
        print("Type the pymodule ", end="")

    description = getKey(
        metadata[module],
        "description",
        input,
        "                  description: "
    )
    author = getKey(
        metadata[module],
        "author",
        input,
        "                  author name: "
    )
    author_email = getKey(
        metadata[module],
        "author_email",
        input,
        "                 author email: "
    )
    license = getKey(
        metadata[module],
        "license",
        input,
        "                      license: "
    )
    requirements = getKey(
        metadata[module],
        "requirements",
        input,
        "        packages requirements: "
    )
    keywords = getKey(
        metadata[module],
        "keywords",
        input,
        "                     keywords: "
    )
    githubUserName = getKey(
        metadata[module],
        "githubUserName",
        input,
        "              github UserName: "
    )
    long_description = description

    # Remove / from path
    path = path.rstrip("/")

    for fileName in ["setup.py", f"{module}.toml", "README.md", "LICENSE"]:

        if fileName in os.listdir(path):
            print(f"'{fileName}' already exists!")
            answer = input(f"Do you wanna update '{fileName}'? (Y/n) ")
            if "n" in answer.lower():
                continue

        script = {
            "setup.py": setupScript,
            f"{module}.toml": tomlScript,
            "README.md": readmeScript,
            "LICENSE": mitLicenseScript
        }[fileName]

        # from pyidebug import debug
        # debug(globals(), locals())
        # input("HERE")

        with open(f"{path}/{fileName}", "w") as f:

            if fileName.endswith(".toml"):
                # Formattin toml file
                script = script % {
                    "module": module,
                    "author": author,
                    "author_email": author_email,
                    "description": description,
                }

            else:
                # Formatting file text content
                script = script.format(
                        module=module, description=description,
                        long_description=long_description, author=author,
                        author_email=author_email, license=license,
                        requirements=prepareRequirements(requirements),
                        keywords=keywords, githubUserName=githubUserName
                    )

            # Write content on file
            f.write(
                script.strip("\t\n ")
            )

    return None


def buildProject(
        module: str = None,
        version: str = None,
        path: str = None
        ) -> (None):

    if module is None or exists(module, verbose=True):
        while exists(module:=input("Type the pymodule name: "), verbose=True):
            pass
    versions = getVersions(module)
    if version is None or version in versions:
        while (version:=input("Type the pymodule version: ").strip(" .")) in versions:
            pass
    if path is None:
        path = input("Type the pymodule main path: ")

    path = "."\
        if not any(path)\
        else path.rstrip(r"/")

    module = module.lower().replace("-","_")
    for file, toChange in [(f"{path}/setup.py", "VERSION = "),
                 (f"{path}/{module}.toml", "version = "),
                 (f"{path}/{module}/__init__.py", "__version__ = ")]:

        with open(file, "r+") as f:
            content = f.readlines()
            for i, c in enumerate(content):
                if toChange in c:
                    pos = c.find('"')
                    newVersionLine = c[:pos+1] + version + '"\n'

                    if not newVersionLine.startswith(toChange):
                        continue

                    content[i] = newVersionLine
                    break
            f.seek(0)
            f.write("".join(content))

    os.system(
        " && ".join([
            f"cd {path}",               # Go to package folder folder
            #"python3 -m build --sdist", # Compacting package file
            "python3 setup.py sdist",   # Compacting package file
        ])
    )

    return None


def uploadPackage(module, path, version):
    "Upload module to PyPI repository"

    # Check if module already exists in PyPI repository
    exists(module)

    out = os.system(
        f"python3 -m twine upload {path}/dist/*{version}.tar.gz",
    )

    return out


def removeCompactedFiles(path):
    "Remove compacted files"

    os.system(
        f"rm -R {path}/dist"
    )

    return None


def pyping(
        module: str,
        version: str,
        path: str,
        createAllFiles: bool = False
        ) -> (None):

    if createAllFiles:
        generateAllFiles(module, path)
    buildProject(module, version, path)
    uploadPackage(module, path, version)
    #removeCompactedFiles(path)

    return None