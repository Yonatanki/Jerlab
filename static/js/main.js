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
let alteonsListUrl ='http://127.0.0.1:8000/api/alteons-list/'
let alteonDetailUrl = 'http://127.0.0.1:8000/alteon-details/'

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
    fetch(`http://127.0.0.1:8000/api/alteon-details/${id}/`)
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
            // if(alteon.Usage_Days != 'None'){
            //     alteon.Usage_Days
            //     alteon.save
            //     // console.log('Alteon1: ', alteon.Usage_Days)
            // }
        })
    
    // lis[0].addEventListener('click', (e) => {
    //     id = e.target.dataset.id
    // //     console.log('Alteon4: ', lis);
    //     console.log('Alteon4: ', id);
    // })
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
        fetch(`http://127.0.0.1:8000/api/alteon-details/${id}/`)
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
            // if(alteon.Usage_Days != 'None'){
            //     alteon.Usage_Days
            //     alteon.save
            //     // console.log('Alteon1: ', alteon.Usage_Days)
            // }
        })
        // })
    }
}
    
function deleteAlteon(){
    let data= document.getElementById("delete")
    console.log('Delete function', data)
    
    id= data.dataset.id
    management = data.dataset.management
    console.log('Delete function', id)
    let answer = window.confirm('Are you sure you want to delete '+management+'?')
    console.log(answer)
    if(answer){
        console.log('BEFORE FETCH:')
        fetch(`http://127.0.0.1:8000/api/alteon-delete/${id}/`,
        {
            method: "POST"
        })
        

    }
}
    // alert('Are you sure you want to delete "172.185.150.1"?')


// function closeDialog() {
//     console.log('CLOSED FUNCTION')
//     let myTimeout = document.getElementById("demo")
//     // document.getElementById("demo")
//     myTimeout.close()
// }

  



















// alteon--form
// function aload () {
//     // (B1) AJAX LOAD JSON DATA
//     console.log('aload function:', 'Loaded')
//     fetch(homepageUrl)
//       .then(response => response.json())
//       .then(alt_list => {
//           console.log('Alt_list:', alt_list)
//           for(let i =0; i< alt_list.length; i++)
//           {
//             let alteon = alt_list[i]
//             document.getElementById("alteon--form").innerHTML = alteon['Form']
//             document.getElementById("alteon--SSL_Card").innerHTML = alteon['SSL_Card']
//             document.getElementById("alteon--Version").innerHTML = alteon['Version']
//             document.getElementById("alteon--RAM").innerHTML = alteon['RAM']
//           }
//       // (B2) BUILD HTML TABLE WITH THE GIVEN DATA
//     //   var table = "<table>";
//     //   for (let alteon of data) {
//     //     table += "<tr>";
//     //     table += "<td>" + alteon.MAC + "</td>";
//     //     table += "<td>" + alteon.Management + "</td>";
//     //     table += "</tr>";
//     //   }
//     //   table += "</table>";
//         // console.log('DATA:' , data)
    
//     })
// }

// let alteon = () => {
//     // function aloaddetail() {
//     // (B1) AJAX LOAD JSON DATA
//     let alteonDetailsbtn = document.getElementsByClassName('alteo')
   
//     console.log(alteonDetailsbtn)
//     alteonDetailsbtn.addEventListener('click', function() {
    
//         let id = target.dataset.id
//         console.log('Details was clickes/loaded:' , id)

    
//         fetch(alteonDetailUrl+id)
//         .then(response => response.json())
//         .then(alt_list => {
//             console.log('Alt_list:', alt_list)
//             for(let i =0; i< alt_list.length; i++)
//             {
//                 let alteon = alt_list[i]
//                 document.getElementById("alteon--MAC").innerHTML = alteon['MAC']
//                 document.getElementById("alteon--form").innerHTML = alteon['Form']
//                 document.getElementById("alteon--SSL_Card").innerHTML = alteon['SSL_Card']
//                 document.getElementById("alteon--Version").innerHTML = alteon['Version']
//                 document.getElementById("alteon--RAM").innerHTML = alteon['RAM']
//             }
//         })
// })
// }
// }

// alteon()




// });
// const element = document.getElementById('alteon--update');
// element.addEventListener("click", function() {
//     console.log('SUCCESS:ddffvggv')
    // document.getElementById("demo").innerHTML = "Hello World";
// });

// document.addEventListener("load", function(){
//     document.getElementById("demo").innerHTML = "Hello Wor333ld!";
//   });

// function myFunction(btn1) {
//     let btn = document.getElementsByClassName("alteon--details")
//     // fetch
//     console.log('BTN;', btn1.id)
//     fetch(`http://127.0.0.1:8000/api/alteon-details/${btn1.id}/`)
//     .then(response => response.json())
//     .then(alteon => {
//         console.log('ideeeee: ', alteon)
//         document.getElementById("alteon--RAM"+alteon.id).innerHTML = alteon['RAM']
//         console.log('SUCCESS: RAM updated')
//         if(alteon.Usage_Days != 'None'){
//             alteon.Usage_Days
//             alteon.save
//             // console.log('Alteon1: ', alteon.Usage_Days)
//         }
//     })
    
