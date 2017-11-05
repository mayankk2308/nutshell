#!/bin/sh
# script testing.sh
# generates test suite

test_folder=TestNLU

if [[ -d "$test_folder" ]]
then
    rm -r "$test_folder"
fi

mkdir TestNLU
mkdir TestNLU/TestMove
mkdir TestNLU/TestCopy
mkdir TestNLU/TestOpen
mkdir TestNLU/TestOrganize
mkdir TestNLU/TestRename

echo "this is that" > TestNLU/TestOpen/openthat.txt
echo "this is this" > TestNLU/TestOpen/openthis.txt

touch TestNLU/TestOrganize/org1.txt
touch TestNLU/TestOrganize/org2.txt
touch TestNLU/TestOrganize/org3.txt
touch TestNLU/TestOrganize/org1.pdf
touch TestNLU/TestOrganize/org2.pdf
touch TestNLU/TestOrganize/org3.pdf
touch TestNLU/TestOrganize/org1.dmg
touch TestNLU/TestOrganize/org2.dmg
touch TestNLU/TestOrganize/org3.dmg
touch TestNLU/TestOrganize/org1.png
touch TestNLU/TestOrganize/org2.png
touch TestNLU/TestOrganize/org3.png

touch TestNLU/TestRename/back.txt
touch TestNLU/TestRename/drag.txt
touch TestNLU/TestRename/hack.txt
touch TestNLU/TestRename/lack.txt
