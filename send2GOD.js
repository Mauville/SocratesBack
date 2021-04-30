const axios = require('axios')

axios
    .post('https://0bf079191fe9.ngrok.io/log', {
        message: 6657
    })
    .then(res => {
        console.log(`statusCode: ${res.statusCode}`)
        console.log(res)
    })
    .catch(error => {
        console.error(error)
    })