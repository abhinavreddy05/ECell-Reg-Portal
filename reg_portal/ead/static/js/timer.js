// Set the date we're counting down to
let countDownDate = new Date("Oct 25, 2023 14:00:00").getTime();

// Update the count down every 1 second
let x = setInterval(function() {

  // Get today's date and time
  let now = new Date().getTime();

  // Find the distance between now and the count down date
  let distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  let days = Math.floor(distance / (1000 * 60 * 60 * 24));
  let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  let seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementsByClassName("days")[0].innerHTML = days.toString()[0];
  document.getElementsByClassName("days")[1].innerHTML = days.toString()[1];

  document.getElementsByClassName("hours")[0].innerHTML = hours.toString()[0];
  document.getElementsByClassName("hours")[1].innerHTML = hours.toString()[1];

  
  document.getElementsByClassName("minutes")[0].innerHTML = minutes.toString()[0];
  document.getElementsByClassName("minutes")[1].innerHTML = minutes.toString()[1];

  
  document.getElementsByClassName("seconds")[0].innerHTML = seconds.toString()[0];
  document.getElementsByClassName("seconds")[1].innerHTML = seconds.toString()[1];

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "EXPIRED";
  }
}, 1000);