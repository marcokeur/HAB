<?php

# Include confiuration files and the smarty library.
require_once("inc/lib/smarty/Smarty.class.php");
require_once("inc/mysqlDb.php");

$smarty = new Smarty;

switch($_GET['page']) {

	case "about":
		$smarty->display('frontend/about.tpl');
	break;

	case "tracker":
		$smarty->display('frontend/tracker.tpl');
	break;

	// Display index.
	default:
	        $smarty->display('frontend/index.tpl');
	break;

}


?>
