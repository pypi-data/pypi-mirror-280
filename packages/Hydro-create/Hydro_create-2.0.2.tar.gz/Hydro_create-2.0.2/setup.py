from setuptools import setup
 
setup(
   name='Hydro_create',
   version='2.0.2',
   description='A useful module',
   author='Cloudann',
   author_email='cloudann@gmail.com',
   packages=['Hydro_create'],  #same as name
   install_requires=['pandas', 'xpinyin'], #external packages as dependencies
)