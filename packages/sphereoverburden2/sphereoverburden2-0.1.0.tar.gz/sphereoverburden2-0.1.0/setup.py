from setuptools import setup, find_packages

setup(
    name="sphereoverburden2",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A utility to calculate and plot sphere-overburden EM response",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="http://github.com/yourusername/sphereresponse",
    packages=find_packages(),
    install_requires=[
        'PyQt5', 'numpy', 'matplotlib', 'pandas', 'scipy'
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'spheremain2=sphereob.sphere_main:main',
        ],
    },
)
