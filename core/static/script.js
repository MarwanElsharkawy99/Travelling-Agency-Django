document.addEventListener('DOMContentLoaded', function() {
  const nav = document.querySelector('nav');
  const mobileMenu = document.getElementById('mobile-menu');
  const linksContainer = document.querySelector('.links-container');

  mobileMenu.addEventListener('click', function() {
      linksContainer.classList.toggle('show-links');
  });

  window.addEventListener('scroll', function() {
      if (window.scrollY > 50) {
          nav.classList.add('scrolled');
      } else {
          nav.classList.remove('scrolled');
      }
  });
});