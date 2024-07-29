#!/usr/bin/env bash
# -*- coding: utf-8 -*-

docker build -t power_supply_control .
docker run -d --rm --name power_supply_control -p 8000:8000 power_supply_control

open http://localhost:8000/docs

docker attach power_supply_control
