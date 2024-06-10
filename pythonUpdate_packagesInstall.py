# pythonUpdate_packagesInstall.py

# update python and install numpy, matplotpy, alg, math and necessary commonly used packages

# update python and install numpy, matplotlib, alg, math and necessary commonly used packages
import subprocess

# update pip
subprocess.run(['pip', 'install', '--upgrade', 'pip'])

# Update Python
subprocess.run(['pip', 'install', '--upgrade', 'python'])

# Install necessary packages
subprocess.run(['pip', 'install', 'numpy'])
subprocess.run(['pip', 'install', 'matplotlib'])
subprocess.run(['pip', 'install', 'alg'])
subprocess.run(['pip', 'install', 'math'])
# Add any other commonly used packages here
# subprocess.run(['pip', 'install', 'datetime'])
# subprocess.run(['pip', 'install', 'os'])
# subprocess.run(['pip', 'install', 'sys'])
# subprocess.run(['pip', 'install', 'random'])
# subprocess.run(['pip', 'install', 're'])
# subprocess.run(['pip', 'install', 'json'])
# subprocess.run(['pip', 'install', 'csv'])

# install pandas, scipy, seaborn, scikit-learn, statsmodels, tensorflow, keras, torch, opencv-python, pillow, requests, beautifulsoup4, flask, django, sqlalchemy, pymysql, pymongo, redis, elasticsearch
subprocess.run(['pip', 'install', 'pandas'])
subprocess.run(['pip', 'install', 'scipy'])
subprocess.run(['pip', 'install', 'seaborn'])
subprocess.run(['pip', 'install', 'scikit-learn'])
subprocess.run(['pip', 'install', 'statsmodels'])
subprocess.run(['pip', 'install', 'tensorflow'])
subprocess.run(['pip', 'install', 'keras'])
subprocess.run(['pip', 'install', 'torch'])
subprocess.run(['pip', 'install', 'opencv-python'])
subprocess.run(['pip', 'install', 'pillow'])
subprocess.run(['pip', 'install', 'requests'])
# subprocess.run(['pip', 'install', 'beautifulsoup4'])
# subprocess.run(['pip', 'install', 'flask'])
subprocess.run(['pip', 'install', 'django'])
# subprocess.run(['pip', 'install', 'sqlalchemy'])
# subprocess.run(['pip', 'install', 'pymysql'])
# subprocess.run(['pip', 'install', 'pymongo'])
# subprocess.run(['pip', 'install', 'redis'])
# subprocess.run(['pip', 'install', 'elasticsearch'])

# install jupyter notebook
subprocess.run(['pip', 'install', 'jupyter'])

# install jupyter lab
subprocess.run(['pip', 'install', 'jupyterlab'])

# install jupyter notebook extensions
# subprocess.run(['pip', 'install', 'jupyter_contrib_nbextensions'])

# # install jupyter notebook extensions
# subprocess.run(['jupyter', 'contrib', 'nbextension', 'install', '--user'])

# # enable jupyter notebook extensions
# subprocess.run(['jupyter', 'nbextension', 'enable', 'codefolding/main'])

# my github 
subprocess.run(['git', 'config', '--global', 'user.name', 'nyammar'])   

# create a repo on github
subprocess.run(['curl', '-u', 'nyammar', 'https://api.github.com/user/repos', '-d', '{"name":"python"}'])



# # upload this code to my github
# subprocess.run(['git', 'add', '.'])
# subprocess.run(['git', 'commit', '-m', 'update python and install necessary packages'])
# subprocess.run(['git', 'push'])

# print a message
print('Python and necessary packages have been updated successfully!')

#what's the shortcut to comment out a block of code in python?
# ctrl + /