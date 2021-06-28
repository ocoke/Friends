fetch("https://cdn.jsdelivr.net/gh/oCoke/Friends@gh-pages/main.json", { method: "GET" })
  .then( res => res.json() )
  .then( json => {
    for (let i = 0; i < json.length; i++) {
      console.log(json[i])
    }
  })
