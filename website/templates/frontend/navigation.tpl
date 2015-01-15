  <nav class="navbar navbar-inverse navbar-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">High Altitude Balloon Project</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
	    {foreach $pages as $page}
            <li {if $get.page eq $page@key}class="active"{/if}><a href="/{$page@key}">{$page|capitalize}</a></li>
	    {/foreach}
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
