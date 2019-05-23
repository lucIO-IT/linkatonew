      var openMenu = 0;
      function displayMenu() {
        var menu = document.getElementsByClassName('aside')[0];
        var button = document.getElementsByClassName('nav-icon')[0];
        if (openMenu === 0) {
            menu.style.maxWidth = '1000px';
            button.classList.add('nav-icon-active');
            openMenu = 1;
        } else {
            menu.style.maxWidth = '0';
            button.classList.remove('nav-icon-active');
            openMenu = 0;
        }
      }

      var openSearchBox = 0;
      function openSearch() {
      var search = document.getElementsByClassName('search-container-box')[0];
          if (openSearchBox === 0 ) {
            search.style.maxHeight = '1000px';
            openSearchBox = 1;
          } else {
            search.style.maxHeight = '0';
            openSearchBox = 0;
          }
      }

      var openUserMenuBox = 0;
      function openUserMenu() {
        var menu = document.getElementsByClassName('dropdown-menu')[0];
        if (openUserMenuBox === 0) {
            menu.classList.add('dropdown-menu-open');
            openUserMenuBox = 1;
        } else {
            menu.classList.remove('dropdown-menu-open');
            openUserMenuBox = 0;
        }
      }