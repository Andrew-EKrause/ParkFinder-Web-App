
// Use the asynchronous function to obtain the proper 
// data from the National Park Services (NPS) API.
// async function getParksData() {
//     const myURL = new URL(window.location.href);

//     const search = myURL.search;

//     // The await keyword lets js know that it needs to wait until it
//     // gets a response back to continue.
//     var response = await fetch(`https://developer.nps.gov/api/v1/parks${search}&api_key=XApMBEDd2SIXa1aX7bakVem1E28W0wWgtHuGn3SF`);

//     // We then need to convert the data into JSON format.
//     var parksData = await response.json();
//     console.log(myURL);
//     console.log(search);
//     console.log(parksData.data);
//     const html = parksData.data.map(park => {
//         return `<h2><a href="${park.url}">${park.fullName}</a></h2>
//         <h4>${park.description}</h4><br>`
//     }).join('');
//     document.querySelector("#search_results").insertAdjacentHTML("afterbegin", html);
//     console.log(html);
//     return parksData.data;
// }
// console.log(getParksData());