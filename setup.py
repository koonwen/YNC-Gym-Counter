from setuptools import find_packages, setup

setup(
    name='app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
# TODO Package Properly
# TODO ADD CI/CD
# TODO Reivew pushing rights