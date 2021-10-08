let inputsearch = document.getElementById("inputsearch");
let btnSub = document.getElementById("btnSub");
let display = document.getElementById("display");

btnSub.addEventListener("click", () => {
  
  display.innerHTML = `
        <div class="container mx-auto mt-3">
        <div class="spinner-grow text-warning" role="status">
            <span class="sr-only">Loading...</span>
        </div>

        <div class="spinner-grow text-dark" role="status">
            <span class="sr-only">Loading...</span>
        </div>

        <div class="spinner-grow text-danger" role="status">
            <span class="sr-only">Loading...</span>
        </div>
        </div>
  `;

  let htmlString = "";
  if (inputsearch.value == "") {
    display.innerHTML = `<h4 class="text-center text-danger mx-auto mt-2">Value Can't Be Empty !</h4>`;
  } else {
    let url = `https://owlbot.info/api/v4/dictionary/${inputsearch.value}`;

    let params = {
      method: "GET",
      headers: {
        Authorization: "Token " + "<YOUR_AUTHORIZATION_TOKEN>",
      },
    };
    fetch(url, params)
      .then((response) => {
        if (response.status == 404) {
          return false;
        } else if (response.status == 200) {
          return response.json();
        } else {
          return false;
        }
      })
      .then((data) => {
        if (!data) {
          display.innerHTML = `<h4 class="text-center mx-auto mt-3 text-info">No Word Found !</h4>`;
        } else {      
          let i = 1;
          data.definitions.forEach((element) => {
            htmlString += `<p class="card-text">${i})  ${element.definition}, Example - ${element.example}, Type - ${element.type}</p>`;
            i++;
          });

          let card = `
                <div class="card mt-4 text-left mx-auto">
                     <div class="card-body">
                        <h5 class="card-title">Word : ${data.word} </h5>
                        <h6 class="card-subtitle mb-2 text-muted">Pronounciation : ${data.pronunciation}</h6>
                        ${htmlString}
                    </div>
                </div>`;

          display.innerHTML = card;
        }
      });
  }
});
