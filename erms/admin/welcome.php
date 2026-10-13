<?php
session_start();
include('includes/dbconnection.php');
if(strlen($_SESSION['aid']==0)){
	header('location:logout.php');
}
else {
?>
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>ERMS | Admin Dashboard</title>

  <!-- Custom fonts for this template-->
  <link href="../vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="../css/sb-admin-2.min.css" rel="stylesheet">
  <!-- Dark Dashboard Theme + Smooth Cursor -->
  <link href="../css/dark-dashboard.css" rel="stylesheet">
  <link href="../css/hexagonal-vault.css" rel="stylesheet">

</head>

<body id="page-top">

  <!-- Page Wrapper -->
  <div id="wrapper">

    <!-- Sidebar -->
    <?php include_once('includes/sidebar.php');?>
    <!-- End of Sidebar -->

    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">

      <!-- Main Content -->
      <div id="content">

        <!-- Topbar -->
       <?php include_once('includes/header.php');?>
        <!-- End of Topbar -->

        <!-- Begin Page Content -->
        <div class="container-fluid">

          <!-- Page Heading -->
          <div class="d-sm-flex align-items-center justify-content-between mb-4">
            <h1 class="h3 mb-0" style="background: linear-gradient(135deg, #ffffff 20%, #93c5fd 60%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800;">Admin Dashboard</h1>
          </div>

          <!-- Content Row -->
          <div class="row">

            <!-- Welcome Card -->
            <div class="col-xl-4 col-md-6 mb-4">
              <div class="card border-left-primary h-100 py-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="text-xs font-weight-bold text-uppercase mb-1" style="color: #818cf8 !important;">Welcome Back to ERMS!</div>

                      <?php
$adminid=$_SESSION['aid'];
$ret=mysqli_query($con,"select AdminName from tbladmin where ID='$adminid'");
$row=mysqli_fetch_array($ret);
$name=$row['AdminName'];
?>
                      <div class="h5 mb-0 font-weight-bold"><?php echo $name; ?></div>
                    </div>
                    <div class="col-auto">
                      <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(99, 102, 241, 0.15); display: flex; align-items: center; justify-content: center; border: 1px solid rgba(99, 102, 241, 0.3);">
                        <i class="fas fa-user-shield fa-lg" style="color: #818cf8;"></i>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Total Employees Card -->
            <div class="col-xl-4 col-md-6 mb-4">
              <div class="card border-left-success h-100 py-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="text-xs font-weight-bold text-uppercase mb-1" style="color: #34d399 !important;">Total Registered Employees</div>

                      <?php
$sql=mysqli_query($con,"select ID from employeedetail");
$totalemp=mysqli_num_rows($sql);
?>
                      <div class="h5 mb-0 font-weight-bold" style="font-size: 2rem;"><?php echo $totalemp; ?></div>
                    </div>
                    <div class="col-auto">
                      <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(16, 185, 129, 0.15); display: flex; align-items: center; justify-content: center; border: 1px solid rgba(16, 185, 129, 0.3);">
                        <i class="fas fa-users fa-lg" style="color: #34d399;"></i>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Manage Employees Card -->
            <div class="col-xl-4 col-md-6 mb-4">
              <div class="card border-left-info h-100 py-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="text-xs font-weight-bold text-uppercase mb-1" style="color: #38bdf8 !important;">Manage Workforce</div>
                      <a href="allemployees.php" class="small font-weight-bold" style="color: #38bdf8; text-decoration: none;">View All Employees →</a>
                    </div>
                    <div class="col-auto">
                      <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(56, 189, 248, 0.15); display: flex; align-items: center; justify-content: center; border: 1px solid rgba(56, 189, 248, 0.3);">
                        <i class="fas fa-clipboard-list fa-lg" style="color: #38bdf8;"></i>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

          </div>

        </div>
        <!-- /.container-fluid -->

      </div>
      <!-- End of Main Content -->

      <!-- Footer -->
       <?php include_once('includes/footer.php');?>
      <!-- End of Footer -->

    </div>
    <!-- End of Content Wrapper -->

  </div>
  <!-- End of Page Wrapper -->

  <!-- Scroll to Top Button-->
  <a class="scroll-to-top rounded" href="#page-top">
    <i class="fas fa-angle-up"></i>
  </a>

  <!-- Bootstrap core JavaScript-->
  <script src="../vendor/jquery/jquery.min.js"></script>
  <script src="../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="../vendor/jquery-easing/jquery.easing.min.js"></script>
  <script src="../js/sb-admin-2.min.js"></script>

</body>

</html>

<?php
}
?>
