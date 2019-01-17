#!/bin/bash

textreset=$(tput sgr0) # reset the foreground colour
cyan=$(tput setaf 6)
green=$(tput setaf 2)
yellow=$(tput setaf 3)

echo "[${green}1/5${textreset}]${cyan} Creating deploy branch...${textreset}"
git checkout -b "deploy" --quiet >/dev/null

echo "[${green}2/5${textreset}] ${cyan}Building dependencies...${textreset}"
npm run bundle-dev >/dev/null

echo "[${green}3/5${textreset}] ${cyan}Committing dependencies to deploy branch...${textreset}"
git add flickr_photo_wall/static/dist/
git commit -m "Build dependencies" >/dev/null

echo "[${green}4/5${textreset}] ${cyan}Deploying branch 'deploy' to heroku master... ${textreset}"
git push --force heroku deploy:master

echo "[${green}5/5${textreset}] ${cyan}Cleaning up deploy branch...${textreset}"
git checkout "master" --quiet >/dev/null
git branch -D deploy >/dev/null

echo "${green}Deployment Complete!${textreset}"