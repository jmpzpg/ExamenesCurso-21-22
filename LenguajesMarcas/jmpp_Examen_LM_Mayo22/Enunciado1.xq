"Examen LM Mayo22 - jmpp",
"a. Muestra el nombre de todos los bailes.",
//baile/nombre/text(),
"*****************",
for $a in //baile/nombre/text()
return $a,
" ",
"b. Muestra el nombre y precio de todos los bailes de la sala 2. (Elementos
completos)",
for $a in //baile
where $a/sala = 2
return ($a/nombre, $a/precio),
" ",
"c. Muestra el nombre e identificador de todos los bailes que cuesten más de 40
euros ordenados por el identificador.",
for $a in //baile
where $a/precio > 40
order by $a/@id
return ($a/nombre/text(), $a/@id/data()),
" ",
"d. Dentro de la etiqueta <NUMBAILES> indicar el total de bailes de la academia.",
let $b := //baile
return <NUMBAILES>{count($b)}</NUMBAILES>,
" ",
"e. Mostrar el nombre y los apellidos de los profesores en forma de tabla HTML.",
<html>
<head>
</head>
<body>

<table>
<tr><th>Profesores de la academia:</th></tr>
{
for $a in /bailes/profesor
return
  <tr>
  <td>{concat($a/Nombre/text(), ' ', $a/Apellidos/text())}</td>
  </tr>
}
</table>

</body>
</html>,
" ",
"f. Muestra cada baile con los apellidos de su profesor entre paréntesis.",
for $b in //baile, $p in //Apellidos
where $b/profesor/@idProf = $p/../@id
return concat($b/nombre/text(), ' (', $p/text(),')')