// i18n.js

let currentLang = localStorage.getItem("lang") || "nl";
let translations = {};

function loadTranslations(lang) {
    return fetch(`/static/i18n/${lang}.json`)
        .then(res => res.json())
        .then(data => {
            translations = data;
            applyTranslations();
        });
}

function applyTranslations() {
    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        const text = key.split('.').reduce((o, i) => o?.[i], translations);

        if (text) {
            el.innerHTML = text;
        }
    });
}

function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem("lang", lang);
    loadTranslations(lang);
}

// initial load
loadTranslations(currentLang);
