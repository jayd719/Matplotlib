






// Initialize the application
function initialize() {
  document.getElementById('resultssection').style.display = "flex"
  // Update the time every second
  const startTime = new Date(document.getElementById("creation-time").innerText)
  setInterval(() => updateTime(startTime), 1000);
  updateTime(startTime);
}

// Call the initialize function to start the app
initialize();


// Update and display the time elapsed since a given start time
function updateTime(startTime) {
  const timeElement = document.getElementById("creation-time");

  if (!timeElement) return;

  // Get the current time
  const now = new Date();

  // Calculate the time difference in milliseconds
  const timeDifference = now - startTime;

  // Convert milliseconds to hours, minutes, and seconds
  const hours = Math.floor(timeDifference / (1000 * 60 * 60));
  const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

  // Format the time elapsed string
  const timeString = `${hours}h ${minutes}m ${seconds}s`;

  // Update the content of the element
  timeElement.textContent = `Created: ${timeString} Ago`;
}


