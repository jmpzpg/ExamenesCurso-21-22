<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <xsl:template match="aplicaciones">
    
    <html>
      <head>
        <meta charset="utf-8"/>
        <title>Enunciado 2 del exámen</title>
        <link rel="stylesheet" type="text/css" href="Enunciado2.css"></link>
      </head>
      <body>
        
        <table>
          <caption> Aplicaciones  </caption>
          <thead>
            <tr>
              <th>Denominación</th>
              <th>Evaluación</th>
              <th>Web</th>
              
            </tr>
          </thead>
          <tbody>
            <tr> 
              <xsl:apply-templates>
               
              </xsl:apply-templates> 
            </tr>
          </tbody>
          
        </table>
      </body>
    </html>
    
  </xsl:template>  
  
  <xsl:template match="detalle">
    <xsl:variable name="url" select="web"/>
    <tr>
      
      <td> <xsl:value-of select="denominacion"/> </td>
      <td> <xsl:value-of select="evaluacion"/> </td>
      <!--<td> <xsl:value-of select="web"/> </td>-->
      <td> <a href="{$url}" target="_blank" ><xsl:value-of select="web"/></a> </td>
      
    </tr>
    
  </xsl:template>
  
  
</xsl:stylesheet>
