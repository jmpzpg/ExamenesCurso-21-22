<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html>
          <head>
              <style>
                    table {margin-left: 50px;}
                    table td {padding: 10px; border-left: 2px red solid; border-right: 2px red solid;}
                    ol li{text-transform: capitalize;}
              </style>
          </head>
          <body>
            <h1>Tipos de lenguajes de programación</h1>
            <h3>Todo depende del criterio de clasificación:</h3>
            <table>
              <tr>
                <td>
                  <ol>
                      <xsl:apply-templates/>
                  </ol>
        
                </td>
        
              </tr>
            </table>
            
            
          </body>
    </html>
    
  </xsl:template>
  
  <xsl:template match="clasificacion">
    
    <li><xsl:value-of select="@criterio"/></li>
       
    
  </xsl:template> 
    
  
</xsl:stylesheet>
