!function(){"use strict";function e(e,t){var n=window.XMLHttpRequest?new XMLHttpRequest:new ActiveXObject("Microsoft.XMLHTTP");return n.open("GET",e),n.onreadystatechange=function(){n.readyState>3&&200==n.status&&t(n.responseText)},n.setRequestHeader("X-Requested-With","XMLHttpRequest"),n.send(),n}var t=function(){document.documentElement.className=""},n=function(){document.body.classList.add("toggle-hide")},o=function(){var e=document.getElementById("header-wrapper"),t=document.getElementById("content-wrapper"),n=(document.getElementById("nav-list"),function(e){window.innerWidth<1024?t.style.backgroundColor="#7300ff":t.style.backgroundColor="transparent"});window.onresize=n,window.onload=n,window.addEventListener("scroll",function(){var n=this.y-window.pageYOffset,o=window.scrollY,a=document.getElementById("header-wrapper").clientHeight,i=document.getElementById("language-bar").clientHeight;o>0&&window.innerWidth>320&&(e.classList.add("header-fixed"),t.style.paddingTop=a+"px"),n>0&&o>a&&window.innerWidth>320?(e.style.transform="translate3d(0px, "+-i+"px, 0px)",t.style.paddingTop=a+"px"):o>a?e.style.transform="translate3d(0px, "+-a+"px, 0px)":(n<0||o<a)&&(e.style.transform="translate3d(0px, 0px, 0px)"),this.y=window.pageYOffset})},a=function(){var t=document.getElementById("more-link");if(t&&null===document.getElementById("articles-more")){var n=document.createElement("div");t.parentNode.insertBefore(n,t),n.appendChild(t),n.setAttribute("id","articles-more"),n.addEventListener("click",function(t){var n=t.target;"A"==n.tagName&&n.classList.contains("more-link")&&(t.preventDefault(),n.childNodes[1].innerHTML="<img src='/static/img/loading.gif' alt='Loading...' />",e(n.getAttribute("data-next"),function(e){n.parentNode.insertAdjacentHTML("beforeend",e),n.parentNode.removeChild(n)}))})}},i=function(e,t,n){if(!(n<0||e.scrollTop==t)){var o=(t-e.scrollTop)/n*2;setTimeout(function(){e.scrollTop=e.scrollTop+o,i(e,t,n-2)},10)}},d=function(){document.getElementById("back-to-top").onclick=function(e){e.preventDefault(),i(document.body,0,100)}},r=(document.getElementsByClassName("call-to-action__button"),document.getElementsByClassName("call-to-action__button--primary"));r.length;!function(e){for(var t=0,n=0;n<e.length;n++)e[n]&&(e[n].addEventListener("click",function(e){e.preventDefault();var t=e.target;document.readyState,t.value?t.value="Spin!!!":t.innerHTML="<img src='/static/img/loading.gif' alt='Loading...' />"}),t++)}(r),function(e){"interactive"===document.readyState||"complete"===document.readyState?e():document.addEventListener("DOMContentLoaded",e)}(function(){t(),n(),o(),a(),d()})}();