/* ---------------------------------------------------------
   VIDEO RESIZE BEHAVIOR
   This script enlarges a video when it starts playing and
   returns it to its smaller size when paused.
   It applies to all <video> elements with the class "video-small".
--------------------------------------------------------- */

// Select all videos that start in small mode
const videos = document.querySelectorAll(".video-small");

// Add play/pause listeners to each video
videos.forEach((vid) => {

    // When the video starts playing, switch to large size
    vid.addEventListener("play", () => {
        vid.classList.remove("video-small");
        vid.classList.add("video-large");
    });

    // When the video is paused, return to small size
    vid.addEventListener("pause", () => {
        vid.classList.remove("video-large");
        vid.classList.add("video-small");
    });
});



/* ---------------------------------------------------------
   CLICKABLE IMAGE OVERLAY
   This script allows images with the class "clickable-image"
   to open in a fullscreen overlay when clicked.
   Clicking the overlay closes it again.
--------------------------------------------------------- */

// Select all images that should open in a fullscreen overlay
document.querySelectorAll(".clickable-image").forEach(img => {

    img.addEventListener("click", () => {

        // Create the dark overlay background
        const overlay = document.createElement("div");
        overlay.classList.add("image-overlay");

        // Create the enlarged image element
        const bigImg = document.createElement("img");
        bigImg.src = img.src; // Use the same image source

        // Add the image to the overlay
        overlay.appendChild(bigImg);

        // Add the overlay to the page
        document.body.appendChild(overlay);

        // Clicking anywhere on the overlay closes it
        overlay.addEventListener("click", () => {
            overlay.remove();
        });
    });
});


  /* ---------------------------------------------------------
     BROWSER LANGUAGE DETECTION
     This script checks the visitor's browser language and
     automatically selects the correct website language.
     
     - If the browser language starts with "nl", Dutch is used.
     - Otherwise, English becomes the default.
     
     The detected language is then passed to the setLanguage()
     function, which updates all text on the page accordingly.
  --------------------------------------------------------- */

  // Detect whether the user's browser language starts with "nl"
  const userLang = navigator.language.startsWith("nl") ? "nl" : "en";

  // Apply the detected language to the website
  setLanguage(userLang);


