from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'stspimoroni'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mark',
    maintainer_email='ligalog@icloud.com',
    description='package to start up sts pimoroni kit using explorerhat',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sts = stspimoroni.stspimoroni:main'
        ],
    },
)
