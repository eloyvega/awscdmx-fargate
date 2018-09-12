#!/bin/bash
tar -cjvf app.tar -C ../docs/ .
docker build -t $1 .
rm -f app.tar
