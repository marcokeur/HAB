<!DOCTYPE html>
<html lang="en">
  {include file="frontend/header.tpl"}
  <body ng-app="habApp">
    {include file="frontend/navigation.tpl"}
    <div class="container">
    	{block name="container"}Define content in block 'container'{/block}       
    </div><!-- /.container -->
    
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
    
    {block name="javascript"}
    <script src="js/hab.js"></script>
    <script src="js/ng-hab.js"></script>

    {/block}
  </body>
</html>
