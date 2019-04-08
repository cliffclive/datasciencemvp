## Data Science MVP - v0.1

A basic data science project intended to demonstrate how to use cookiecutter-data-science for better project workflow and engineering practices.

In v0.1, we take a freshly initialized cookiecutter datascience project and remove the files that are likely to be unfamiliar to new data scientists, leaving only the ones that present a self-describing project workflow.

_Note that this is just intended to be a starting point for your first few projects. Learning how to work with the tools that have been removed from here will make your work much easier to share with others and have an impact on the broader data science community!_

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py


--------
Removed files:
(See https://datasciencemvp.com for tutorials on how to integrate these with your projects. These tools may be unfamiliar to new data scientists, and the intention behind this version is to get you up and running as quickly as possible.)

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── data
    │   ├── external       <- Data from third party sources.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
