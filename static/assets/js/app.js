/*
 Template Name: Zoogler - Bootstrap 4 Admin Dashboard
 Author: Mannatthemes
 Website: www.mannatthemes.com
 File: Main js
 */

!function ($) {
    "use strict";

    //Body

    var MainApp = function () {
        this.$body = $("body"),
            this.$wrapper = $("#wrapper"),
            this.$leftMenuButton = $('.button-menu-mobile'),
            this.$menuItem = $('.has_sub > a')
    };

    //Slim Scroll

    MainApp.prototype.initSlimscroll = function () {
        $('.slimscrollleft').slimscroll({
            height: 'auto',
            position: 'right',
            size: "6px",
            color: '#babbde'
        });
    },

    //Left Menu

    MainApp.prototype.initLeftMenuCollapse = function () {
        var $this = this;
        this.$leftMenuButton.on('click', function (event) {
            event.preventDefault();
            $this.$body.toggleClass("fixed-left-void");
            $this.$wrapper.toggleClass("enlarged");
        });
    },

    //Components

    MainApp.prototype.initComponents = function () {
        $('[data-toggle="tooltip"]').tooltip();
        $('[data-toggle="popover"]').popover();
    },
    
    //Menu

    MainApp.prototype.initMenu = function () {
        var $this = this;
        $this.$menuItem.on('click', function () {
            var parent = $(this).parent();
            var sub = parent.find('> ul');

            if (!$this.$body.hasClass('sidebar-collapsed')) {
                if (sub.is(':visible')) {
                    sub.slideUp(300, function () {
                        parent.removeClass('nav-active');
                        $('.body-content').css({height: ''});
                        adjustMainContentHeight();
                    });
                } else {
                    visibleSubMenuClose();
                    parent.addClass('nav-active');
                    sub.slideDown(300, function () {
                        adjustMainContentHeight();
                    });
                }
            }
            return false;
        });

        //inner functions

        function visibleSubMenuClose() {
            $('.has_sub').each(function () {
                var t = $(this);
                if (t.hasClass('nav-active')) {
                    t.find('> ul').slideUp(300, function () {
                        t.removeClass('nav-active');
                    });
                }
            });
        }

        function adjustMainContentHeight() {
            // Adjust main content height
            var docHeight = $(document).height();
            if (docHeight > $('.body-content').height())
                $('.body-content').height(docHeight);
        }
    },

    //Menu item

    MainApp.prototype.activateMenuItem = function () {
        // === following js will activate the menu in left side bar based on url ====
        $("#sidebar-menu a").each(function () {
            if (this.href == window.location.href) {
                $(this).addClass("active");
                $(this).parent().addClass("active"); // add active to li of the current link
                $(this).parent().parent().prev().addClass("active"); // add active class to an anchor
                $(this).parent().parent().parent().addClass("active"); // add active class to an anchor
                $(this).parent().parent().prev().click(); // click the item to make it drop
            }
        });
    },

    //Loader

    MainApp.prototype.Preloader = function () {
        $(window).load(function() {
            $('#status').fadeOut();
            $('#preloader').delay(350).fadeOut('slow');
            $('body').delay(350).css({
                'overflow': 'visible'
            });
        });
    },


    MainApp.prototype.init = function () {
        this.initSlimscroll();
        this.initLeftMenuCollapse();
        this.initComponents();
        this.initMenu();
        this.activateMenuItem();
        this.Preloader();
    },

    //init
    $.MainApp = new MainApp, $.MainApp.Constructor = MainApp
}(window.jQuery),

//initializing
    function ($) {
        "use strict";
        $.MainApp.init();
    }(window.jQuery);

    document.addEventListener("DOMContentLoaded", function(event) {
   
        const showNavbar = (toggleId, navId, bodyId, headerId) =>{
        const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId)
        
        // Validate that all variables exist
        if(toggle && nav && bodypd && headerpd){
        toggle.addEventListener('click', ()=>{
        // show navbar
        nav.classList.toggle('show')
        // change icon
        toggle.classList.toggle('bx-x')
        // add padding to body
        bodypd.classList.toggle('body-pd')
        // add padding to header
        headerpd.classList.toggle('body-pd')
        })
        }
        }
        
        showNavbar('header-toggle','nav-bar','body-pd','header')
        
        /*===== LINK ACTIVE =====*/
        const linkColor = document.querySelectorAll('.nav_link')
        
        function colorLink(){
        if(linkColor){
        linkColor.forEach(l=> l.classList.remove('active'))
        this.classList.add('active')
        }
        }
        linkColor.forEach(l=> l.addEventListener('click', colorLink))
        
         // Your code to run since DOM is loaded and ready
        });