Assert in python 

Test convention 
``` 
def test_someting_test():
    a=2
    b=3
    assert a==b   
```
command to test 

```
pytest -v
```
Linting method 

https://www.python.org/dev/peps/pep-0008/

Automatically check for the erros 
```
Flake8 library 
```
black package also can be used 

Other model can be used on train_test_py file 

$ mkdir -p prediction_service/model

mkdir webapp
touch add.py

Flask function will be written 
















253  conda activate mlop_wine_project

  254  jupyter notebook

  255  jupyter lab

  256  clear

  257  touch requiremnets.txt

  258  python

  259  pip install -r requirements.txt

  260  pip install -r requirements.txt

  261  python

  262  dvc init

  263  dvc add data/InputData/winequality.csv

  264  git add .

  265  git commit -m" updating dvc and dataset"

  266  git push -u origin master

  267  python src/get_data.py

  268  python src/get_data.py

  269  git add .

  270  git commit -m"updated get data"

  271  git push origin main

  272  git push origin master

  273  git push -u origin master

  274  git remote add origin https://github.com/prash16/mlop_wine_project

  275  git push -u origin master

  276  python src/load_data.py

  277  python src/load_data.py

  278  python src/load_data.py

  279  python src/get_data.py

  280  python src/get_data.py

  281  python src/load_data.py

  282  python src/load_data.py

  283  python src/load_data.py

  284  dvc repro

  285  dvc repro

  286  python src/get_data.py

  287  python src/load_data.py

  288  python src/get_data.py

  289  python src/load_data.py

  290  dvc repro

  291  dvc repro

  292  dvc repro

  293  python src/split_data.py

  294  dvc repro

  295  dvc repro

  296  python src/train_and_evaluate.py

  297  python src/train_and_evaluate.py

  298  git add .

  299  git commit -m"stage 1 pipeline"

  300  git push -u origin master

  301  dvc repro

  302  mkdir report

  303  touch report/params.json

  304  touch report/scores.json

  305  clear

  306  dvc repro

  307  dvc repro

  308  git add .

  309  git commit -m"updated yaml file"

  310  git push -u origin master

  311  dvc repro

  312  dvc repro

  313  dvc metrics shwo

  314  dvc metrics show

  315  dvc repro

  316  dvc metrics show

  317  dvc metrics show

  318  dvc metrics diff

  319  git add .

  320  git commit -m"changes"

  321  git push -u origin master

  322  dvc metrics show

  323  dvc version

  324  dvc metrics show

  325  dvc version

  326  dvc metrics show

  327  dvc repro

  328  dvc repro

  329  dvc metrics show

  330  dvc metrics diff

  331  dvc repro

  332  dvc metrics diff

  333  dvc repro

  334  dvc metrics diff

  335  dvc metrics show

  336  dvc repro

  337  dvc metrics diff

  338  python src/train_and_evaluate.py

  339  dvc repro

  340  dvc metrics diff

  341  dvc metrics shwo

  342  dvc metrics show

  343  dvc repro

  344  dvc metrics diff

  345  dvc repro

  346  dvc repro

  347  dvc repro

  348  dvc metrics diff

  349  dvc repro

  350  dvc metrics diff

  351  dvc repro

  352  dvc metrics diff

  353  dvc metrics diff

  354  git status

  355  git add .

  356  git commit -m"changes"

  357  git push -u origin master

  358  dvc repro

  359  dvc metrics diff

  360  git add .

  361  git commit -m"changes"

  362  git push -u origin master

  363  dvc metrics diff

  364  dvc metrics diff

  365  dvc repro

  366  dvc metrics diff

  367  dvc repro

  368  dvc metrics diff

  369  dvc repro

  370  dvc metrics diff

  371  git add .

  372  git commit -m"changes"

  373  git push -u origin master

  374  dvc repro

  375  dvc metrics diff

  376  pip install -r requirements.txt

  377  touch tox.ini

  378  pytest -v
  
  379  mkdir tests

  380  touch tests/conftest.py tests/test_config.py

  381  git add .

  382  git commit -m"pytest"

  383  git push -u origin master

  384  touch tests/__init__.py

  385  pytest -v

  386  pytest -v

  387  pytest -v

  388  pytest -v

  389  pytest -v

  390  pytest -v

  391  pytest -v

  392  tox

  393  tox

  394  touch setup.py

  395  tox

  396  tox

  397  tox

  398  pip install -e .

  399  pip freeze

  400  python setup.py sdist bdist_wheel

  401  tox

  402  jupyter lab

  403  pytest -v

  404  pytest -v

  405  pytest -v

  406  pytest -v
  407  pytest -v
  408  pytest -v
  409  pytest -v
  410  pytest -v

  411  git add .

  412  git commit -m"test updated"

  413  git push -u origin master

  414  tox

  415  mkdir -p prediction_service/model

  416  mkdir webapp

  417  touch app.py

  418  history

touch prediction_service/__init__.py

touch prediction_service/prediction.py

#### creata flask application where all css and java file will reside 

mkdir -p webapp/static/css -p webapp/static/script

mkdir  webapp/templates



touch webapp/static/css/main.css

touch webapp/static/script/index.js

touch webapp/templates/index.html


touch webapp/templates/404.html webapp/templates/base.html



main css, 40 and base .. file format to be copied 

base.html --- 

find bootstarp pages 



