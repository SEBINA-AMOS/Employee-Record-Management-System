<?php
include('includes/dbconnection_supabase.php');

if ($con_supabase) {
    echo "<h1>Supabase Connection Successful!</h1>";
    echo "<p>Connected to PostgreSQL instance at <code>db.ytgpguhsghokixtsjhqc.supabase.co</code></p>";
    
    $res = pg_query($con_supabase, "SELECT count(*) FROM employeedetail");
    $count = pg_fetch_result($res, 0, 0);
    echo "<p>Total employees in Supabase: <strong>{$count}</strong></p>";
    
    $admin = pg_query($con_supabase, "SELECT AdminName, AdminuserName FROM tbladmin LIMIT 1");
    $row = pg_fetch_assoc($admin);
    echo "<p>Admin User: <strong>{$row['adminusername']}</strong> ({$row['adminname']})</p>";
} else {
    echo "<h1>Connection Failed</h1>";
}
?>
