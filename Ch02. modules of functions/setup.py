from distutils.core import setup

setup(
        name         = 'nester',
        version      = '1.4.0',
        py_modules   = ['nester'],
        author       = 'sijeon',
        author_email = 'si.j@navercorp.com',
        url          = 'http://www.naver.com',
        description  = 'Test - A simple printer of nested lists',
     )

# Build your distribution
# $ python3 setup.py sdist

# Install your distribution into your local copy of Python
# $ sudo python3 setup.py install --record files.txt

# Upload your code to PyPI
# Registering (only once)
# $ python3 setup.py register
# Uploading modules
# $ python3 setup.py sdist upload
