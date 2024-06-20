from setuptools import setup, find_packages
import setuptools.command.build_py as build_py


class BuildPyCommand(build_py.build_py):
    def run(self):
        build_py.build_py.run(self)


setup_kwargs = dict(
    name='rmq_interface',
    version='1.3.0',
    packages=find_packages(),
    install_requires=['pika==1.0.1'],
    setup_requires=[],
    author_email=['me@maksimeremeev.com', 'rois@rois.dev'],
    cmdclass={'build_py': BuildPyCommand},
)
setup(**setup_kwargs)
