<?php
// Supabase Cloud PostgreSQL Connection Bridge
$host     = "db.ytgpguhsghokixtsjhqc.supabase.co";
$port     = "5432";
$dbname   = "postgres";
$user     = "postgres";
$password = "Blackclover2237";

$conn_str = "host={$host} port={$port} dbname={$dbname} user={$user} password={$password} sslmode=require";

$con_supabase = @pg_connect($conn_str);

if (!$con_supabase) {
    error_log("Supabase connection failed: " . pg_last_error());
}
?>
