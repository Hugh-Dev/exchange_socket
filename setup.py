from setuptools import setup

setup(
    name='exchange_socket',
    version='1.0',
    install_requires=['flask', 'python-decouple', 'websocket-client', 'pandas', 'prettytable'],
    packages=[''],
    python_requires='>=3.8',
    url='https://github.com/Hugh-Dev/exchange_socket',
    license='GNU General Public License v3.0 ',
    author='Hugo Ramirez',
    author_email='hughpythoneer@gmail.com',
    description='Quiz - Connect to a Secure WebSocket, read the message, and process the data.'
)
