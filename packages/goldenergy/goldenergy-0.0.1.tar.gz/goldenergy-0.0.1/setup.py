from setuptools import setup, find_namespace_packages

setup(
    name="goldenergy",
    version="0.0.1",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    install_requires=[
        'python-dateutil',
        'aiohttp'
    ]
)
