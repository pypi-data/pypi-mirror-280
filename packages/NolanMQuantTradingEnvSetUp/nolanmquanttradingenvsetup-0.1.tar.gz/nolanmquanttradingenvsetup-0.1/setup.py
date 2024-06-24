from setuptools import setup, find_packages

setup(
    name='NolanMQuantTradingEnvSetUp',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'setup-env=NolanMQuantTradingEnvSetUp.setup:main',
        ],
    },
)
