#!/bin/bash
if [ -e changes.txt ]
then
  git push origin master
else
echo "no changes"
fi
