if [ -e changes.txt ]
then
  echo "changed done"
  git push origin main
else
echo "no changes"
fi
