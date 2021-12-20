window.addEventListener("resize", resizeFunction);
var mq = window.matchMedia("(max-width:1200px)");
landtext = document.getElementsByClassName("landing-title")[0];
landsub = document.getElementsByClassName("landing-subtitle")[0];
landvec = document.getElementsByClassName("landing-vector")[0];

var land_text = ["Start your own Business with Zero Investment", "Home Loan and Balance Transfer @ 6.65%", "Zero Cost Home Loan Balance Transfer", "Get Instant and Collateral Free Business Loan","Make a Fantastic Career as an Insurance Agent","Why to Mortgage your Property When ..."];
var landsub_text = [
    "Earning Opportunity for Lifetime",
    "Exciting offer you cannot resist",
    "Salaried Customers. Minimum 50 Lacs",
    "Minimal Documents. Flexible Repayment",
    "Lucrative Commission. Flexible Timing",
    "You can Mortgage your CAR- Small Letters"
];

var i;
var counter = 0;

setInterval(function () {
    landtext.innerHTML = land_text[counter];
    landsub.innerHTML = landsub_text[counter];
    landvec.src = vec_loc[counter];

    counter++;
    if (counter >= land_text.length) {
        counter = 0;
    }
}, 5000);

function resizeFunction() {
    if (!mq.matches) {
        landtext.classList.add("display-4");
        landsub.style.fontSize = "1.5rem";
        landtext.style.fontSize = "3.4rem";
    } else {
        landtext.classList.remove("display-4");
        landsub.style.fontSize = "1rem";
        landtext.style.fontSize = "2rem";
    }
}

resizeFunction();

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

$(".count").counterUp({
    delay: 50,
    time: 2000,
});

setInterval(() => {
    if($('#v-pills-tab :nth-child(4)').hasClass('active')){
        $('#v-pills-tab :nth-child(4)').removeClass('active');
        $('#v-pills-tab :nth-child(1)').addClass('active');
    }
    else{
        $('#v-pills-tab .active').next().click();  
    }
    
    
}, 5000);