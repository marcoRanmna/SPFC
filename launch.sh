#!/bin/sh
echo "======= Initilazing ======="
export PYTHONPATH="${PYTHONPATH}:${PWD}/application"

echo "======= Requirements ======="
pip install -r requirements.txt

echo "======= Launching Docker ======="
#cd docker/
#docker-compose up --build -d
#cd ..

echo "======= Launching ======="
python ./application/view/cli/startup.py

echo "exit 0"
