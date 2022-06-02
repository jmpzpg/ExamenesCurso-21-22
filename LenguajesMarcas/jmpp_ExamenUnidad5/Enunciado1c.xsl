<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html>
          <head>
          </head>
          <body>
            <h1>Tipos de lenguajes de programación</h1>
            <xsl:apply-templates/>
          </body>
    </html>
    
  </xsl:template>
  
  <xsl:template match="clasificacion">
    <xsl:choose>
      <xsl:when test="{@criterio}='ejecucion'">
            <h2> <mark><xsl:value-of select="@criterio"/>  </mark></h2>
      </xsl:when>    
      <xsl:otherwise>
            <h2> <em><xsl:value-of select="@criterio"/>  </em></h2>
      </xsl:otherwise>
    </xsl:choose>  
  
  
    <h2> <xsl:value-of select="@criterio"/>  </h2>
    <xsl:apply-templates/>
  </xsl:template> 
    
    
 
  
  <xsl:template match="lenguaje">
      <p>
        <xsl:value-of select="@tipo"/>: 
        <xsl:value-of select="ejemplos"/>
    </p>
  </xsl:template>
  
</xsl:stylesheet>
