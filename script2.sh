#!/bin/bash
if [ -e changes.txt ]
then
  echo "changed done"
  git push origin master
else
echo "no changes"
fi
