<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="Employee Record Management System">
  <meta name="author" content="">

  <title>ERMS | Main Portal</title>

  <!-- Custom fonts for this template-->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="css/sb-admin-2.min.css" rel="stylesheet">
  <!-- Spectral Drape 3D, Hexagonal Vault & Smooth Cursor Styles -->
  <link href="css/spectral-drape.css" rel="stylesheet">
  <link href="css/hexagonal-vault.css" rel="stylesheet">

  <style>
    body {
      background-color: #070b14 !important;
      overflow-x: hidden;
      min-height: 100vh;
      color: #e2e8f0;
    }
    #content-wrapper {
      background: transparent !important;
    }
    .portal-icon {
      width: 60px;
      height: 60px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 14px;
      font-size: 1.6rem;
      margin-bottom: 1.25rem;
      transition: transform 0.3s ease;
    }
    .vault-glass-card:hover .portal-icon {
      transform: scale(1.1) rotate(4deg);
    }
  </style>

</head>

<body id="page-top">

  <!-- Spectral Drape 3D Canvas -->
  <div id="spectral-drape-canvas"></div>

  <!-- Page Wrapper -->
  <div id="wrapper" class="spectral-content-wrapper">

    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column min-vh-100">

      <!-- Main Content -->
      <div id="content" class="py-5">

        <!-- Begin Page Content -->
        <div class="container">

          <!-- Hero Heading -->
          <div class="text-center mb-5" style="padding-top: 3.5rem;">
            <div class="spectral-badge mb-3">Enterprise Workforce Network</div>
            <h1 class="display-4 spectral-title font-weight-bold mb-3">Employee Record Management</h1>
            <p class="lead text-gray-400 mx-auto" style="max-width: 640px; color: #94a3b8;">
              Centralized human resource administration, real-time employee profile management, and verified academic credentials.
            </p>
          </div>

          <div class="row justify-content-center mt-4">

            <!-- Employee Portal Card -->
            <div class="col-xl-4 col-md-6 mb-4">
              <a href="loginerms.php" style="text-decoration: none;">
                <div class="card vault-glass-card h-100 py-4">
                  <div class="card-body text-center p-4">
                    <div class="portal-icon mx-auto" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.35);">
                      <i class="fas fa-id-badge"></i>
                    </div>
                    <h5 class="font-weight-bold text-white mb-2">Employee Portal</h5>
                    <p class="small mb-4" style="color: #94a3b8;">Sign in to review credentials, education history, and career records.</p>
                    <span class="btn vault-btn btn-sm px-4 py-2">Open Portal &rarr;</span>
                  </div>
                </div>
              </a>
            </div>

            <!-- New Registration Portal Card -->
            <div class="col-xl-4 col-md-6 mb-4">
              <a href="registererms.php" style="text-decoration: none;">
                <div class="card vault-glass-card h-100 py-4">
                  <div class="card-body text-center p-4">
                    <div class="portal-icon mx-auto" style="background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35);">
                      <i class="fas fa-user-plus"></i>
                    </div>
                    <h5 class="font-weight-bold text-white mb-2">New Registration</h5>
                    <p class="small mb-4" style="color: #94a3b8;">Enroll new personnel profiles and submit credentials for review.</p>
                    <span class="btn btn-outline-light btn-sm px-4 py-2" style="border-radius: 0.65rem; border-color: rgba(255,255,255,0.25);">Enroll Now &rarr;</span>
                  </div>
                </div>
              </a>
            </div>

            <!-- Administrator Portal Card -->
            <div class="col-xl-4 col-md-6 mb-4">
              <a href="admin/" style="text-decoration: none;">
                <div class="card vault-glass-card h-100 py-4">
                  <div class="card-body text-center p-4">
                    <div class="portal-icon mx-auto" style="background: rgba(217, 70, 239, 0.15); color: #f472b6; border: 1px solid rgba(217, 70, 239, 0.35);">
                      <i class="fas fa-shield-alt"></i>
                    </div>
                    <h5 class="font-weight-bold text-white mb-2">Administrator</h5>
                    <p class="small mb-4" style="color: #94a3b8;">Enterprise oversight, workforce metrics, and access privileges.</p>
                    <span class="btn btn-outline-info btn-sm px-4 py-2" style="border-radius: 0.65rem; border-color: #38bdf8; color: #38bdf8;">Admin Console &rarr;</span>
                  </div>
                </div>
              </a>
            </div>

          </div>

          <!-- Quick Navigation to Front Landing Page -->
          <div class="text-center mt-4">
            <a href="front/index.html" class="text-xs" style="color: #64748b; text-decoration: none;">
              <i class="fas fa-external-link-alt mr-1"></i> Visit Company Public Website
            </a>
          </div>

        </div>
        <!-- /.container-fluid -->

      </div>
      <!-- End of Main Content -->

      <!-- Footer -->
      <footer class="mt-auto py-4 text-center" style="position: relative; z-index: 2; color: #475569; font-size: 0.85rem;">
        <span>Copyright &copy; ERMS &bull; Spectral 3D Drape & Smooth Cursor Active</span>
      </footer>

    </div>
    <!-- End of Content Wrapper -->

  </div>
  <!-- End of Page Wrapper -->

  <!-- Bootstrap core JavaScript-->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="vendor/jquery-easing/jquery.easing.min.js"></script>
  <script src="js/sb-admin-2.min.js"></script>

  <!-- Spectral Drape 3D + Smooth Cursor Components -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="js/spectral-drape.js"></script>
  <script src="js/smooth-cursor.js"></script>

</body>

</html>
