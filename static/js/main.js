// GET SEARCH FORM AND PAGE LINKS
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')
console.log('PAGE:', searchForm);
// ENSURE SEARCH FORM EXISTS
if(searchForm){
    for(let i = 0; pageLinks.length > i; i++){
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault()
        // GET THE DATA ATTRIBUTE
            let page = this.dataset.page
            console.log('PAGE:', page);
        // ADD HIDDEN SEARCH INPUT TO FORM
            searchForm.innerHTML += `<input value=${page} name="page" hidden/> `
            // SUBMIT FORM
            searchForm.submit()
        })
    }
}


// let homepageUrl = 'http://127.0.0.1:8000/api/'
let alteonsListUrl ='http://172.185.95.16/api/alteons-list/'
let alteonDetailUrl = 'http://172.185.95.16/alteon-details/'

let getHome = () => {
    console.log('Home Page Loaded')
    fetch(alteonsListUrl)
    .then(response => response.json())
    .then(data => {
        alteonsDetailsFetch(data)
    })

}



//   window.addEventListener('load', (event) => {
// //    getAlteons()
//     // aloaddetail()
//     // alteon()
//     // alteonEventtest()
//     // alteonDetails()
//     //  getHome()
//     console.log('The page has fully loaded');
// });

function singleAlteonFetch(){
    
    console.log('Yonatan')
    let lis = document.getElementById("alteon--d")
    // alteon = dataset.alteon
    console.log('Alteon ID: ', lis);
    id = lis.dataset.id
    console.log('Alteon4: ', lis.dataset.id);
    fetch(`http://172.185.95.16/api/alteon-details/${id}/`)
        .then(response => response.json())
        .then(alteon => {
            console.log('ide: ', alteon)
            console.log('RAM: ', alteon['RAM'])
            if(document.getElementById("alteon--RAM"+alteon.id)){
                document.getElementById("alteon--RAM"+alteon.id).innerHTML = alteon['RAM']
                document.getElementById("alteon--Platform"+alteon.id).innerHTML = alteon['Platform']
                document.getElementById("alteon--Version"+alteon.id).innerHTML = alteon['Version']
                document.getElementById("alteon--State"+alteon.id).innerHTML = alteon['State']
                console.log('SUCCESS: RAM updated')
            }
        })
}


function alteonsDetailsFetch(btn1) {
    // let btn = document.getElementsByClassName("alteon--details")
    // fetch
    console.log('fUNCTION:', 'alteonsDetailsFetch')
    console.log('alteonsDetailsFetch BTN:', btn1)
    for(let i = 0; i < btn1.length; i++)
    {
        id = btn1[i].id
        console.log('BTN id;', id)
        fetch(`http://172.185.95.16/api/alteon-details/${id}/`)
        .then(response => response.json())
        .then(alteon => {
            console.log('ideeeee: ', alteon)
            console.log('RAM: ', alteon['RAM'])
            if(document.getElementById("alteon--RAM"+alteon.id)){
                document.getElementById("alteon--RAM"+alteon.id).innerHTML = alteon['RAM']
                document.getElementById("alteon--Platform"+alteon.id).innerHTML = alteon['Platform']
                document.getElementById("alteon--Version"+alteon.id).innerHTML = alteon['Version']
                document.getElementById("alteon--State"+alteon.id).innerHTML = alteon['State']
                console.log('SUCCESS: RAM updated')
            }
        })
    }
}
    
//function deleteAlteon(){
//    let data= document.getElementById("delete")
//    console.log('Delete function', data)
//
//    id= data.dataset.id
//    management = data.dataset.management
//    console.log('Delete function', id)
//    let answer = window.confirm('Are you sure you want to delete '+management+'?')
//    console.log(answer)
//    if(answer){
//        console.log('BEFORE FETCH:')
//        fetch(`http://172.185.95.16/api/alteon-delete/${id}/`,
//        {
//            method: "POST"
//        })
//
//
//    }
//}
    // alert('Are you sure you want to delete "172.185.150.1"?')


// function closeDialog() {
//     console.log('CLOSED FUNCTION')
//     let myTimeout = document.getElementById("demo")
//     // document.getElementById("demo")
//     myTimeout.close()
// }

  
















