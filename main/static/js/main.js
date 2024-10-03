document.querySelector('.js-sidebar').addEventListener('click', (event) => {
  event.preventDefault();
  const sidebar = document.querySelector('.sidebar');
  sidebar.style.display = 'flex';

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
  sidebar.style.display = 'none';
}
