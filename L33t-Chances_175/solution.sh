#!/bin/bash

while :; do
    response=$(curl http://162.243.0.171/secret.php)
    if grep "^flag" <(echo $response); then
        echo "Got the flag!"
        echo $response
        break
    else
        echo "Trying again..."
    fi
done

# flag{T0O_M@ny_But10ns}
