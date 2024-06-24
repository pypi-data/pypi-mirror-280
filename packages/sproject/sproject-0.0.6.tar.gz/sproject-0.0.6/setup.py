from setuptools import setup, find_packages
setup(
    name='sproject',  # Replace with your desired package name
    version='0.0.6',  # Version number (update for future releases)
    description='Fixed many bugs in the project.',
    author='Grand Master',
    packages=find_packages(),  # Automatically finds your package
    install_requires=['pycryptodome','tqdm']  # Add any external dependencies here (if needed)
)