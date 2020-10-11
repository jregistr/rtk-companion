[
    document.querySelector("#k-nav_m_bar"),
    document.querySelector("#k-nav"),
    document.querySelector("#body-navbar-holder"),
    document.querySelector("#EditStoryComponent"),
    document.querySelector("#DictStudy"),
    document.querySelector("#sharedstories-top"),
    document.querySelector("#browse > div > div:nth-child(3)"),
    document.querySelector("#browse > div > div:nth-child(2)"),
    document.querySelector("#main_container > div > div.col-md-3.mb-1 > div.visible-md-lg.padded-box-inset.mb-1"),
].forEach((element) => {
    if(element && element.style)
        element.style.display = "none";
});

// Main container surrounding content
const mainContainer = document.querySelector("#main_container")
if(mainContainer && mainContainer.style) {
    mainContainer.style.paddingLeft = "5px"
    mainContainer.style.paddingRight = "5px"
    mainContainer.style.paddingTop = "0px"
}
