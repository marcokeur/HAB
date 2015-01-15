<?php

# Include confiuration files and the smarty library.
require_once("inc/lib/smarty/Smarty.class.php");
require_once("inc/mysqlDb.php");

$smarty = new Smarty;
$smarty->display('frontend/index.tpl');

?>
