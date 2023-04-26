function startLoading() {
    document.getElementById("generate-button").style.display = "none";
    document.getElementById("loading").style.display = "block";
    var loadingText = document.getElementById("loading-text");
    var seconds = 0;
    var intervalId = setInterval(function() {
      seconds++;
      loadingText.innerHTML = "Loading..." + seconds + "s";
    }, 1000);
    setTimeout(function() {
      clearInterval(intervalId);
    }, 5000); // change 5000 to the desired number of seconds to load the data
  }
  