"use strict";!function(){var e;e=function(){var e,t,n,o;!function(){var o=document.getElementById("header");document.getElementById("content_wrapper");window.addEventListener("scroll",function(){var e=this.y-window.pageYOffset,t=window.scrollY,n=document.getElementById("header").clientHeight+366.66;768<window.innerWidth&&(0<e&&n<t?(o.style.transform="translate3d(0px, 0px, 0px)",o.style.position="fixed"):n<t?(o.style.transform="translate3d(0px, "+-n+"px, 0px)",o.style.position="absolute"):(e<0||t<n)&&(o.style.transform="translate3d(0px, 0px, 0px)")),this.y=window.pageYOffset})}(),e=document.getElementsByClassName("surveys"),t=document.getElementsByClassName("polls"),n=e[e.length-1],o=t[t.length-1],0<e.length&&0<t.length&&(e[0].classList.add("first"),o.classList.add("last")),e.length<=0&&0<t.length&&(1==t.length?t[0].classList.add("only"):t[0].classList.add("first"),1<t.length&&o.classList.add("last")),t.length<=0&&0<e.length&&(1==e.length?e[0].classList.add("only"):e[0].classList.add("first"),1<e.length&&n.classList.add("last"))},"interactive"===document.readyState||"complete"===document.readyState?e():document.addEventListener("DOMContentLoaded",e)}(),jQuery(document).ready(function(t){t(".dropdown-toggle").click(function(){var e=t(this).parents(".dropdown").children(".dropdown-menu").is(":hidden");t(".dropdown .dropdown-menu").hide(),t(".dropdown .dropdown-toggle").removeClass("open"),e&&t(this).parents(".dropdown").children(".dropdown-menu").toggle().parents(".dropdown").children(".dropdown-toggle").addClass("open")}),t(document).bind("click",function(e){t(e.target).parents().hasClass("dropdown")||t(".dropdown .dropdown-menu").hide()}),t(document).bind("click",function(e){t(e.target).parents().hasClass("dropdown")||t(".dropdown .dropdown-toggle").removeClass("open")}),($.browser.webkit||$.browser.safari)&&console.log("This is a Webkit Engine Browser (Apple Safari or Google Chrome) with version "+$.browser.version.substr(0,1))});