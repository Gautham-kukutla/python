#!/bin/bash
if [ -e "changes.txt" ]
then
  echo "changed done"
  git push "https://github.com/Gautham-kukutla/python.git"
else
echo "no changes"
fi
