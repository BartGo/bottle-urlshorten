#!/bin/bash

set -e -u -o pipefail
IFS=$'\n\t'

export DATABASE_URL="sqlite:///data//sqlite.db" #"postgresql+psycopg2://cuturl:cuturl@localhost:5432/python-cuturl"
python -m pip install --user --upgrade --requirement requirements-global.txt
python -m virtualenv --clear --quiet ./env 

if [ "$OSTYPE" == "msys" ] ; then
  PYVE="Scripts"
else
  PYVE="bin"
fi

./env/$PYVE/pip install --upgrade --requirement requirements-dev.txt
./env/$PYVE/pip install --upgrade --requirement requirements.txt

echo "export DATABASE_URL=$DATABASE_URL"           > devtests.sh
#echo "export LC_ALL=en_US.utf-8"		  >> devtests.sh
#echo "export LANG=en_US.utf-8"			  >> devtests.sh
echo "export PYTHONIOENCODING=UTF-8"  >> devtests.sh

echo "./env/$PYVE/python -B manage.py tests"     >> devtests.sh
echo "printf '\nRunning feature tests\n\n'"       >> devtests.sh
echo "./env/$PYVE/behave"                         >> devtests.sh

echo "export DATABASE_URL=$DATABASE_URL"           > devrun.sh
#echo "export LC_ALL=en_US.utf-8"		  >> devrun.sh
#echo "export LANG=en_US.utf-8"			  >> devrun.sh
echo "export PYTHONIOENCODING=UTF-8"  >> devrun.sh
echo "./env/$PYVE/python -B manage.py runserver" >> devrun.sh

#echo "./env/$PYVE/pylint --output-format=parseable app/ alembic/ features/ tests/ *.py" > devlint.sh

chmod +x ./devrun.sh
chmod +x ./devtests.sh
chmod +x ./devucl.sh
chmod +x ./manage.py
#chmod +x ./devlint.sh

./devtests.sh

echo ""
echo "To start: ./devrun.sh"
echo "To test:  ./devtests.sh"
#echo "To lint:  ./devlint.sh"
echo ""
sleep 3
