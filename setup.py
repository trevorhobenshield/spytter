from textwrap import dedent

from setuptools import find_packages, setup

install_requires = [
    "aiofiles",
    "websockets",
    "nest_asyncio",
    "httpx",
    "orjson",
    "tqdm",
    'uvloop; platform_system != "Windows"',
]

setup(
    name="spytter",
    version="0.0.0",
    python_requires=">=3.10.10",
    description="Twitter Spy Tools",
    long_description=dedent('''

    ### Twitter Spy Tools

    Capture live data from Twitter Spaces

    - asynchronously capture live audio and transcripts for 500 streams per IP
    - search Live, Upcoming, and Top streams by keyword

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
