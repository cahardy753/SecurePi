<html>
<head>
    <title>Door Access Logs</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }
        table { width: 50%; margin: auto; border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 8px; text-align: center; }
    </style>
</head>
<body>

<h2>Door Access Log</h2>

<table>
    <tr>
        <th>Timestamp</th>
        <th>Status</th>
    </tr>

<?PHP
// Open SQLite database
try {
    $db = new SQLite3('/home/iws3/final_project/door_log.db');
} catch (Exception $exception) {
    echo '<p>There was an error connecting to the database!</p>';
}


// Query to retrieve the door logs from the database
$query = 'SELECT * FROM door_logs ORDER BY timestamp DESC LIMIT 10';
$result = $db->query($query) or die('Query failed');

// Loop through the results and display them in the table
while ($row = $result->fetchArray()) {
    echo "<tr><td>{$row['timestamp']}</td><td>{$row['status']}</td></tr>";
}
?>

</table>

</body>
</html>
