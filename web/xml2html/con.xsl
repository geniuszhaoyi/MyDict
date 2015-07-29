<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">



<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black" />
<meta name="format-detection" content="telephone=no" />
<title>advert</title>
<style type="text/css">
<!--
-->
</style>
<script type="text/javascript" src="http://ajax.microsoft.com/ajax/jquery/jquery-1.4.1.min.js"></script><script>
</script>
</head>
<body>

<xsl:for-each select="entry_list/entry">
<h2><xsl:value-of select="ew"/></h2>
<p>[<xsl:value-of select="pr"/>] <xsl:value-of select="fl"/></p>
<xsl:for-each select="def/dt">
<p><xsl:value-of select="."/></p>
</xsl:for-each>
</xsl:for-each>

</body>
</html>


</xsl:template>
</xsl:stylesheet>
