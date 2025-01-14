// Used to show which page is active
$(document).ready(function(){
    var pathname = window.location.pathname;
    var pages = ['moulures','panneaux','plinthes','corniches','indirect','decoratifs','solutions','colles',];
    $('#categ-nav > .nav-link').each(function(i) {
        if (pathname.includes(pages[i])) $(this).addClass('active');
        else if (this.className.includes('active')) $(this).removeClass('active');
    });
});
function ShowDownload() {
    var DivDownload = document.getElementById("DivDownload");
    var socialShare = document.getElementById("socialShare");
    var orac_tds = document.getElementById("orac_tds");

    if (DivDownload.style.display === "none") {
        DivDownload.style.display = "block";
        orac_tds.style.paddingBottom ='4rem';
        socialShare.style.display = "none";
    } else {
        orac_tds.style.paddingBottom ='0rem';
        socialShare.style.display = "block";
        DivDownload.style.display = "none";
    }
  }


  const ShowShare = async () => {
    var UlShare = document.getElementById("UlShare");
  
    if (navigator.share) {
        try {
               await navigator.share({
                url: document.URL,
                title: document.title,
                text: ""
              });
          } catch (e) {
            if (e.toString().includes('AbortError')) {
             
            }
          }



       
     }
     else{
    if (UlShare.style.display === "none") {
        UlShare.style.display = "block";
    } else {
        UlShare.style.display = "none";
    }
      }

  }
  document.body.innerHTML = document.body.innerHTML.replace('commande', ' Devis');