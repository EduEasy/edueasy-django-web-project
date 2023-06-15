const typedText = document.querySelector(".typed-text");
const cursor = document.querySelector(".cursor");

const textArray = ["Edu-Easy", "Python", "Java", "C/C++", "PHP", "MySQL", "HTML", "CSS", "JavaScript", "Web Development", "App Development", "IOS Development", "Ethical Hacking", "Free Notes", "Free Courses"];

let textArrayIndex = 0;
let charIndex = 0;

const erase = () => {
  if (charIndex > 0) {
    cursor.classList.remove('blink');
    typedText.textContent = textArray[textArrayIndex].slice(0, charIndex - 1);
    charIndex--;
    setTimeout(erase, 80);
  } else {
    cursor.classList.add('blink');
    textArrayIndex++;
    if (textArrayIndex > textArray.length - 1) {
      textArrayIndex = 0;
    }
    setTimeout(type, 1000);
  }
}

const type = () => {
  if (charIndex <= textArray[textArrayIndex].length - 1) {
    cursor.classList.remove('blink');
    typedText.textContent += textArray[textArrayIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, 120);
  } else {
    cursor.classList.add('blink');
    setTimeout(erase, 1000);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  type();
})

function cformslide() {
  var cform = document.getElementById('cform')
  var scrollval2 = window.scrollY;
  if (scrollval2 > 1200) {
    cform.style.left = '-5%';
    cform.style.transition = 'left 2.2s';
  }
}
window.addEventListener('scroll', cformslide);

function menubg() {
  var menubar = document.getElementById('navigation');
  var scrollval = window.scrollY;
  if (scrollval >= 890) {
    menubar.style.backgroundColor = 'darkslateblue';
    menubar.style.transition = 'background-color .8s ease-in-out';
  }

  else {
    menubar.style.backgroundColor = 'transparent';
    menubar.style.transition = 'background-color .8s ease-in-out';
  }
}

window.addEventListener('scroll', menubg);