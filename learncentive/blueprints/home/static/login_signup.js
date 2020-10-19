function showForm(form) {
    var all_forms, all_buttons

        if (document.getElementById(form).style.display == "none") {
            all_buttons = document.getElementsByClassName("nav-tab");
            for (i=0; i < all_buttons.length; i++) {
                if (all_buttons[i].classList.contains('btn-secondary')) {
                    $(all_buttons[i]).removeClass('btn-secondary');
                    $(all_buttons[i]).addClass('active');
                } else {
                    $(all_buttons[i]).removeClass('active');
                    $(all_buttons[i]).addClass('btn-secondary');
                }
            }
        }



    all_forms = document.getElementsByClassName("tab-content");
    for (i=0; i < all_forms.length; i++) {
    all_forms[i].style.display = "none";
    }

    document.getElementById(form).style.display = "block"
}

document.getElementById("default-form").click()