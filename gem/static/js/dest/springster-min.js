!function(){"use strict";var e,t=function(){var e=document.getElementById("more-link");if(e&&null===document.getElementById("articles-more")){var t=document.createElement("div");e.parentNode.insertBefore(t,e),t.appendChild(e),t.setAttribute("id","articles-more"),t.addEventListener("click",function(e){e.preventDefault();var t,n,d,a=e.target;"A"==a.tagName&&a.classList.contains("more-link")&&(a.classList.add("call-to-action__button--loader"),a.setAttribute("value",""),a.innerHTML="",t=a.getAttribute("data-next"),n=function(e){a.parentNode.insertAdjacentHTML("beforeend",e),a.parentNode.removeChild(a)},(d=window.XMLHttpRequest?new XMLHttpRequest:new ActiveXObject("Microsoft.XMLHTTP")).open("GET",t),d.onreadystatechange=function(){3<d.readyState&&200==d.status&&n(d.responseText)},d.setRequestHeader("X-Requested-With","XMLHttpRequest"),d.send())})}};e=function(){document.documentElement.className="",document.body.classList.add("toggle-hide"),function(){var a=document.getElementById("header-wrapper"),o=document.getElementById("content-wrapper");document.getElementById("nav-list");window.addEventListener("scroll",function(){var e=this.y-window.pageYOffset,t=window.scrollY,n=document.getElementById("header-wrapper").clientHeight,d=document.getElementById("language-bar").clientHeight;0<t&&320<window.innerWidth&&(a.classList.add("header-fixed"),o.style.paddingTop=n+"px"),0<e&&n<t&&320<window.innerWidth?(a.style.transform="translate3d(0px, "+-d+"px, 0px)",o.style.paddingTop=n+"px"):n<t?a.style.transform="translate3d(0px, "+-n+"px, 0px)":(e<0||t<n)&&(a.style.transform="translate3d(0px, 0px, 0px)"),this.y=window.pageYOffset})}(),t(),function(){for(var e=document.querySelectorAll(".call-to-action__button"),t=0;t<e.length;t++)e[t].addEventListener("click",function(e){setTimeout(this.classList.add("active"),1e3)})}()},"interactive"===document.readyState||"complete"===document.readyState?e():document.addEventListener("DOMContentLoaded",e)}();