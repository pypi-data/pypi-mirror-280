from setuptools import setup, find_packages

setup(
    name="sphereobmodel",
    version="0.1.0",
    author="Anon",
    author_email="Anon@example.com",
    description="A utility to calculate and plot sphere-overburden EM response",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anonseg24/sphere_ob_response/tree/main",
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
            'sphereobmodel=sphereob.sphere_main:main',
        ],
    },
)
