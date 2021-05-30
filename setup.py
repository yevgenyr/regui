# ========globals=========
author = "Yevgeny Rakita"
email = "yr2369@columbia.edu"

pkg_name = 'regui'
version = "0.1.0"
description = "regui - a lightweight gui for regolith" 
url = "git@github.com:yevgenyr/regui.git"
alias = "regui"
rel_ex_path = [pkg_name, "main"]


def install():
    install_dependencies()
    main_installation()


def install_dependencies():
    import subprocess as sp
    import os

    # path_to_conda = os.path.join('.', 'requirements', 'conda.txt')
    path_to_pip = os.path.join('.', 'requirements', 'pip.txt')

    # sp.run(f"conda install --yes --channel conda-forge --file {path_to_conda}", shell=True)
    sp.run(f"pip install -r {path_to_pip}", shell=True)


def main_installation():
    import setuptools
    # read long description from README
    with open("README.md", "r") as fh:
        long_description = fh.read()
    # create setuptools dict
    _setup = dict(
        name=pkg_name,
        version=version,
        author=author,
        author_email=email,
        description=description,
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=url,
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT",
            "Operating System :: OS Independent",
        ],
        entry_points={
            # define console_scripts here, see setuptools docs for details.
            'console_scripts': [
                f'{alias} = {".".join(rel_ex_path)}:main',
            ]
        },
        data_files=[("", ["LICENSE.txt", "README.md"])],
        include_package_data=False,
        package_data={"": ['*.yml', '*.pye']},
        python_requires='>=3.7',
        zip_safe=False, )

    setuptools.setup(**_setup)


# ======INSTALL======
install()
