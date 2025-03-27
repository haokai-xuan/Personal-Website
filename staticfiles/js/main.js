document.querySelector('.js-sidebar').addEventListener('click', (event) => {
  event.preventDefault();
  const sidebar = document.querySelector('.sidebar');
  sidebar.style.display = 'flex';
  sidebar.classList.add('visible');

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
  sidebar.classList.remove('visible');
  sidebar.classList.add('closing');
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