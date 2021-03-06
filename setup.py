from setuptools import setup, find_packages

setup(
    name='notification_api_client',
    version='0.4',
    packages=find_packages(),
    license='MIT',
    description='Notification API Client',
    long_description=open('README.md').read(),
    install_requires=['httpx>=0.15.4,<0.23.0','attrs>=21.3.0','python-dateutil==2.8.2','boto3', 'urllib3'],
    url='https://github.com/danieljarrett74/notification-api-python-client',
    author='Daniel Jarrett',
    author_email='danieljarrett74@gmail.com',
) 