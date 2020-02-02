# !/usr/bin/env python

from distutils.core import setup
setup(
    name='napari-segmentation',
    packages=['napari_segmentation'],
    version='0.0.1',
    description='napari segmentation plugin.',
    maintainer='Nicholas Sofroniew',
    maintainer_email='sofroniewn@gmail.com',
    license='BSD 3-Clause',
    url='https://github.com/sofroniewn/napari-segmentation',
    keywords=['napari', 'napari-plugins', 'segmentation', ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Plugins',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Utilities',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
)