//     // console.log('BTN;', btn.id)//undifined
//     // alert(btn);
//     return console.log('fetch alteon id success')
//   }

// //   myFunction()


// let getAlteons = () => {
//     console.log('Get Alteons loaded')
//     fetch(alteonsListUrl)
//     .then(response => response.json())
//     .then(data => {
//         console.log('DATA:alteonsListUrl: ', data)
//         console.log('fetch is done')
//         // buildAlteonsList1(data)
//         // aload ()
//         // alteonEventtest(data)
//     })
//     // .then(() => {
//     //     console.log('reload Alteons is Ready')
//     //     window.location.reload();
//     // })
//     // console.log('reload Alteons is Ready')
//     // window.location.reload();
// }

// let buildAlteonsList = (alteons_list) =>{
//     // let alteonWrapper = document.getElementById('alteons-wrapper')
//     let alteonDetailsbtn = document.getElementsByClassName('alteon--details')
//     console.log('DATA:alteonsListUrl: ', alteons_list)
//     for(let i=0; alteons_list.length > i; i++){
//         let alteon = alteons_list[i]
//         console.log('DATA:alteonsListUrl: ', alteon)
//         if(alteon.Usage_Days != 'None'){
//             alteon.Usage_Days
//             alteon.save
//             console.log('Alteon1: ', alteon.Usage_Days)
//         }

//         console.log('Alteon: ', alteon['SSL_Card'])
//         document.getElementById("alteon--form").innerHTML = alteon['Form']
//         // document.getElementById("alteon--SSL_Card").innerHTML = alteon['SSL_Card']
//         // document.getElementById("alteon--Version").innerHTML = alteon['Version']
//         // document.getElementById("alteon--RAM").innerHTML = alteon['RAM']
//         console.log(alteon)

//     }
// }

// let buildAlteonsList1 = (alteons_list) =>{

//     let alteonDetailsbtn = document.getElementsByClassName('alteon--details')

//     console.log('buildAlteonsList1 : ', alteons_list)
//     for(let i=0; alteons_list.length > i; i++){
//         let alteon = alteons_list[i]
//         console.log(`buildAlteonsList1 - Alteon${i}: `, alteon)
//         fetch(`http://127.0.0.1:8000/api/alteon-details/${alteon.id}/`)
//         .then(response => response.text())
//         .then(data => {
//             console.log('id: ', alteon.id)
//             document.getElementById("alteon--RAM"+alteon.id).innerHTML = alteon['RAM']
//             // document.getElementById("alteon--RAM").innerHTML = alteon['RAM']
//             console.log('SUCCESS: load RAM')
//         })
//         if(alteon.Usage_Days != 'None'){
//             alteon.Usage_Days
//             alteon.save
//             // console.log('Alteon1: ', alteon.Usage_Days)
//         }

//         console.log('Alteon SSL: ', alteon['SSL_Card'])
//         // document.getElementById("alteon--form").innerHTML = alteon['Form']
//         // document.getElementById("alteon--RAM").innerHTML = alteon['RAM']
//         // document.getElementById("alteon--Platform").innerHTML = alteon['Platform']
//         console.log(alteon)

//     }

//     // alteonEventtest()
// }

// let a = (alteon) => {
//     console.log('A function started')
//     document.getElementById("alteon--RAM").innerHTML = alteon['RAM']
//     document.getElementById("alteon--Platform").innerHTML = alteon['Platform']
 
// }

// let alteonEventtest = (alteons_list) => {
//     let alteonDetailsbtn = document.getElementsByClassName('alteon--details')
// //     // let alteonload = document.getElementById()
// //     // aload ()
//     console.log('alteonEvent function:' , alteonDetailsbtn )
    
//     for (let i = 0; alteonDetailsbtn.length > i; i++ ){
//         alteonDetailsbtn[i].addEventListener('click', (e) => {
//         let id = e.target.dataset.id
//         console.log('loaded:' , id)
//         console.log('alteonnnnnnn : ' , alteonDetailsbtn[i].dataset.id)
//         // fetch(`http://127.0.0.1:8000/api/alteon-details${id}/`)
//         fetch(`http://127.0.0.1:8000/api/alteon-details/${id}/`)//,{
//         //     method:'POST',
//         //     headers:{
//         //         'Content-Type': 'application/json',
//         //         // "X-CSRFToken": `${crf_token}`
//         //     },
//         //     body:JSON.stringify({'value':id})
            
//         // })
//         .then(response => response.json())
//         .then( () =>{
//             console.log('ready to reload')
//             window.location.reload();
//         })
//     })
// // //     console.log('DETAIL BUTTON:', alteonDetailsbtn)
        
//     }
    
// }

// alteonEventtest()
