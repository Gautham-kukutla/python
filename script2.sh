#!/bin/bash
echo "entered shell script"
if [ -e "changes.txt" ]
then
  echo "changes done"
  git push 'https://github.com/Gautham-kukutla/python.git'
# git push origin main
else
echo "no changes"
fi
