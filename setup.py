from setuptools import findpackages,setup
from typing import List
hyphen = '-e.'


def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of packages.
    """
    requirements=[]
    with open(file_path)as myfile:
       requirements=myfile.readlines()
       requirements=[req.replace("\n"," ")for req in requirements] 

        if hyphen in requirements:
            requirements.remove(hyphen)


    return requirements




setup(
    name='mlproject',
    version='0.0.1',
    author = 'siva',
    author_email = 'botinasivanagaraju5@gmail.com',
    packages=findpackages(),
    install_requires = get_requirements(requirments.txt)

)