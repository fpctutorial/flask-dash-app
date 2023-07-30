

    function I(i) {
      return document.getElementById(i);
    }

    //INITIALIZE SPEEDTEST
    var s = new Speedtest(); //create speedtest object


    //UI CODE
    var uiData = null;

    function startStop(geolocate) {

     
      $('#coordinates').html('');
      $("#ip").html('');
      $("#effective-type").html('');

      //clear the form values
      document.getElementById('f_latitude').value = '';
      document.getElementById('f_longitude').value = '';
      document.getElementById('f_upload').value = '';
      document.getElementById('f_download').value = '';
      document.getElementById('f_latency').value = '';
      document.getElementById('f_jitter').value = '';
      document.getElementById('f_isp').value = '';

      if (s.getState() == 3) {
        //speedtest is running, abort
        s.abort();
        data = null;
        I("startStopBtn").className = "";
       // I("server").disabled = false;
        initUI();
      } else {
        //call geolocator function
        geolocate();

        //test is not running, begin
        I("startStopBtn").className = "running";
        // I("shareArea").style.display = "none";
       // I("server").disabled = true;
        s.onupdate = function(data) {
          uiData = data;
        };
        s.onend = function(aborted) {
          I("startStopBtn").className = "";
        //  I("server").disabled = false;

          updateUI(true)

          if (!aborted) {

          }
        };
        s.start();
      }
    }


    //geolocation function
    function geolocate() {
      if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(position => {
          var latitude = position.coords.latitude;
          var longitude = position.coords.longitude;
          var coordinates = latitude + ', ' + longitude

          document.getElementById('f_latitude').value = latitude;
          document.getElementById('f_longitude').value = longitude;

          $('#coordinates').html(coordinates);
        }, error => {
          alert(error.code)
        });
      } else {
        alert('Not Supported')
      }
    }
    // get isp information
    function isp_info() {
      $.ajax({
        type: 'GET',
        dataType: 'json',
        url: "http://ip-api.com/json?callback=?",
        success: function(e) {
          var isp = e['as']
          //add to #data_form
          document.getElementById('f_isp').value = isp;
        }
      })
    }

    //submit_data function to submit the data to the database
    function submit_data() {


      var connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
      var type = connection.effectiveType;

      function updateConnectionStatus() {
        type = connection.effectiveType;
      }

      connection.addEventListener('change', updateConnectionStatus);

      var latitude = document.getElementById('f_latitude').value;
      var longitude = document.getElementById('f_longitude').value;
      var upload = document.getElementById('f_upload').value;
      var download = document.getElementById('f_download').value;
      var latency = document.getElementById('f_latency').value;
      var jitter = document.getElementById('f_jitter').value;
      var isp = document.getElementById('f_isp').value;


      if (type !== '') {
        $('#effective-type').text(type)
        var data = {
          effectiveType: type,
          latitude: latitude,
          longitude: longitude,
          upload: upload,
          download: download,
          latency: latency,
          jitter: jitter,
          isp: isp
        }

        $.ajax({
          url: 'php_load/submit.php',
          type: 'POST',
          dataType: "json",
          data: data,
          beforeSend: function() {},
          success: function(info) {
            if (info.error == true) {
              $('#feedback').html(`<h3 class='text-danger'>${info.message}</h3>`)
            } else {
              getShareLink();
            }
          }
        })
      } else {
        alert('Empty type')
      }

    }


    //this function reads the data sent back by the test and updates the UI
    function updateUI(forced) {
      if (!forced && s.getState() != 3) return;
      if (uiData == null) return;
      var status = uiData.testState;
      I("ip").textContent = uiData.clientIp;
      //add to #data_form
      document.getElementById('f_isp').value = uiData.clientIp;


      I("dlText").textContent = (status == 1 && uiData.dlStatus == 0) ? "..." : uiData.dlStatus;
      //add to #data_form
      document.getElementById('f_download').value = uiData.dlStatus;
     
      I("ulText").textContent = (status == 3 && uiData.ulStatus == 0) ? "..." : uiData.ulStatus;
      //add to #data_form
      document.getElementById('f_upload').value = uiData.ulStatus;
     
      I("pingText").textContent = uiData.pingStatus;
      //add to #data_form
      document.getElementById('f_latency').value = uiData.pingStatus;
      
      I("jitText").textContent = uiData.jitterStatus;
      //add to #data_form
      document.getElementById('f_jitter').value = uiData.jitterStatus;
   }


    //update the UI every frame
    window.requestAnimationFrame = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.msRequestAnimationFrame || (function(callback, element) {
      setTimeout(callback, 1000 / 60);
    });

    function frame() {
      requestAnimationFrame(frame);
      updateUI();
    }
    frame(); //start frame loop
    //function to (re)initialize UI
    function initUI() {
    
      I("dlText").textContent = "";
      I("ulText").textContent = "";
      I("pingText").textContent = "";
      I("jitText").textContent = "";
      I("ip").textContent = "";
    }