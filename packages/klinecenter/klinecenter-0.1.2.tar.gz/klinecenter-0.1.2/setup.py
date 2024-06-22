from setuptools import setup, find_packages  
  
setup(  
    name='klinecenter',  
    version='0.1.2',  
    packages=find_packages(),  
    # url='https://github.com/your-github-username/your-package-name',  
    license='Your license',  
    # author='Your Name',  
    # author_email='your-email@example.com',  
    # description='A short description of your package',  
    install_requires=[  
        # List your dependencies here  
        'pandas',  
        'requests',  
        # ...  
    ],  
    # entry_points={  
    #     'console_scripts': [  
    #         'your-command = your_package.module:function',  
    #     ],  
    # },  
)