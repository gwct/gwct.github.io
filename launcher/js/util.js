function timeStamp()
// Retrieves current date and time for title of page.
{
    var currentdate = new Date(); 
	var datetime = currentdate.getMonth()+1 + "."
					+ currentdate.getDate()  + "." 
					+ currentdate.getFullYear() + " @ "  
					+ currentdate.getHours() + ":"  
					+ currentdate.getMinutes() + ":" 
					+ currentdate.getSeconds();
    document.write('<title>Launcher - ' + datetime + '</title>');
}

///////////////////////////////////////////////////////

function updateClock()
// Gets and formats the current time.
{
    var months = [ "Jan", "Feb", "Mar", "April", "May", "June",
                    "July", "Aug", "Sep", "Oct", "Nov", "Dec" ];
    var currentTime = new Date ( );
    
    var currentHours = currentTime.getHours ( );
    var currentMinutes = currentTime.getMinutes ( );
    var currentSeconds = currentTime.getSeconds ( );
    var currentMonth = currentTime.getMonth();
    var currentMonthStr = months[currentMonth];
    var currentDate = currentTime.getDate(); 
    
    // Pad the minutes and seconds with leading zeros, if required
    currentMinutes = ( currentMinutes < 10 ? "0" : "" ) + currentMinutes;
    currentSeconds = ( currentSeconds < 10 ? "0" : "" ) + currentSeconds;
    
    // Choose either "AM" or "PM" as appropriate
    var timeOfDay = ( currentHours < 12 ) ? "am" : "pm";
    
    // Convert the hours component to 12-hour format if needed
    currentHours = ( currentHours > 12 ) ? currentHours - 12 : currentHours;
    
    // Convert an hours component of "0" to "12"
    currentHours = ( currentHours == 0 ) ? 12 : currentHours;
    
    curtime = currentHours + ":" + currentMinutes + " " + timeOfDay
    curdate = currentMonthStr + " " + currentDate;

    // Compose the string for display
    var currentTimeString = "<center>" +curtime + "<br />" + curdate +"</center>";
    //var currentTimeString = currentSeconds;

    // Update the time display
    document.getElementById("clock").innerHTML = currentTimeString;

    // <iframe scrolling="no" frameborder="no" clocktype="html5" style="overflow:hidden;border:0;margin:0;padding:0;width:120px;height:40px;"src="https://www.clocklink.com/html5embed.php?clock=043&timezone=EST&color=white&size=120&Title=&Message=&Target=&From=2018,1,1,0,0,0&Color=white"></iframe>
    // <iframe src="http://free.timeanddate.com/clock/i6odrl28/n3723/fn14/fs20/fcfff/tct/pct/tt0/tw1/tm1/ts1/tb4" frameborder="0" width="174" height="50" allowTransparency="true"></iframe>
    // v2.0 clock format
}

///////////////////////////////////////////////////////

function setBackground()
// Gets the current background image file based on the current time and writes style into body tag.
// Body tag also include call to updateClock.
{
    var currentdate = new Date(); 
    var curhour = currentdate.getHours();
    var curdate = currentdate.getDate();
    var dateflag = 1;
	if(curhour > 12){
		curhour = curhour - 12;
    }
    if(curhour == 0){
        curhour = 12
    }
    if(curdate % 2 == 0){
        dateflag = 2;
    }
    var bg = "launcher/img/bg/bg" + curhour + "-" + dateflag + ".jpg"
    if(window.innerWidth < 1025){
        bg = "launcher/img/bg/bg" + curhour + "-" + dateflag + "-m.jpg"
    }
    document.write("<body onload=\"updateClock(); setInterval('updateClock()', 1000 )\" style='background-image: url(" + bg + ");'>");
}

///////////////////////////////////////////////////////

function searchEnter(i)
// Handles the search forms.
{  
    if(i==1){
        var queryString = document.getElementById('sbox1').value;
        var url = 'https://duckduckgo.com/?q=' + queryString;
        window.location.href = url;
        // Opens in same tab.
    }
    if(i==2){
        var queryString = document.getElementById('sbox2').value;
        var url = 'https://scholar.google.com/scholar?q=' + queryString;
        window.open(url,'_blank');
        // Opens in new tab.
    }
    if(i==3){
        var queryString = document.getElementById('sbox3').value;
        var url = 'https://en.wikipedia.org/wiki/' + queryString;
        window.open(url,'_blank');
        // Opens in new tab.
    }
}

///////////////////////////////////////////////////////

function getWeather()
// Writes the weather widget.
{
    document.write("<a class='weatherwidget-io' href='https://forecast7.com/en/39d17n86d53/bloomington/?unit=us' data-label_1='' data-icons='Climacons Animated' data-textcolor='#ffffff' data-font='Arimo'>BLOOMINGTON WEATHER</a>");
    !function(d,s,id){
        var js,fjs=d.getElementsByTagName(s)[0];
        if(!d.getElementById(id)){
            js=d.createElement(s);
            js.id=id;
            js.src='https://weatherwidget.io/js/widget.min.js';
            fjs.parentNode.insertBefore(js,fjs);
        }
    }
    (document,'script','weatherwidget-io-js');

    // https://weatherwidget.io/ 
    // Noscript: set weatherwidget.io and forecast7.com to TRUSTED
    
    // <a class="weatherwidget-io" href="https://forecast7.com/en/39d17n86d53/bloomington/?unit=us" data-label_1="BLOOMINGTON" data-icons="Climacons Animated" data-days="5" data-theme="weather_one" >BLOOMINGTON</a>
    // <script>
    //     !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
    // </script>
    // v2.0 settings
}


///////////////////////////////////////////////////////

function iotd()
// Gets the image of the day based on the date.
{
    var currentdate = new Date(); 
	var curdate = currentdate.getDate();
	document.write('<center><img class="pure-img" src="launcher/img/iotd/iotd' + curdate + '.jpg"></center>');
}