<?php
session_start();
include('includes/dbconnection.php');

if(isset($_POST['login']))
  {
    $uname=$_POST['username'];
    $Password=$_POST['Password'];
    $query=mysqli_query($con,"select ID from tbladmin where  AdminuserName='$uname' && Password='$Password' ");
    $ret=mysqli_fetch_array($query);
    if($ret>0){
      $_SESSION['aid']=$ret['ID'];
     header('location:welcome.php');
    }
    else{
      $msg="Invalid Details.";
    }
  }
  ?>

<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="Employee Record Management System in php and mysql">
  <meta name="author" content="Sarita Pandey">

  <title>ERMS | Administrator Portal</title>

  <!-- Custom fonts for this template-->
  <link href="../vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="../css/sb-admin-2.min.css" rel="stylesheet">
  <!-- Spectral Drape 3D, Hexagonal Vault & Smooth Cursor Styles -->
  <link href="../css/spectral-drape.css" rel="stylesheet">
  <link href="../css/hexagonal-vault.css" rel="stylesheet">

  <style>
    body {
      background-color: #070b14 !important;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2.5rem 0;
      color: #e2e8f0;
      overflow-x: hidden;
    }
  </style>

</head>

<body>

  <!-- Spectral Drape 3D Canvas -->
  <div id="spectral-drape-canvas"></div>

  <div class="container spectral-content-wrapper">

    <!-- Outer Row -->
    <div class="row justify-content-center">

      <div class="col-xl-5 col-lg-7 col-md-9">

        <div class="text-center mb-4">
          <div class="spectral-badge mb-2" style="color: #f472b6; border-color: rgba(244, 114, 182, 0.4); background: rgba(244, 114, 182, 0.12);">
            Administrator Gateway
          </div>
          <h2 class="spectral-title font-weight-bold">Administrator Portal</h2>
        </div>

        <div class="card vault-glass-card o-hidden border-0 shadow-2xl">
          <div class="card-body p-5">

            <div class="text-center mb-4">
              <div class="d-inline-flex align-items-center justify-content-center mb-3" style="width: 52px; height: 52px; border-radius: 50%; background: rgba(217, 70, 239, 0.15); color: #f472b6; border: 1px solid rgba(217, 70, 239, 0.3);">
                <i class="fas fa-user-shield fa-lg"></i>
              </div>
              <h4 class="text-white font-weight-bold mb-1">Admin Authentication</h4>
              <p class="small text-gray-400" style="color: #94a3b8;">Enter master administrative credentials</p>
            </div>

            <?php if($msg){ ?>
              <div class="alert alert-danger py-2 text-center small" style="background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.3); color: #fca5a5;">
                <i class="fas fa-exclamation-circle mr-1"></i> <?php echo $msg; ?>
              </div>
            <?php } ?>

            <form class="user" method="post" action="">
              <div class="form-group mb-3">
                <label class="small text-gray-300 font-weight-bold ml-1" style="color: #cbd5e1;">USERNAME</label>
                <input type="text" class="form-control py-3" id="username" name="username" placeholder="Username" required="true" value="admin">
              </div>

              <div class="form-group mb-4">
                <label class="small text-gray-300 font-weight-bold ml-1" style="color: #cbd5e1;">PASSWORD</label>
                <input type="password" class="form-control py-3" id="Password" name="Password" placeholder="Password" required="true" value="Test@123">
              </div>

              <input type="submit" name="login" class="btn vault-btn btn-block py-3 font-weight-bold" value="Authenticate as Admin" style="background: linear-gradient(135deg, #a855f7 0%, #7c3aed 50%, #38bdf8 100%) !important;">
            </form>

            <hr style="border-color: rgba(255, 255, 255, 0.1); margin: 2rem 0 1.5rem;">

            <div class="text-center">
              <a class="small" href="../index.php" style="color: #94a3b8; text-decoration: none;">
                <i class="fas fa-arrow-left mr-1"></i> Back to Main Portal
              </a>
            </div>

          </div>
        </div>

      </div>

    </div>

  </div>

  <!-- Bootstrap core JavaScript-->
  <script src="../vendor/jquery/jquery.min.js"></script>
  <script src="../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="../vendor/jquery-easing/jquery.easing.min.js"></script>
  <script src="../js/sb-admin-2.min.js"></script>

  <!-- Spectral Drape 3D + Smooth Cursor Components -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="../js/spectral-drape.js"></script>
  <script src="../js/smooth-cursor.js"></script>

</body>

</html>
