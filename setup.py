from setuptools import find_packages,setup

hiphen="-e ."
def get_requirements(file_path:str):
    ''' This function returns list of requirements'''

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hiphen in requirements:
            requirements.remove(hiphen)

    return requirements


setup(
    name="machine learning projects",
    version="0.0.1",
    author="PNMR",
    author_email="nagamallirgukt@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)