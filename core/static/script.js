      //This function opens menu in mobile version
      var openMenu = 0;
      document.getElementById('nav-opener').addEventListener('click', function displayMenu() {
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
      );

      //This function opens search bar in mobile vrsion
      var openSearchBox = 0;
      document.getElementById('search-opener').addEventListener('click', function openSearch() {
          var search = document.getElementsByClassName('search-container-box')[0];
              if (openSearchBox === 0 ) {
                search.style.maxHeight = '1000px';
                openSearchBox = 1;
              } else {
                search.style.maxHeight = '0';
                openSearchBox = 0;
              }
          }
      );

      //This function opens dropdown menu
      var openUserMenuBox = 0;
      document.getElementById('dropdown-opener').addEventListener('click', function openUserMenu() {
            var menu = document.getElementsByClassName('dropdown-menu')[0];
            if (openUserMenuBox === 0) {
                menu.classList.add('dropdown-menu-open');
                openUserMenuBox = 1;
            } else {
                menu.classList.remove('dropdown-menu-open');
                openUserMenuBox = 0;
            }
          }
      );

      //This function opens dialog box
      var lessonForks = document.getElementsByClassName('fork-lesson')
    	var dialogs = document.getElementsByClassName('dialog-box');
		function openDialog() {
			for (var i = 0; i < dialogs.length; i++){
				dialogs[i].classList.remove('dialog-box-open');
			}
			var el = this.firstElementChild;

			if (el.classList.contains("var-open")) {
				el.classList.remove('dialog-box-open');
				el.classList.remove('var-open');
			} else {
				el.classList.add('dialog-box-open');
				el.classList.add('var-open');
			}
		}
		for (var i = 0; i < lessonForks.length; i++) {
			lessonForks[i].addEventListener('click', openDialog, false);
		}

	  //This function opens course detail sections
	  var detailBtns = document.getElementsByClassName('box-list');
	  var detailSections = document.getElementsByClassName('detail-section');

	  function showSection() {
	    for (var i = 0; i < detailSections.length; i++) {
	        detailSections[i].style.display = 'none';
	    }
	    var target = this.getAttribute('data-target');
	    document.getElementById(target).style.display = 'block';
	    for (var i = 0; i < detailBtns.length; i++) {
	        detailBtns[i].classList.add('unactive');
	    }
	    this.classList.remove('unactive');
	  }

	  for (var i = 0; i < detailBtns.length; i++) {
	    detailBtns[i].addEventListener('click', showSection, false);
	  }





