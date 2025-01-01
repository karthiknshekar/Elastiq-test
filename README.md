#Solution to search funcitionality

#Installation Process
clone the main repo
git clone  https://github.com/karthiknshekar/Elastiq-test

#To install all project dependecies:
pip install -r requirements.txt

#In order to run  
pytest 
pytest -v 
pytest -s -v

#To generate reports we need to install html reports as follows:
pip install pytest-html

#Then run
pytest --html = report.html
or
pytest --html=reports/report.html --self-contained-html
