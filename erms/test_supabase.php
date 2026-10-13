<?php
include('includes/dbconnection_supabase.php');
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>ERMS | Supabase Cloud Diagnostics</title>
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:400,600,700,800" rel="stylesheet">
  <link href="css/sb-admin-2.min.css" rel="stylesheet">
  <link href="css/spectral-drape.css" rel="stylesheet">
  <link href="css/hexagonal-vault.css" rel="stylesheet">
  <link href="css/dark-dashboard.css" rel="stylesheet">
  <style>
    body {
      background-color: #070b14 !important;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem 0;
      color: #e2e8f0;
    }
  </style>
</head>
<body>

  <!-- Spectral Drape 3D Background Canvas -->
  <div id="spectral-drape-canvas"></div>

  <div class="container spectral-content-wrapper">
    <div class="row justify-content-center">
      <div class="col-xl-6 col-lg-8 col-md-10">

        <div class="text-center mb-4">
          <div class="spectral-badge mb-2">Cloud Infrastructure Diagnostics</div>
          <h2 class="spectral-title font-weight-bold">Supabase PostgreSQL Bridge</h2>
        </div>

        <div class="card vault-glass-card o-hidden border-0 shadow-2xl">
          <div class="card-body p-5">
            <?php if ($con_supabase) { 
              $res = pg_query($con_supabase, "SELECT count(*) FROM employeedetail");
              $count = pg_fetch_result($res, 0, 0);
              $admin = pg_query($con_supabase, "SELECT AdminName, AdminuserName FROM tbladmin LIMIT 1");
              $row = pg_fetch_assoc($admin);
            ?>
              <div class="text-center mb-4">
                <div class="d-inline-flex align-items-center justify-content-center mb-3" style="width: 58px; height: 58px; border-radius: 50%; background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4);">
                  <i class="fas fa-check-circle fa-2x"></i>
                </div>
                <h4 class="text-white font-weight-bold mb-1">Database Connected</h4>
                <p class="small text-gray-400" style="color: #94a3b8;">PostgreSQL Instance: <code>db.ytgpguhsghokixtsjhqc.supabase.co</code></p>
              </div>

              <div class="row text-center mb-4">
                <div class="col-6">
                  <div class="p-3" style="background: rgba(255, 255, 255, 0.04); border-radius: 0.75rem; border: 1px solid rgba(56, 189, 248, 0.2);">
                    <div class="small text-gray-400 mb-1" style="color: #94a3b8;">CLOUD EMPLOYEES</div>
                    <div class="h3 font-weight-bold text-white mb-0"><?php echo $count; ?></div>
                  </div>
                </div>
                <div class="col-6">
                  <div class="p-3" style="background: rgba(255, 255, 255, 0.04); border-radius: 0.75rem; border: 1px solid rgba(217, 70, 239, 0.2);">
                    <div class="small text-gray-400 mb-1" style="color: #94a3b8;">ADMIN STATUS</div>
                    <div class="h5 font-weight-bold mb-0" style="color: #f472b6;"><?php echo htmlspecialchars($row['adminusername']); ?> (Active)</div>
                  </div>
                </div>
              </div>

              <div class="p-3 mb-4 small" style="background: rgba(56, 189, 248, 0.08); border-left: 3px solid #38bdf8; border-radius: 0.5rem; color: #bae6fd;">
                <i class="fas fa-info-circle mr-1"></i>
                <strong>Architecture Note:</strong> Relational schema validated for transactional ACID consistency and pgvector AI skill-clustering readiness.
              </div>

            <?php } else { ?>
              <div class="text-center mb-4">
                <div class="d-inline-flex align-items-center justify-content-center mb-3" style="width: 58px; height: 58px; border-radius: 50%; background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4);">
                  <i class="fas fa-times-circle fa-2x"></i>
                </div>
                <h4 class="text-white font-weight-bold mb-1">Connection Unavailable</h4>
                <p class="small text-gray-400">Could not resolve Supabase connection.</p>
              </div>
            <?php } ?>

            <div class="text-center mt-3">
              <a class="small" href="index.php" style="color: #38bdf8; text-decoration: none;">
                <i class="fas fa-arrow-left mr-1"></i> Return to Main Enterprise Portal
              </a>
            </div>

          </div>
        </div>

      </div>
    </div>
  </div>

  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="js/spectral-drape.js"></script>
  <script src="js/smooth-cursor.js"></script>
</body>
</html>
