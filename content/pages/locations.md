Title: locations
Date: 2015-11-08 19:00
Modified: 2015-11-08 19:00
Tags: internal


A [google fusion table](https://www.google.com/fusiontables/DataSource?docid=1H_oE0Xo6ExfvFPIyVExXmavhNLdL5Cxk76WoZNcW) of geo-tagged articles

click on the red dots to open article info and link to article

    
    


<script type="text/javascript" src="https://maps.google.com/maps/api/js?sensor=false&amp;v=3"></script>

<script type="text/javascript">
  function initialize() {
    google.maps.visualRefresh = true;
    var isMobile = (navigator.userAgent.toLowerCase().indexOf('android') > -1) ||
      (navigator.userAgent.match(/(iPod|iPhone|iPad|BlackBerry|Windows Phone|iemobile)/));
    if (isMobile) {
      var viewport = document.querySelector("meta[name=viewport]");
      viewport.setAttribute('content', 'initial-scale=1.0, user-scalable=no');
    }
    var mapDiv = document.getElementById('googft-mapCanvas');
    mapDiv.style.width = isMobile ? '100%' : '1200px';
    mapDiv.style.height = isMobile ? '100%' : '480px';
    var map = new google.maps.Map(mapDiv, {
      center: new google.maps.LatLng(21.786919101146587, 8.106536865234375),
      zoom: 3,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    layer = new google.maps.FusionTablesLayer({
      map: map,
      heatmap: { enabled: false },
      query: {
        select: "col2",
        from: "1H_oE0Xo6ExfvFPIyVExXmavhNLdL5Cxk76WoZNcW",
        where: ""
      },
      options: {
        styleId: 3,
        templateId: 4
      }
    });

    if (isMobile) {
      var legend = document.getElementById('googft-legend');
      var legendOpenButton = document.getElementById('googft-legend-open');
      var legendCloseButton = document.getElementById('googft-legend-close');
      legend.style.display = 'none';
      legendOpenButton.style.display = 'block';
      legendCloseButton.style.display = 'block';
      legendOpenButton.onclick = function() {
        legend.style.display = 'block';
        legendOpenButton.style.display = 'none';
      }
      legendCloseButton.onclick = function() {
        legend.style.display = 'none';
        legendOpenButton.style.display = 'block';
      }
    }
  }

  google.maps.event.addDomListener(window, 'load', initialize);
</script>



<div id="googft-mapCanvas"></div>
