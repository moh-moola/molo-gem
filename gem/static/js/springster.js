(function() {

  'use strict';
  var domReady = function(callback) {
      document.readyState === "interactive" || document.readyState === "complete" ? callback() : document.addEventListener("DOMContentLoaded", callback);
  };

  var remNoJS = function() {
    var root = document.documentElement;
    root.className = '';
  };

  var hidePagination = function() {
    document.body.classList.add('toggle-hide');
  };

  function getAjax(url, success) {
    var xhr = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
    xhr.open('GET', url);
    xhr.onreadystatechange = function() {
      if (xhr.readyState>3 && xhr.status==200) success(xhr.responseText);
    };
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.send();
    return xhr;
  }

  var stickyHeader = function() {
    var header = document.getElementById("header-wrapper");
    var content = document.getElementById("content-wrapper");
    var menuList = document.getElementById("nav-list");

    // elastic scroll effect background fix
    var onResizing = function(event) {
      if (window.innerWidth < 768){
        content.style.backgroundColor =  "#7300ff";
      } else {
        content.style.backgroundColor =  "transparent";
      }
    };
    window.onresize = onResizing;
    window.onload = onResizing;

    window.addEventListener('scroll', function(){
      var scrollAmount = this.y - window.pageYOffset;
      var scrollPos = window.scrollY;
      var headerHeight = document.getElementById('header-wrapper').clientHeight;
      var langHeight = document.getElementById('language-bar').clientHeight;

      if (scrollPos > 0 && window.innerWidth > 320 ) {
       header.classList.add("header-fixed");
       content.style.paddingTop =  headerHeight + "px";
     }

      if(scrollAmount > 0 && scrollPos > headerHeight && window.innerWidth > 320 ){
        header.style.transform = "translate3d(0px, "+ -langHeight + "px, 0px)";
        content.style.paddingTop =  headerHeight + "px";
      } else if (scrollPos > headerHeight ) {
        header.style.transform = "translate3d(0px, "+ -headerHeight + "px, 0px)";
      } else if (scrollAmount < 0 || scrollPos < headerHeight){
        header.style.transform = "translate3d(0px, 0px, 0px)";
      }

      this.y = window.pageYOffset;
    });
  };

  var loadMore = function() {
    var moreLink = document.getElementById('more-link');
    if (moreLink) {
      var articlesMore = document.getElementById('articles-more');
      if (articlesMore === null) {
        var wrapper = document.createElement('div');
        moreLink.parentNode.insertBefore(wrapper, moreLink);
        wrapper.appendChild(moreLink);
        wrapper.setAttribute("id", "articles-more");
        wrapper.addEventListener("click", function(event) {
          event.preventDefault();
          var element = event.target;
          if (element.tagName == 'A' &&element.classList.contains("more-link")) {
            element.classList.add('call-to-action__button--loader');
            element.setAttribute('value', '');
            element.innerHTML = '';
            getAjax(element.getAttribute('data-next'), function(data){
              element.parentNode.insertAdjacentHTML('beforeend', data);
              element.parentNode.removeChild(element);
            });
           }
        });
      }
    }
  };

  var loaderAnimation = function() {
    var ctaBtn = document.querySelectorAll('.call-to-action__button--primary, .call-to-action__button-text--yellow');
    for (var i = 0; i < ctaBtn.length; i++) {
      ctaBtn[i].addEventListener('click', function(event) {
        setTimeout(this.classList.add('active'), 1000)
      });
    }
  }

  domReady(function() {
    remNoJS();
    hidePagination();
    stickyHeader();
    loadMore();
    loaderAnimation();
  });

})();
