#!/usr/bin/env bash
# -*- coding: utf-8 -*-

env_main=.env
env_template=.env.template

if [[ ! -e ${env_main} ]]
then
    cp "${env_template}"  "${env_main}"
fi

cd ~/power_supply_control

docker build -t power_supply_control .
docker run -d --rm --name power_supply_control -p 8000:8000 power_supply_control

xdg-open http://localhost:8000/docs

docker attach power_supply_control
