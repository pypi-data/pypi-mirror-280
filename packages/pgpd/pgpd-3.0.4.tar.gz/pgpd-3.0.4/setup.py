import setuptools as setup

import versioneer


def find_packages():
    return ['pgpd'] + ['pgpd.' + p for p in setup.find_packages('pgpd')]


requirements = [
    'pandas>=1.1',
    'shapely>=2.0.0',
]

setup.setup(
    name='pgpd',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='0phoff',
    description='Shapely ExtensionArray for pandas',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    test_suite='test',
    install_requires=requirements,
)
