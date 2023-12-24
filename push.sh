#!/bin/ksh
find .  -type d -name .git -prune -o -print > /tmp/s
for i in `cat /tmp/s`
do
    git add $i
done
git commit -m a
git push origin main
\rm /tmp/s
