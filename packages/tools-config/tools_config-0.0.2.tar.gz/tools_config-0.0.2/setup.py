
import os
from setuptools import find_packages, setup
import glob

from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements
from version import __version__

if __name__ == '__main__':
    # parse_requirements() returns generator of pip.req.InstallRequirement objects
    os.environ['VERSION'] = __version__
    with open('tools_config/requirements.txt') as fd:
        data = fd.read()
        data = os.path.expandvars(data)

    with open('tools_config/requirements.txt', 'w') as fd:
        fd.write(data)

    install_reqs = parse_requirements('tools_config/requirements.txt', session=PipSession())

    extras_require = {}
    all_require = []
    extra_requirements = glob.glob('tools_config/requirements_*.txt')
    for extra_requirement in extra_requirements:
        extra_requirement_name = extra_requirement.replace('tools_config/requirements_', '').replace('.txt', '')
        extra_reqs = parse_requirements(extra_requirement, session=PipSession())
        extra_reqs = [str(ir.requirement) for ir in extra_reqs]
        extras_require[extra_requirement_name] = extra_reqs
        all_require.extend(extra_reqs)

    if len(all_require) > 0:
        extras_require['all'] = all_require

    reqs = [str(ir.requirement) for ir in install_reqs]

#    with open('tools_config/README.md', 'r') as fh:
#        _long_description = fh.read()

    setup(
        name='tools_config',
        version=__version__,
        packages=find_packages(include=['tools_config', 'tools_config.*']),
        install_requires=reqs,
        extras_require=extras_require,
        url='https://github.com/teesign/pipelib',
        license='',
        author='',
        author_email='',
        description='tools_config component of pipelib',
        long_description_content_type='text/markdown',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
        ],
        include_package_data=True,
        python_requires='>=3.6'
    )
  
