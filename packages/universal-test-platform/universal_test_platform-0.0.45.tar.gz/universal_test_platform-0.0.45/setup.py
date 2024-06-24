from setuptools import setup, find_packages

setup(
    name='universal-test-platform',
    version='0.0.45',

    package_dir  = {'': 'src'},
    package_data = {'utp': ['*','**/*.jar']},
    include_package_data=True,
    packages     = find_packages('src'),
    install_requires=['Click', 'pyyaml', 'robotlibcore-temp', 'robotframework-appiumlibrary', 'robotframework-seleniumlibrary', 'requests' ],
    entry_points={
        'console_scripts': [
            'utp = utp.utp:cli'
        ]
    }
)