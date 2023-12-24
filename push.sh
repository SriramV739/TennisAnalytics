#!/bin/ksh

for i in `cat /tmp/s`
do
    git add $i
done
git commit -m a
git push origin main
