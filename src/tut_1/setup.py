from setuptools import find_packages, setup

package_name = 'tut_1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vijay',
    maintainer_email='vijay@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = tut_1.node_1:main",
            "circle = tut_1.circle:main",
            "pose_sub = tut_1.pose_sub:main",
            "tut_controller = tut_1.tut_controller:main"
        ],
    },
)
