#!/usr/bin/env bash
# -*- coding: utf-8 -*-

env_main=.env
env_template=.env.template

if [[ ! -e ${env_main} ]]
then
    cp "${env_template}"  "${env_main}"
fi

docker build -t power_supply_control .
docker run -d --rm --name power_supply_control -p 8000:8000 power_supply_control
docker container exec -i power_supply_control pytest -rA
docker stop power_supply_control
