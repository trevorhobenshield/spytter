from textwrap import dedent

from setuptools import find_packages, setup

install_requires = [
    "websockets",
    "nest_asyncio",
    "aiohttp",
    "httpx",
    "tqdm",
    "orjson",
    "requests",
    "bcrypt",
    "python-gnupg",
    "pyopenssl",
    'uvloop; platform_system != "Windows"',
]

setup(
    name="spytter",
    version="0.0.0",
    python_requires=">=3.10.10",
    description="Twitter Spy Tools",
    long_description=dedent('''
    
    Capture live data from Twitter Spaces
    
    - live audio capture
    - live transcript capture
    - ability to download streams from playback-disabled spaces
    - keyword search

    '''),
    long_description_content_type='text/markdown',
    author="Trevor Hobenshield",
    author_email="trevorhobenshield@gmail.com",
    url="https://github.com/trevorhobenshield/spytter",
    install_requires=install_requires,
    keywords="twitter api spaces audio stream capture client automation bot scrape",
    packages=find_packages(),
    include_package_data=True,
)
