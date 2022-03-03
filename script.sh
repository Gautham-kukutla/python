#!/bin/bash
for i in *.py
 do
  autopep8 --in-place --aggressive --aggressive i
 done
git status
