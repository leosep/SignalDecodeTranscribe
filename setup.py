from setuptools import setup, find_packages

setup(
    name="433mhz-audio-decoding",
    version="0.1",
    packages=find_packages(where='src'),
    install_requires=[
        'openai-whisper',
        'pydub',
        'scipy',
        'numpy',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'rf-audio-decoding = src.main:main'
        ]
    },
)
