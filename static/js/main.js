(function(){
  'use strict';
  // Portfolio data is supplied by Flask/Jinja from content.py.
  var works = window.PORTFOLIO_WORKS || [];
  var catName = window.PORTFOLIO_CATEGORIES || {};
  var gallery = document.getElementById('gallery');
  works.forEach(function(w){
    var el=document.createElement('div');
    el.className='work reveal';
    el.setAttribute('data-cat',w.category);
    var thumb = w.image
      ? '<img class="thumb" src="'+w.image+'" alt="'+w.title+'" loading="lazy">'
      : '<div class="thumb" style="background:linear-gradient(135deg,'+w.gradient[0]+','+w.gradient[1]+')"></div>';
    el.innerHTML=thumb+
      '<div class="overlay"><span class="cat">'+(catName[w.category] || w.category)+'</span><h4></h4></div>';
    el.querySelector('h4').textContent=w.title;
    gallery.appendChild(el);
  });

  // ---- Filtering ----
  var btns=document.querySelectorAll('.filter-btn');
  btns.forEach(function(b){
    b.addEventListener('click',function(){
      btns.forEach(function(x){x.classList.remove('active');});
      b.classList.add('active');
      var f=b.getAttribute('data-filter');
      document.querySelectorAll('.work').forEach(function(w){
        w.classList.toggle('hide', !(f==='all'||w.getAttribute('data-cat')===f));
      });
    });
  });

  // ---- Header scroll state ----
  var header=document.getElementById('header');
  window.addEventListener('scroll',function(){
    header.classList.toggle('scrolled', window.scrollY>40);
  });

  // ---- Mobile menu ----
  var burger=document.getElementById('burger'), nav=document.getElementById('navLinks');
  burger.addEventListener('click',function(){nav.classList.toggle('open');});
  nav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('open');});});

  // ---- Reveal on scroll + skill bars ----
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){
        e.target.classList.add('in');
        e.target.querySelectorAll('.bar span').forEach(function(s){s.style.width=s.getAttribute('data-w');});
        io.unobserve(e.target);
      }
    });
  },{threshold:.12});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});

  // ---- Contact form (demo) ----
  var form=document.getElementById('contactForm');
  form.addEventListener('submit',function(ev){
    ev.preventDefault();
    document.getElementById('formMsg').style.display='block';
    form.reset();
  });

  document.getElementById('yr').textContent=new Date().getFullYear();
})();
