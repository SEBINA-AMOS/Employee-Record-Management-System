<?php
include('includes/dbconnection.php');
error_reporting(0);
if(isset($_POST['submit']))
  {
    $FName=$_POST['FirstName'];
    $LName=$_POST['LastName'];
    $empcode=$_POST['empcode'];
    $Email=$_POST['Email'];
    $Password=$_POST['Password'];
    $ret=mysqli_query($con, "select EmpEmail from employeedetail where EmpEmail='$Email'");
    $result=mysqli_fetch_array($ret);
    if($result>0){
      $msg="This email already associated with another account";
    }
    else{
      $query=mysqli_query($con, "insert into employeedetail(EmpFname, EmpLName, EmpCode, EmpEmail,  EmpPassword) value('$FName', '$LName', '$empcode', '$Email', '$Password' )");
      if ($query) {
        $msg="You have successfully registered";
      }
      else {
        $msg="Something Went Wrong. Please try again";
      }
    }
  }
?>

<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="Employee Registration">
  <meta name="author" content="">

  <title>ERMS | New Registration Portal</title>

  <!-- Custom fonts for this template-->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="css/sb-admin-2.min.css" rel="stylesheet">
  <!-- Spectral Drape 3D, Hexagonal Vault & Smooth Cursor Styles -->
  <link href="css/spectral-drape.css" rel="stylesheet">
  <link href="css/hexagonal-vault.css" rel="stylesheet">

  <script type="text/javascript">
    function checkpass() {
      if(document.register.Password.value != document.register.RepeatPassword.value) {
        alert('Password and Repeat Password fields do not match');
        document.register.RepeatPassword.focus();
        return false;
      }
      return true;
    }
  </script>

  <style>
    body {
      background-color: #070b14 !important;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 3rem 0;
      color: #e2e8f0;
      overflow-x: hidden;
    }
  </style>

</head>

<body>

  <!-- Spectral Drape 3D Canvas -->
  <div id="spectral-drape-canvas"></div>

  <div class="container spectral-content-wrapper">

    <div class="row justify-content-center">

      <div class="col-xl-7 col-lg-9 col-md-11">

        <div class="text-center mb-4">
          <div class="spectral-badge mb-2" style="color: #34d399; border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.12);">
            Onboarding Gateway
          </div>
          <h2 class="spectral-title font-weight-bold">New Registration Portal</h2>
        </div>

        <div class="card vault-glass-card o-hidden border-0 shadow-2xl">
          <div class="card-body p-5">

            <div class="text-center mb-4">
              <div class="d-inline-flex align-items-center justify-content-center mb-3" style="width: 52px; height: 52px; border-radius: 50%; background: rgba(52, 211, 153, 0.15); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.3);">
                <i class="fas fa-user-plus fa-lg"></i>
              </div>
              <h4 class="text-white font-weight-bold mb-1">Create Staff Profile</h4>
              <p class="small text-gray-400" style="color: #94a3b8;">Enter details to register your employee account</p>
            </div>

            <?php if($msg){ ?>
              <div class="alert alert-info py-2 text-center small" style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.3); color: #7dd3fc;">
                <i class="fas fa-info-circle mr-1"></i> <?php echo $msg; ?>
              </div>
            <?php } ?>

            <form class="user" name="register" method="post" onsubmit="return checkpass();">
              <div class="form-group row mb-3">
                <div class="col-sm-6 mb-3 mb-sm-0">
                  <label class="small text-gray-300 font-weight-bold ml-1" style="color: #cbd5e1;">FIRST NAME</label>
                  <input type="text" class="form-control py-3" id="FirstName" name="FirstName" placeholder="e.g. John" required="true">
                </div>
                <div class="col-sm-6">
                  <label class="small text-gray-300 font-weight-bold ml-1" style="color: #cbd5e1;">LAST NAME</label>
                  <input type="text" class="form-control py-3" id="LastName" name="LastName" placeholder="e.g. Doe" required="true">
                </div>
              </div>

              <div class="form-group mb-3">
                <label class="small text-gray-300 font-weight-bold ml-1" style="color: #cbd5e1;">EMPLOYEE CODE (EMPID)</label>
                <input type="text" class="form-control py-3" id="empcode" name="empcode" placeholder="e.g. EMP10928" required="true">
              </div>

              <div class="form-group mb-3">
                <label class="small text-gray-300 font-weight-bold ml-1" style="color: #cbd5e1;">OFFICIAL EMAIL</label>
                <input type="email" class="form-control py-3" id="Email" name="Email" placeholder="e.g. name@company.com" required="true">
              </div>

              <div class="form-group row mb-4">
                <div class="col-sm-6 mb-3 mb-sm-0">
                  <label class="small text-gray-300 font-weight-bold ml-1" style="color: #cbd5e1;">PASSWORD</label>
                  <input type="password" class="form-control py-3" id="Password" name="Password" placeholder="Create password" required="true">
                </div>
                <div class="col-sm-6">
                  <label class="small text-gray-300 font-weight-bold ml-1" style="color: #cbd5e1;">REPEAT PASSWORD</label>
                  <input type="password" class="form-control py-3" id="RepeatPassword" name="RepeatPassword" placeholder="Confirm password" required="true">
                </div>
              </div>

              <input type="submit" name="submit" value="Complete Registration" class="btn vault-btn btn-block py-3 font-weight-bold" style="background: linear-gradient(135deg, #059669 0%, #10b981 50%, #06b6d4 100%) !important;">
            </form>

            <hr style="border-color: rgba(255, 255, 255, 0.1); margin: 2rem 0 1.5rem;">

            <div class="d-flex justify-content-between text-center">
              <a class="small" href="loginerms.php" style="color: #38bdf8; text-decoration: none;">Already have an account? Sign In</a>
              <a class="small" href="index.php" style="color: #94a3b8; text-decoration: none;">&larr; Back to Main Portal</a>
            </div>

          </div>
        </div>

      </div>

    </div>

  </div>

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
