// -----------------------------
//  Language handling
// -----------------------------

// Load saved language or default to browser language
let savedLang = localStorage.getItem("lang");
let browserLang = navigator.language.startsWith("nl") ? "nl" : "en";
let currentLang = savedLang || browserLang;

// Load the language file on page load
document.addEventListener("DOMContentLoaded", () => {
    setLanguage(currentLang);
});

// Called when user clicks NL or EN button
function changeLanguage(lang) {
    currentLang = lang;
    localStorage.setItem("lang", lang);
    setLanguage(lang);
}
