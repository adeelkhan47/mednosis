#!/usr/bin/sh

red=`tput setaf 1`
whitebg=`tput setab 7`
reset=`tput sgr0`

echo "${red}${whitebg}Updating code...${reset}"
git pull
echo "${red}${whitebg}Stopping app container${reset}"
sudo docker stop mednosis_app
sudo docker rm -f mednosis_app
sudo docker rmi mednosis_python_app -f
echo "${red}${whitebg}Rebuilding...${reset}"
yes | sudo docker-compose up -d
echo "${red}${whitebg}Deployment complete.${reset}"
