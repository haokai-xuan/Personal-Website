document.querySelector('.js-sidebar').addEventListener('click', (event) => {
  event.preventDefault();
  const sidebar = document.querySelector('.sidebar');
  const menuButton = document.querySelector('.menu-button');
  sidebar.style.display = 'flex';
  sidebar.classList.add('visible');
  menuButton.style.display = 'none';

  // propagation to prevent immediate closing
  event.stopPropagation();
});

document.querySelector('.js-sidebar-x').addEventListener('click', (event) => {
  event.preventDefault();
  closeSidebar();
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closeSidebar();
  }
});

document.addEventListener('click', function (e) {
  const sidebar = document.querySelector('.sidebar');
  
  if (sidebar.style.display === 'flex') {
    let node = e.target;
    let inside = false;

    while (node) {
      if (node.classList.contains('sidebar')) {
        inside = true;
        break;
      }
      node = node.parentElement;
    }

    if (!inside) {
      closeSidebar();
    }
  }
});

function closeSidebar() {
  const sidebar = document.querySelector('.sidebar');
  const menuButton = document.querySelector('.menu-button');
  sidebar.classList.remove('visible');
  sidebar.classList.add('closing');
  menuButton.style.display = 'block';
  setTimeout(() => {
    sidebar.style.display = 'none';
    sidebar.classList.remove('closing');
  }, 500);
}

const current_year = document.querySelector(".js-current-year");
current_year.innerHTML = new Date().getFullYear();

document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    })
  }, {threshold: 0.4});

  cards.forEach(card => observer.observe(card));
});

document.addEventListener("DOMContentLoaded", function () {
  const isProjectPage = window.location.pathname.startsWith("/projects/");
  const isBlogPage = window.location.pathname.startsWith("/blogs/");
  
  if (isProjectPage || isBlogPage) {
    document.querySelectorAll("img:not(.no-lightbox)").forEach((img, index) => {
      // Skip if already wrapped in a lightbox anchor
      if (img.closest("a[data-lightbox]")) return;

      const link = document.createElement("a");
      link.href = img.src;
      link.setAttribute("data-lightbox", "auto-gallery");
      link.setAttribute("data-title", img.alt || `Image ${index + 1}`);

      img.parentNode.insertBefore(link, img);
      link.appendChild(img);
    });
  }
});

