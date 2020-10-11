//Logo navbar that says Koohie
const logoNavBar = document.querySelector("#k-nav_m_bar")
logoNavBar.style.display = "none";

const logoNavBarPar = document.querySelector("#k-nav")
logoNavBarPar.style.display = "none";

//Fixed Navbar spaceholder
const spacer = document.querySelector("#body-navbar-holder")
spacer.style.display = "none"

// Edit story box. Box where user add their custom story
const editStory = document.querySelector("#EditStoryComponent")
editStory.style.display = "none"

// Main container surrounding content
const mainContainer = document.querySelector("#main_container")
mainContainer.style.paddingLeft = "5px"
mainContainer.style.paddingRight = "5px"
mainContainer.style.paddingTop = "0px"

// Dictionary header
const dictStudy = document.querySelector("#DictStudy")
dictStudy.style.display = "none"

// shared top stories header
const sharedtop = document.querySelector("#sharedstories-top")
sharedtop.style.display = "none"

// left and right buttons next to search box
const rightSearchBtn = document.querySelector("#browse > div > div:nth-child(3)")
const leftSearchBtn = document.querySelector("#browse > div > div:nth-child(2)")
leftSearchBtn.style.display = "none"
rightSearchBtn.style.display = "none"

const linksBox = document.querySelector("#main_container > div > div.col-md-3.mb-1 > div.visible-md-lg.padded-box-inset.mb-1")
if (linksBox) {
    linksBox.style.display = "none"
}
