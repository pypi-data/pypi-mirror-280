from setuptools import setup, find_packages

VERSION = '0.3.3'
DESCRIPTION = 'sdk for duwi third platform'

setup(
    name="duwi_smarthome_sdk_dev",
    version=VERSION,
    author="duwi",
    author_email="ledgerbiggg@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md', encoding="UTF8").read(),
    packages=find_packages(),
    install_requires=['websockets', 'aiohttp'],
    keywords=['python', 'duwi', 'sdk', 'third', 'platform'],
    entry_points={
        'console_scripts': [
            'duwi = duwi_smarthome_sdk_dev.main:main'
        ]
    },
    license="MIT",
    url="https://github.com/duwi2024/homeassistant-sdk",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)
