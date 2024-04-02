import os
import yaml


files = os.listdir('test')

for file in files:
    if file.startswith('utils'):
        continue

    yaml_content = {
        'name': f'{file[5:-3]}',
        'on': {
            'workflow_dispatch': {},
            'push': {
                'paths': [
                    f'src/{file[5:-3]}.vhd',
                    f'test/{file}'
                ]
            }
        },
        'jobs': {
            'run-tests': {
                'name': f'{file[5:-3]}',
                'runs-on': 'ubuntu-latest',
                'steps': [
                    {
                        'name': 'Checkout code',
                        'uses': 'actions/checkout@v3'
                    },
                    {
                        'name': 'Install GHDL',
                        'uses': 'ghdl/setup-ghdl-ci@nightly',
                        'with': {
                            'backend': 'llvm'
                        }
                    },
                    {
                        'name': 'Set up Python',
                        'uses': 'actions/setup-python@v4',
                        'with': {
                            'python-version': '3.11',
                            'cache': 'pip'
                        }
                    },
                    {
                        'name': 'Install dependencies',
                        'run': 'pip install -r requirements.txt'
                    },
                    {
                        'name': 'Run pytest',
                        'run': 'pytest -s'
                    }
                ]
            }
        }
    }

    filename = ".github/workflows/" + os.path.splitext(file)[0][5:] + '.yml'
    with open(filename, 'w') as file_workflow:
        yaml.dump(yaml_content, 
                  file_workflow, 
                  default_flow_style=False,
                  sort_keys=False
        )
