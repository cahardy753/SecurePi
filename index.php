# Isaac Schaafsma (iws3), Cliff Hardy (cah43)
# Used code from lab 9
# This file creates a webpage for our databasse
<html>
<head>
    <title>Raspberry Pi Door Log Cloud Data</title>
</head>
<body>
<h2>Raspberry Pi Door Log Cloud Data</h2>

<?php
# Connect to SQL cloud database
$host = "*****";
$user = "*****";
$pass = "*****";
$db = "defaultdb";
$port = "*****";
$con = pg_connect("host=$host port=$port dbname=$db user=$user password=$pass")
    or die ("Could not connect to SQL server\n");

# Query temperature data
$query = 'SELECT * FROM doorlog ORDER by datetime DESC LIMIT 10';
$result = pg_query($con, $query) or die('Query failed');
$array = pg_fetch_all($result);

# Output data as an HTML table
echo "<table border='1'>
<tr><th>Date and Time</th><th>Status</th></tr>";

foreach ($array as $row) {
    echo "<tr>";
    echo "<td>" . htmlspecialchars($row['datetime']) . "</td>";
    echo "<td>" . htmlspecialchars($row['status']) . "</td>";
    echo "</tr>";
}
echo "</table>";
?>
</body>
</html>
