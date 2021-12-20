document.getElementById("menu-icon").style.color = "black";
document.getElementsByClassName("navbar")[0].style.backgroundColor = "white";
document.getElementsByClassName("brand-logo1")[0].classList.add("d-none");
document.getElementsByClassName("navbar")[0].classList.remove("navbar-dark");
document.getElementsByClassName("navbar")[0].classList.add("navbar-light");
window.onscroll = function () {
    scrollFunction();

    function scrollFunction() {
        if (
            document.body.scrollTop > 60 ||
            document.documentElement.scrollTop > 60
        ) {
            document
                .getElementsByClassName("navbar")[0]
                .classList.add("floatingNav");
        } else {
            document
                .getElementsByClassName("navbar")[0]
                .classList.remove("floatingNav");
        }
    }
    scrollFunction();
};

function closeMenu() {
    document.getElementById("navbar").style.width = "0%";
    document.getElementsByTagName("BODY")[0].style.backgroundColor = "";
}
function openMenu() {
    document.getElementById("navbar").style.width = "20vw";
}

var accordions = document.getElementsByClassName("accordion");

for (var i = 0; i < accordions.length; i++) {
    accordions[i].onclick = function () {
        this.classList.toggle("is-open");

        var content = this.nextElementSibling;
        if (content.style.maxHeight) {
            // accordion is currently open, so close it
            content.style.maxHeight = null;
        } else {
            // accordion is currently closed, so open it
            content.style.maxHeight = content.scrollHeight + "px";
        }
    };
}
