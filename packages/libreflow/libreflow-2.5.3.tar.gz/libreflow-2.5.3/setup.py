import setuptools
import versioneer
import os

readme = os.path.normpath(os.path.join(__file__, '..', 'README.md'))
with open(readme, "r", encoding="utf-8") as fh:
    long_description = fh.read()

long_description += '\n\n'

changelog = os.path.normpath(os.path.join(__file__, '..', 'CHANGELOG.md'))
with open(changelog, "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    cmdclass=versioneer.get_cmdclass(),
    name="libreflow", # Replace with your own username
    version=versioneer.get_version(),
    author="Flavio Perez",
    author_email="flavio@lfs.coop",
    description="An example flow for kabaret",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/lfs.coop/libreflow",
    license="LGPLv3+",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    keywords="kabaret cgwire kitsu gazu animation pipeline libreflow",
    install_requires=["kabaret>=2.3.0rc6",
                      "pyside2~=5.0",
                      "six~=1.0",
                      "kabaret.script-view",
                      "kabaret.subprocess-manager>=1.1.0",
                      "kabaret.flow-contextual-dict",
                      "kabaret.flow-entities",
                      "gazu>=0.8.33",
                      "minio",
                      "timeago",
                      "blender-asset-tracer",
                      "psutil",
                      "fileseq",
                      "sentry-sdk"
                      ],
    python_requires='>=3.7',
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    package_data={
        '': [
            "*.css",
            '*.png',
            '*.svg',
            '*.gif',
            '*.abc',
            '*.aep',
            '*.ai',
            '*.blend',
            '*.jpg',
            '*.kra',
            '*.mov',
            '*.psd',
            '*.psb',
            '*.txt',
            '*.usd',
            '*.fbx',
            '*.json',
            '*.obj',
            '*.wav',
            '*.pproj',
            '*.ttf',
            '*.otf',
            '*.nk',
            '*.jsx',
            '*.mp4'
        ],
    },
)