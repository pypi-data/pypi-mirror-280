from setuptools import setup, find_packages

setup(name='ZYOpentracingGrpcio',
      version='1.7',
      description='Python OpenTracing Extensions for gRPC',
      author='LightStep',
      license='',
      install_requires=['opentracing>=2.4.0', 'grpcio>=1.63.0', 'six>=1.16.0'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'future'],
      keywords=['opentracing'],
      classifiers=[
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.8',
      ],
      packages=find_packages(exclude=['docs*', 'tests*', 'examples*']))
