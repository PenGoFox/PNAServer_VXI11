#!/bin/bash

which rpcbind
if [ $? -ne 0 ]; then
    echo command rpcbind not found
    exit -1
fi

# start rpcbind
rpcbind_pid=`ps -x | grep rpcbind | grep -v grep | awk '{print $1}'`
while [ "$rpcbind_pid" == '' ]
do
    echo starting rpcbind...
    rpcbind -i
    rpcbind_pid=`ps -ax | grep rpcbind | grep -v grep | awk '{print $1}'`
    sleep 1
done

echo rpcbind started!
echo you could exit by press Ctrl + C

python3 main.py
