<?php

# Include confiuration files and the smarty library.
require_once("inc/lib/smarty/Smarty.class.php");
require_once("inc/mysqlDb.php");

$smarty = new Smarty;

# Supported pages (format url -> title)
$pages = array("home" => "home", "tracker" => "tracker", "about" => "about");
$smarty->assign("pages",$pages);

# If page not set, default page is this one.
if(!isset($_GET['page'])) {
	$_GET['page'] = "home";
}

# Make get variables available to smarty.
$smarty->assign("get",$_GET);

# Check if we know the URL
if (array_key_exists($_GET['page'],$pages)) {
	$smarty->assign("title", ucwords($_GET['page']));	
	$smarty->display("frontend/".$_GET['page'].".tpl");
} else {
	echo "Page not found";
}

?>
