import setuptools

with open('README.md', 'rt') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    install_reqs = [
        s for s in [
            line.strip(' \n') for line in f
        ] if not s.startswith('#') and s != ''
    ]

setuptools.setup(
    name='crix',
    version='1.0',
    author='Baryshnikov Aleksandr (reddec)',
    author_email='ab@crix.io',
    description='CRIX.IO official client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blockwise/crix-client-py',
    packages=setuptools.find_packages(),
    install_requires=install_reqs,
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'License :: Other/Proprietary License',
        'Topic :: Office/Business :: Financial'
    ]
)