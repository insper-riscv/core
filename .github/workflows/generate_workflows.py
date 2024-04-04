import os
import yaml


files = os.listdir('test')

yaml_content = {
        'name': f'VHD tests',
        'on': {
            'workflow_dispatch': {},
            'push': {
                'paths': [
                    f'src/**',
                    f'test/**',
                    f'.github/workflows/vhd_tests.yml'
                ]
            }
        },
        'jobs': {}
    }

for file in files:
    if not file.startswith('test'):
        continue

    yaml_content['jobs'][file[5:-3]] = {
        'name': f'{file[5:-3]}',
        'runs-on':'ubuntu-latest',
        'steps':  [
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
                        'name': 'Run Synthesis',
                        'run': f'pytest -k  {file[5:-3]} -m synthesis'
                    },
                    {
                        'name': 'Run Test Cases',
                        'run': f'pytest -k  {file[5:-3]} -m testcases'
                    }
                    
                ]
        }


filename = ".github/workflows/vhd_tests.yml"
with open(filename, 'w') as file_workflow:
    yaml.dump(yaml_content, 
              file_workflow, 
              default_flow_style=False,
              sort_keys=False
    )
