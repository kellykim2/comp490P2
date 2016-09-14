#! /bin/bash

# This is a little CGI program
###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The desired MIME type for the response.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.
# HTTP_USER_AGENT:   Information about the requesting client.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. 
# REQUEST_URI:       The URI of the request.
# SERVER_PROTOCOL:   Currently “HTTP/1.1”.
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address.
# SERVER_PORT:       The port of the server.

# Add a content type and a blank line

echo "X-COMP-490: ${USER}"
echo "Content-type: text/html"
echo ""

GUESTNAME=`echo "$QUERY_STRING" | grep -oE "(^|[?&])name=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
#WEBLINK =`echo "$QUERY_STRING" | grep -oE "(^|[?&])link=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`

echo '<html>'
echo '<head>'
echo '<title>Display Environment Variables </title>'
echo '<link rel="stylesheet" href="styles.css">'
echo '</head>'
echo '<body>'
echo 'Environment Variables prepared for' $GUESTNAME 
echo '<pre>'

		/usr/bin/env

echo '</pre>'
		#Below is the website you wanted to peek.
echo 'Sorry ! the peek function is not yet available. So I present you my school!'
		/usr/bin/curl http://www.csun.edu/
		#/usr/bin/curl $WEBLINK 
		
echo		'</pre>
	</body>
	</html>	'

exit 0

