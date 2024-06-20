from setuptools import setup, find_packages

setup(
    name="Systemadminbd-WebTool",
    version="1.1",
    author="Red hair shanks",
    author_email="admin@systemadminbd.com",
    description="A Powerful webtool from Systemadminbd",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://systemadminbd.com",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='webtool systemadminbd development Abir',
    project_urls={
        'Documentation': 'https://systemadminbd.com/',
        'Tracker': 'https://t.me/systemadminbdbot',
    },
    python_requires='>=3.7',
    install_requires=[
        'aiohttp',
        'asyncio',
        'requests',
        'colorama',
        'rich',
        'lolcat',
        'tqdm',
        'termcolor',
        'fake_useragent',
        'beautifulsoup4',
        'chardet',
        'urllib3',
        'aiofiles'
    ],
    entry_points={
        'console_scripts': [
            'systemadminbd-webtool=WebTool.test:async_main',  # Adjust path and function name as needed
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
