from setuptools import setup

setup(
    name='wetsuite',
    version='0.1.3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
    ],
    url='https://github.com/WetSuiteLeiden/wetsuite-core.git',
    project_urls = {
        'Project home':'https://wetsuite.nl',
        'API docs': 'https://wetsuite.knobs-dials.com/apidocs/',
        'Source code': 'https://github.com/WetSuiteLeiden/wetsuite-core.git'
    },
    author='Wetsuite team',
    author_email='alewijnse.bart@gmail.com',
    description='A library that helps to explore dutch legal data, and to apply language processing on it',
    long_description='A library that helps to explore dutch legal data, and to apply language processing on it',
    packages=['wetsuite.datasets', 'wetsuite.helpers', 'wetsuite.datacollect', 'wetsuite.extras'],
    package_dir={"": "src"},
    python_requires=">=3",
    install_requires=[
        'lxml',                # BSD
        'bs4',                 # MIT
        'msgpack',             # Apache2
        'requests',            # Apache2
        'python-dateutil',     # Apache2
        'numpy >= 1.11.1',     # BSD
        'matplotlib >= 1.5.1', # BSD
        'spacy',               # MIT
        'pillow',              # HPND, which is permissive and GPL-compatible
        'pysftp',              # BSD; also pulls in paramiko (LGPL) 
        'wordcloud',           # MIT
        'PyMuPDF',             # AGPL (or commercial)
    ],
    extras_require={
        #  TODO: allow install of easyOCR and spacy CPU-only, to avoid needing CUDA
        
        'nogpu':[
            'torch==1.9.0+cpu',
            'torchvision==0.10.0+cpu',
            'easyocr',             # Apache2, also pulls in pytorch and CUDA;
            'spacy'
        ], 

        'gpu':[
            'torch==1.9.0',
            'torchvision==0.10.0',
            'easyocr',             # Apache2, also pulls in pytorch and CUDA;
            'spacy',
            'spacy[cuda-autodetect]',
        ], 

        # try to have gpu install be optional (this only makes sense when we explain it in our own install instructions, though)
        #'spacy-cpu':'spacy',
        #'spacy-cuda90':'spacy[cuda90]',
        #'spacy-cuda91':'spacy[cuda91]',
        #'spacy-cuda92':'spacy[cuda92]',
        #'spacy-cuda100':'spacy[cuda100]',
        #'spacy-cuda101':'spacy[cuda101]',
        #'spacy-cuda102':'spacy[cuda102]',
        #'spacy-cuda110':'spacy[cuda110]',
        #'spacy-cuda111':'spacy[cuda111]',
        #'spacy-cuda112':'spacy[cuda112]',
        #'spacy-cuda113':'spacy[cuda113]',
        #'spacy-cuda114':'spacy[cuda114]',
        #'spacy-cuda115':'spacy[cuda115]',
        #'spacy-cuda116':'spacy[cuda116]',
        #'spacy-cuda117':'spacy[cuda117]',
        #'spacy-cuda11x':'spacy[cuda11x]',
        #'spacy-cuda12x':'spacy[cuda12x]',


        'fastlang':[
            'spacy_fastlang',    # MIT
            'fasttext'           # MIT
        ],

        #'collection':

        #'spacy-transformers',  # MIT,  draws in a bunch more depdendencies, so optional; could uncomment now that it's in extras

        # CONSIDER: all?
    },
)
