"use strict";!function(){var e;e=function(){!function(){var e=document.querySelectorAll("div, a, input, button, select, textarea,ul,li"),t=0,n=[];function o(e){var o=t+e;document.querySelectorAll(".items")[t=o].focus()}(function(e){for(i=0;i<e.length;i++)e[i].className+=" items",e[i].setAttribute("tabindex",i),n.push(e[i]);return n})(e).forEach(function(e,o,t){return o,e,n=t}),document.activeElement.addEventListener("keydown",function(e){switch(e.key){case"ArrowUp":o(-1),console.log("You click on ArrowUp",e.which||e.keyCode);break;case"ArrowDown":o(1),console.log("You click on ArrowDown",e.which||e.keyCode);break;case"ArrowRight":o(1),console.log("You click on ArrowRight",e.which||e.keyCode);break;case"ArrowLeft":o(-1),console.log("You click on ArrowLeft",e.which||e.keyCode)}},!0);var c=function(){console.log("You click on SoftLeft")},r=function(){console.log("You click on Enter")},u=function(){console.log("You click on SoftRight")};document.addEventListener("keydown",function(e){switch(e.key){case"SoftLeft":c();break;case"SoftRight":u();break;case"Enter":r()}})}()},"interactive"===document.readyState||"complete"===document.readyState?e():document.addEventListener("DOMContentLoaded",e)}();