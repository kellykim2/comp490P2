#! /bin/bash

echo "Content-type: text/html"
echo ""

USERNAME=`echo "$QUERY_STRING" | sed -n 's/^.*name=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"
WHATTODO=`echo "$QUERY_STRING" | sed -n 's/^.*Check-in=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"
echo "<html><head><title>What You Said</title></head>"
echo "<body>Here's what you said:"
echo "You entered $USERNAME for username and wanted the action to be $ACTION."
echo "</body></html>"