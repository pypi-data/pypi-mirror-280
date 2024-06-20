#!/bin/sh

# These are pretty hacky and need to be cleaned up, but serve a purpose.

# Set REAL_TESTING_TOKEN for more tests.

set -ex

export SPORESTACK_ENDPOINT=https://api.sporestack.com
# export SPORESTACK_ENDPOINT=http://127.0.0.1:8000

export SPORESTACK_DIR=$(pwd)/dummydotsporestackfolder

rm -r $SPORESTACK_DIR || true
mkdir $SPORESTACK_DIR

sporestack version
sporestack version | grep '[0-9]\.[0-9]\.[0-9]'

sporestack api-endpoint
sporestack api-endpoint | grep "$SPORESTACK_ENDPOINT"

sporestack token list

sporestack token import importediminvalid --key "imaninvalidkey"
sporestack token list | grep importediminvalid
sporestack token list | grep imaninvalidkey
sporestack server launch --no-quote --token neverbeencreated --operating-system debian-12 --days 1 2>&1 | grep 'does not exist'

# Online tests start here.

sporestack server launch --no-quote --token importediminvalid --operating-system debian-12 --days 1 2>&1 | grep 'String should have at least'

sporestack server flavors | grep vcpu
sporestack server operating-systems | grep debian-12
sporestack server regions | grep sfo3
sporestack api-changelog

if [ -z "$REAL_TESTING_TOKEN" ]; then
	rm -r $SPORESTACK_DIR
	echo "REAL_TESTING_TOKEN not set, not finishing tests."
	echo Success
	exit 0
else
	echo "REAL_TESTING_TOKEN is set, will continue testing."
fi

sporestack token import realtestingtoken --key "$REAL_TESTING_TOKEN"
sporestack token balance realtestingtoken | grep -F '$'
sporestack token info realtestingtoken
sporestack token messages realtestingtoken
sporestack token servers realtestingtoken
sporestack token invoices realtestingtoken
sporestack token topup realtestingtoken --currency xmr --dollars 26 --no-wait

sporestack server list --token realtestingtoken
SSHKEYFILE="$SPORESTACK_DIR/id_ed25519.pub"
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIO5JfslJFj8Yilb3PmU43vkGI8R91mpcz/44RW3T1/SK" > "$SSHKEYFILE"
sporestack server launch --no-quote --token realtestingtoken --operating-system debian-12 --days 1 --hostname sporestackpythonintegrationtestdelme --ssh-key-file "$SSHKEYFILE"
sporestack server list --token realtestingtoken | grep sporestackpythonintegrationtestdelme
sporestack server topup --token realtestingtoken --hostname sporestackpythonintegrationtestdelme --days 1
sporestack server info --token realtestingtoken --hostname sporestackpythonintegrationtestdelme
MACHINE_ID=$(sporestack server json --token realtestingtoken --hostname sporestackpythonintegrationtestdelme | jq -r .machine_id)
sporestack server autorenew-enable --token realtestingtoken --hostname sporestackpythonintegrationtestdelme
sporestack server autorenew-disable --token realtestingtoken --hostname sporestackpythonintegrationtestdelme
sporestack server update-hostname "$MACHINE_ID" --hostname "new" | grep sporestackpythonintegrationtestdelme
sporestack server update-hostname "$MACHINE_ID" --hostname ""
sporestack server update-hostname "$MACHINE_ID" --hostname "new again" | grep set
sporestack server update-hostname "$MACHINE_ID" --hostname sporestackpythonintegrationtestdelme
sporestack server start --token realtestingtoken --hostname sporestackpythonintegrationtestdelme
sporestack server stop --token realtestingtoken --hostname sporestackpythonintegrationtestdelme
sporestack server rebuild --token realtestingtoken --hostname sporestackpythonintegrationtestdelme
sporestack server delete --token realtestingtoken --hostname sporestackpythonintegrationtestdelme
sporestack server forget --token realtestingtoken --hostname sporestackpythonintegrationtestdelme

sporestack token create newtoken --currency xmr --dollars 27 --no-wait

rm -r $SPORESTACK_DIR

echo Success
