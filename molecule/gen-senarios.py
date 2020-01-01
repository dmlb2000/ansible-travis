#!/usr/bin/python
import os
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from jinja2 import Template

def main():
    """Main method."""
    molecule_dir = os.path.dirname(__file__)
    molecule_senario = Template(open(os.path.join(molecule_dir, 'common', 'molecule.yml.j2')).read())
    python_versions = ['3.6', '3.7', '3.8']
    repository_list = []
    with open(os.path.join(molecule_dir, '..', 'vars', 'main.yml'), 'r') as vars_fd:
        repository_list = load(vars_fd, Loader=Loader).get('github_repository_dependencies', {}).keys()
    for python_version in python_versions:
        for repository in repository_list:
            os.makedirs(os.path.join(molecule_dir, '{}-python{}'.format(repository, python_version)), exist_ok=True)
            with open(os.path.join(molecule_dir, '{}-python{}'.format(repository, python_version), 'molecule.yml'), 'w') as mole_fd:
                mole_fd.write('{}\n'.format(molecule_senario.render(
                    repository=repository,
                    python_version=python_version
                )))

if __name__ == '__main__':
    main()