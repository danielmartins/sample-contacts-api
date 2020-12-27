from setuptools import setup

setup(name='contacts-app-api',
      python_requires='>=3.8',
      author='Daniel Santos',
      author_email='dan.elias@gmail.com',
      url='https://github.com/danielmartins/sample-contacts-api/',
      license='MIT',
      zip_safe=True,
      install_requires=[
          'fastapi==0.61.1',
          'gunicorn==20.0.4',
          'uvicorn==0.12.1',
          'requests==2.24.0',
          'uvloop==0.14.0',
          'httptools==0.1.1',
          "google-cloud-firestore==1.9.0",
          "pydantic[email]==1.7.3",
          "aiohttp==3.7.3"
      ])
