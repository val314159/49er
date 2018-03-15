#!/bin/bash

if [ "$1" == "--no-sign" ]; then
    shift
else
    cat   c/n/*  2>/dev/null | openssl ripemd160 >c/n/.id
fi
echo \$Iid: >c/n/.hdr
echo 0   >c/n/.nce
echo `cat c/n/.[a-zA-Z]* 2>/dev/null`| tee c/n/.pfx | openssl ripemd160 >c/n/.~id
echo \$Id: `cat -vet      c/n/.~id`
cat       c/n/.pfx

if [ "$1" == "--prefix-only" ]; then
    shift
else
    cat       c/n/*
fi
