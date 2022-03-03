#!/bin/bash
for i in *
 do
  autopep8 --in-place --aggressive --aggressive i
 done
