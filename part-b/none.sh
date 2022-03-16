#!/bin/bash

RET=0

# make copy of file
cp wireworld-original.c patched.c

realout=`gcc -c wireworld-original.c`

# perform the patching
for i in $*; do
  cat patch.$i | patch -p0 patched.c > file.log
done

# try to compile
newout=`gcc -c patched.c`
if [[ "$newout" != "$realout" ]]; then
  RET=1
fi

# remove patched version
#rm rm patched.c
echo $RET
exit $RET